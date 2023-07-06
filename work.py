# -*- coding: utf-8 -*-
from os import rename, remove
from random import choice
from re import sub, compile, findall
from concurrent.futures import ThreadPoolExecutor

from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Qt, QThread, Signal
from httpx import Client
from filetype import guess
from ujson import load


kg_api = "http://ovooa.caonm.net/API/kgdg/api.php"
kg_lyric_api = "http://ovooa.caonm.net/API/kggc/api.php"
mg_api = "http://ovooa.caonm.net/API/migu/api.php"
qq_vip_api = "http://ovooa.caonm.net/API/QQ_Music"
qq_api = "http://ovooa.caonm.net/API/qqdg/api.php"
wy_api = "http://ovooa.caonm.net/API/wydg/api.php"
github_api = "https://api.github.com/repos/ZYKsslm/BlackStone_Music_GUI/releases"
zip_url = "https://github.com/ZYKsslm/BlackStone_Music_GUI/releases/download/{}/BlackStone_Music_GUI.7z"


with open("User-Agent.json") as u:
    user_agent_json = load(u)


def update(ua):
    if ua == "random":
        headers = {
            "User-Agent": get_user_agent()
        }
    else:
        headers = {
            "User-Agent": ua
        }
    with Client(headers=headers, follow_redirects=True, timeout=None, verify=False) as client:
        resp = client.get(github_api)
        data = resp.json()[0]
        version = data["tag_name"]
        info = data["body"]
        
        return version, info
    

def updating(version, ua):
    if ua == "random":
        headers = {
            "User-Agent": get_user_agent()
        }
    else:
        headers = {
            "User-Agent": ua
        }
    url = zip_url.format(version)
    with Client(headers=headers, follow_redirects=True, timeout=None, verify=False) as client:
        resp = client.get(url)
        if not resp.status_code == 200:
            return False, resp.status_code
    with open(f"./BlackStone_Music_GUI_{version}.zip", "wb+") as f:
        f.write(resp.content)

    return True, f"./BlackStone_Music_GUI_{version}.zip"
    

def reset_name(string):
    """剔除字符 /:*?"<>| Windows操作系统下文件或文件夹名字中不允许出现以上字符"""
    pattern = compile(r'[/:*?"<>|]')
    new_string = sub(pattern=pattern, repl="", string=string)

    return new_string


def get_user_agent():
    """获取随机UA"""
    user_agent = choice(choice(list(choice(user_agent_json).values())))
    return user_agent


# 解析歌单
def import_songlist(info):
    try:
        songlist_id = int(info)
    except ValueError:
        try:
            songlist_id = findall(r'/(\d+)', info)[0]
        except IndexError:
            return False

    headers = {
        "User-Agent": get_user_agent()
    }
    url = f"https://c.y.qq.com/v8/fcg-bin/fcg_v8_playlist_cp.fcg?cv=10000&ct=19&newsong=1&tpl=wk&id={songlist_id}&g_tk=5381&platform=mac&g_tk_new_20200303=5381&loginUin=0&hostUin=0&format=json&inCharset=GB2312&outCharset=utf-8&notice=0&platform=jqspaframe.json&needNewCode=0"

    with Client(headers=headers, timeout=None) as client:
        resp = client.get(url=url)
        data = resp.json()["data"]["cdlist"][0]

    song_list = data["songlist"]
    tags = ""
    for i in data["tags"]:
        tags += f":{i['name']}"

    songlist_info = f"歌单名:{data['dissname']}\n" \
                    f"创建者:{data['nickname']}\n" \
                    f"简介:{data['desc']}\n" \
                    f"总歌数:{data['total_song_num']}\n" \
                    f"浏览人数:{data['visitnum']}\n" \
                    f"标签:{tags}"

    return songlist_info, [f"{i['name']}-{i['singer'][0]['name']}" for i in song_list], data["songids"].split(",")


# 酷狗音乐
def kg_get_music(name, ua):
    if ua == "random":
        headers = {
            "User-Agent": get_user_agent()
        }
    else:
        headers = {
            "User-Agent": ua
        }

    data = {
        "msg": name,
        "sc": 50,
        "type": "json",
    }

    with Client(headers=headers, params=data, follow_redirects=True, timeout=None) as client:
        resp = client.get(url=kg_api)
        music_info = resp.json()["data"]

    choice_list = []

    for i in music_info:
        music_name = i["name"]
        singers = i["singer"]
        choose = f"{music_name}-{singers}"

        choice_list.append(choose)

    return choice_list, None


def kg_download(name, n, path, ua):
    if ua == "random":
        headers = {
            "User-Agent": get_user_agent()
        }
    else:
        headers = {
            "User-Agent": ua
        }

    data = {
        "msg": name,
        "n": n
    }

    with Client(headers=headers, params=data, follow_redirects=True, timeout=None) as client:
        resp = client.get(url=kg_api)
        music_info = resp.json()
        try:
            music_info = music_info["data"]
        except KeyError:
            music_info = music_info["text"]
            return False, music_info
    try:
        music = music_info["url"]
    except KeyError:
        return False, "无资源"
    song = reset_name(music_info["song"])
    singer = reset_name(music_info["singer"])
    music_url = music_info["Music_Url"]
    image_url = music_info["cover"]

    with Client(headers=headers, follow_redirects=True, timeout=None) as client:
        resp = client.get(url=music)
        content = resp.content

    kind = guess(content)

    if kind is None:
        return False, False

    with open(fr"{path}/{song}-{singer}.{kind.extension}", "wb+") as f:
        f.write(content)

    music = Music(song, singer=singer, lyric=None, music_url=music_url, image_url=image_url, source="酷狗音乐")

    return True, music


def kg_lyric_download(name, task_name, n, path, ua):
    if ua == "random":
        headers = {
            "User-Agent": get_user_agent()
        }
    else:
        headers = {
            "User-Agent": ua
        }

    data = {
        "msg": name,
        "n": n
    }
    with Client(headers=headers, params=data, follow_redirects=True, timeout=None) as client:
        resp = client.get(url=kg_lyric_api)
        info = resp.json()
        try:
            info = info["data"]
        except KeyError:
            info = info["text"]
            return False, info
    
    content = info["content"].encode("utf-8")

    with open(fr"{path}/{task_name}.txt", "wb+") as f:
        f.write(content)

    return True, True


# 咪咕音乐
def mg_get_music(name, ua):
    if ua == "random":
        headers = {
            "User-Agent": get_user_agent()
        }
    else:
        headers = {
            "User-Agent": ua
        }

    data = {
        "msg": name,
        "sc": 50,
        "type": "json"
    }

    with Client(headers=headers, params=data, follow_redirects=True, timeout=None) as client:
        resp = client.get(url=mg_api)
        music_info = resp.json()["data"]

    choice_list = []

    for i in music_info:
        music_name = i["song"]
        singers = i["singer"]

        choose = f"{music_name}-{singers}"

        choice_list.append(choose)

    return choice_list, None


def mg_download(name, n, path, ua):
    if ua == "random":
        headers = {
            "User-Agent": get_user_agent()
        }
    else:
        headers = {
            "User-Agent": ua
        }

    data = {
        "msg": name,
        "n": n,
    }

    with Client(headers=headers, params=data, follow_redirects=True, timeout=None) as client:
        resp = client.get(url=mg_api)
        music_info = resp.json()["data"]

    try:
        music = music_info["musicurl"]
    except KeyError:
        return False, "无资源"
    song = reset_name(music_info["musicname"])
    singer = reset_name(music_info["singer"])
    lyric = music_info["lyric"]
    image = music_info["image"]

    with Client(headers=headers, follow_redirects=True, timeout=None) as client:
        resp = client.get(url=music)
        content = resp.content

    kind = guess(content)
    if kind is None:
        return False, False

    with open(fr"{path}/{song}-{singer}.{kind.extension}", "wb+") as f:
        f.write(content)

    music = Music(song, singer=singer, lyric=lyric, music_url=None, image_url=image, source="咪咕音乐")

    return True, music


# QQ音乐VIP
def vip_qq_get_music(name, ua):
    if ua == "random":
        headers = {
            "User-Agent": get_user_agent()
        }
    else:
        headers = {
            "User-Agent": ua
        }

    data = {
        "msg": name,
        "limit": 50
    }

    with Client(headers=headers, params=data, follow_redirects=True, timeout=None) as client:
        resp = client.get(url=qq_vip_api)
        music_info = resp.json()["data"]

    choice_list = []
    songids = []
    for i in music_info:
        music_name = i["song"]
        singers = i["singer"]
        songid = i["songid"]
        choose = f"{music_name}-{singers}"
        choice_list.append(choose)
        songids.append(songid)

    return choice_list, songids


def vip_qq_download(br, path, songid, ua, slice_num=20):
    if ua == "random":
        headers = {
            "User-Agent": get_user_agent()
        }
    else:
        headers = {
            "User-Agent": ua
        }

    data = {
        "songid": songid,
        "br": br
    }

    with Client(headers=headers, params=data, follow_redirects=True, timeout=None) as client:
        resp = client.get(url=qq_vip_api)
        info = resp.json()
    try:
        music_info = info["data"]
    except KeyError:
        return False, info["text"]

    image_url = music_info["picture"]
    song = reset_name(music_info["song"])
    singer = reset_name(music_info["singer"])
    music_url = music_info["url"]
    music = music_info["music"]

    if br < 3:
        with Client(headers=headers, follow_redirects=True, timeout=None) as client:
            resp = client.get(url=music)
            content = resp.content

        kind = guess(content)
        if kind is None:
            return False, False

        with open(fr"{path}/{song}-{singer}.{kind.extension}", "wb+") as f:
            f.write(content)
    else:
        # 多线程流式并发响应
        total = music_info["size"]

        def get_slice():
            step = total // slice_num
            arr = list(range(0, total, step))
            res = {}
            for li in range(len(arr) - 1):
                s_pos = arr[li]
                e_pos = arr[li + 1] - 1
                res.update(
                    {
                        li: [s_pos, e_pos]
                    }
                )

            res[slice_num - 1][-1] = total - 1

            return res

        def stream_download(ranges):
            order, ranges = ranges
            headers.update(
                {
                    "Range": f"bytes={ranges[0]}-{ranges[1]}"
                }
            )
            with Client(headers=headers, follow_redirects=True, timeout=None) as cli:
                r = cli.get(url=music)
                with open(f"{path}/{song}-{singer}_{order}", "wb") as m:
                    m.write(r.content)

        def combine():
            with open(f"{path}/{song}-{singer}", "wb+") as m:
                for o in range(slice_num):
                    with open(f"{path}/{song}-{singer}_{o}", "rb") as dt:
                        m.write(dt.read())
                    remove(f"{path}/{song}-{singer}_{o}")

                k = guess(m)

            rename(f"{path}/{song}-{singer}", f"{path}/{song}-{singer}.{k.extension}")

        rgs = get_slice()
        with ThreadPoolExecutor(slice_num) as pool:
            for i in rgs.items():
                pool.submit(stream_download, i)

        combine()

    music = Music(song, singer=singer, lyric=None, music_url=music_url, image_url=image_url, source="QQ音乐")

    return True, music


# QQ音乐
def qq_get_music(name, ua):
    if ua == "random":
        headers = {
            "User-Agent": get_user_agent()
        }
    else:
        headers = {
            "User-Agent": ua
        }

    data = {
        "msg": name,
        "sc": 50
    }

    with Client(headers=headers, params=data, follow_redirects=True, timeout=None) as client:
        resp = client.get(url=qq_api)
        music_info = resp.json()["data"]

    choice_list = []

    for i in music_info:
        music_name = i["song"]
        singers = i["singers"]
        choose = f"{music_name}-{singers}"

        choice_list.append(choose)

    return choice_list, None


def qq_download(name, n, path, ua):
    if ua == "random":
        headers = {
            "User-Agent": get_user_agent()
        }
    else:
        headers = {
            "User-Agent": ua
        }

    data = {
        "msg": name,
        "n": n
    }
    with Client(headers=headers, params=data, follow_redirects=True, timeout=None) as client:
        resp = client.get(url=qq_api)
        info = resp.json()
    try:
        music_info = info["data"]
    except KeyError:
        return False, info["text"]

    song = reset_name(music_info["Music"])
    music_url = music_info["Music_Url"]
    singer = reset_name(music_info["Singer"])
    lyric = music_info["lyric"]
    music = music_info["Url"]
    image_url = music_info["Cover"]

    with Client(headers=headers, follow_redirects=True, timeout=None) as client:
        resp = client.get(url=music)
        content = resp.content

    kind = guess(content)
    if kind is None:
        return False, False
    
    if kind.extension == "mp4":
        extension = "mp3"
    else:
        extension = kind.extension

    with open(fr"{path}/{song}-{singer}.{extension}", "wb+") as f:
        f.write(content)

    music = Music(song, singer=singer, lyric=lyric, music_url=music_url, image_url=image_url, source="QQ音乐_2")

    return True, music


# 网易云音乐
def wy_get_music(name, ua):
    if ua == "random":
        headers = {
            "User-Agent": get_user_agent()
        }
    else:
        headers = {
            "User-Agent": ua
        }

    data = {
        "msg": name,
        "sc": 50,
        "type": "json"
    }

    with Client(headers=headers, params=data, follow_redirects=True, timeout=None) as client:
        resp = client.get(url=wy_api)
        music_info = resp.json()["data"]

    choice_list = []

    for i in music_info:
        music_name = i["song"]
        singer_list = i["singers"]
        singer_num = len(singer_list)
        singers = ""
        if singer_num > 1:
            for s in range(singer_num):
                s += 1
                if s == singer_num:
                    singers += f"{singer_list[s - 1]}"
                else:
                    singers += f"{singer_list[s - 1]}、"
        else:
            singers = singer_list[0]

        choose = f"{music_name}-{singers}"
        choice_list.append(choose)

    return choice_list, None


def wy_download(name, n, path, ua):
    if ua == "random":
        headers = {
            "User-Agent": get_user_agent()
        }
    else:
        headers = {
            "User-Agent": ua
        }
    data = {
        "msg": name,
        "n": n,
    }

    with Client(headers=headers, params=data, follow_redirects=True, timeout=None) as client:
        resp = client.get(url=wy_api)
        info = resp.json()
        try:
            music_info = info["data"]
        except KeyError:
            return False, info["text"]
    try:
        music = music_info["Url"]
    except KeyError:
        return False, "无资源"
    song = reset_name(music_info["Music"])
    singer = reset_name(music_info["Singer"])
    music_url = music_info["Music_Url"]
    image_url = music_info["Cover"]

    with Client(headers=headers, follow_redirects=True, timeout=None) as client:
        resp = client.get(url=music)
        content = resp.content

    kind = guess(content)
    if kind is None:
        return False, False

    with open(fr"{path}/{song}-{singer}.{kind.extension}", "wb+") as f:
        f.write(content)

    music = Music(song, singer=singer, lyric=None, music_url=music_url, image_url=image_url, source="网易云音乐")

    return True, music


def myFreeMP3_get_music(name, ua):
    if ua == "random":
        headers = {
            "User-Agent": get_user_agent()
        }
    else:
        headers = {
            "User-Agent": ua
        }

    data = {

    }


class Mode(object):
    SEARCH = "search"
    DOWNLOAD = "download"
    MUSIC = "music"
    LYRIC = "lyric"
    IMPORT = "import"
    UPDATE = "update"


class Music(object):
    def __init__(self, name, singer, lyric, music_url, image_url, source):
        self.name = name
        self.singer = singer
        self.lyric = lyric
        self.music_url = music_url
        self.image_url = image_url
        self.source = source


class TaskExecuter(QThread):
    task_finish = Signal(tuple)

    def __init__(self, mode, downloader, n=None, info=None, version=None):
        super().__init__()
        self.downloader = downloader
        self.mode = mode

        self.n = n
        self.info = info
        self.version = version

        self.music_search_sources = {
            "酷狗音乐": kg_get_music,
            "QQ音乐": vip_qq_get_music,
            "QQ音乐_2": qq_get_music,
            "咪咕音乐": mg_get_music,
            "网易云音乐": wy_get_music
        }
        self.music_download_sources = {
            "酷狗音乐": kg_download,
            "QQ音乐": vip_qq_download,
            "QQ音乐_2": qq_download,
            "咪咕音乐": mg_download,
            "网易云音乐": wy_download
        }

    def run(self):

        if self.mode == Mode.SEARCH:
            get_music = self.music_search_sources[self.downloader.source]
            choice_list, songids = get_music(self.downloader.current_music, self.downloader.ua)
            self.task_finish.emit((self.mode, self.downloader, choice_list, songids))

        elif self.mode == Mode.MUSIC:
            download_music = self.music_download_sources[self.downloader.source]
            if self.downloader.source == "QQ音乐":
                info = download_music(
                    br=self.downloader.quality,
                    path=self.downloader.music_path,
                    songid=self.downloader.songids[self.n],
                    ua=self.downloader.ua,
                    slice_num=self.downloader.thread_num
                )
            else:
                info = download_music(
                    name=self.downloader.current_music,
                    n=self.n+1,
                    path=self.downloader.music_path,
                    ua=self.downloader.ua
                )
            self.task_finish.emit((self.mode, self.downloader, info))

        elif self.mode == Mode.LYRIC:
            info = kg_lyric_download(
                name=self.downloader.current_music,
                task_name=self.downloader.task_name,
                n=self.n+1,
                path=self.downloader.lyric_path,
                ua=self.downloader.ua
            )
            self.task_finish.emit((self.mode, self.downloader, info)) 

        elif self.mode == Mode.IMPORT:
            res = import_songlist(self.info)
            self.task_finish.emit((self.mode, self.downloader, res))

        elif self.mode == Mode.UPDATE:
            res = updating(self.version, self.downloader.ua)
            self.task_finish.emit((self.mode, res))

class Downloader(object):
    def __init__(self, w, ua, thread_num, music_path, lyric_path):
        self.w = w
        self.ua = ua
        self.music_path = music_path
        self.lyric_path = lyric_path
        self.thread_num = thread_num

        self.current_music = ""
        self.task_name = ""
        self.source = ""
        self.music: list[Music] = []
        self.thread_task = {}
        self.current_choices = []
        self.quality = 2
        self.songids = []

    def _task_finish(self, args: tuple):
        mode = args[0]

        if mode == Mode.SEARCH:
            downloader = args[1]
            self.current_choices, self.songids = args[2], args[3]
            self.w.musicListWidget.clear()
            self.w.musicListWidget.addItems(self.current_choices)
            self.w.mainStacked.setCurrentIndex(1)

        elif mode == Mode.MUSIC:
            downloader = args[1]
            info = args[2]
            if info[0]:
                self.music.append(info[1])
                try:
                    item = self.w.taskList.findItems(downloader.task_name, Qt.MatchFlag.MatchExactly)[0]
                    self.w.taskList.takeItem(self.w.taskList.row(item))
                except IndexError:
                    pass
                
                QMessageBox.information(self.w, "下载成功", f"{self.task_name}\n下载完成")
            else:
                QMessageBox.warning(self.w, "下载失败", f"'{self.task_name}'下载失败:\n{info[1]}")
        
        elif mode == Mode.LYRIC:
            downloader = args[1]
            info = args[2]
            if info[0]:
                try:
                    item = self.w.taskList.findItems(downloader.task_name, Qt.MatchFlag.MatchExactly)[0]
                    self.w.taskList.takeItem(self.w.taskList.row(item))
                except IndexError:
                    pass

                self.thread_task.pop(downloader.task_name)
                QMessageBox.information(self.w, "下载成功", f"{self.task_name}\n下载完成")
            else:
                QMessageBox.warning(self.w, "下载失败", f"'{self.task_name}'下载失败:\n{info[1]}")

        elif mode == Mode.IMPORT:
            downloader = args[1]
            res = args[2]
            if res[0]:
                info, self.current_choices, self.songids = res
                QMessageBox.information(self.w, "导入成功", info)
                self.w.musicImportListWidget.clear()
                self.w.musicImportListWidget.addItems(self.current_choices)
                self.w.mainStacked.setCurrentIndex(2)
            else:
                QMessageBox.warning(self.w, "导入失败", "导入失败，请输入歌单id或链接")

        elif mode == Mode.UPDATE:
            self.w.updateLabel.clear()
            self.w.updateBtn.setEnabled(True)
            res = args[1]
            if not res[0]:
                QMessageBox.warning(self.w, "更新", f"更新失败:\n{res[1]}")
                return
            QMessageBox.information(self.w, "更新", f"更新成功，新的文件在\n{res[1]}")
            self.w.updateCheckBtn.setEnabled(False)
            self.w.updateBtn.setEnabled(False)

    def search_music(self, name):
        thread = TaskExecuter(
            mode=Mode.SEARCH,
            downloader=self
        )
        self.current_music = name

        thread.task_finish.connect(self._task_finish)
        self.task_name = f"search - {self.current_music}"
        self.thread_task.update(
            {self.task_name: thread}
        )
        thread.start()

    def download_music(self, n, task_name, mode: Mode =None):
        self.task_name = task_name
        thread = TaskExecuter(
            mode=Mode.MUSIC,
            downloader=self,
            n=n
        )
        self.thread_task.update(
            {self.task_name: thread}
        )
        thread.task_finish.connect(self._task_finish)
        if mode == Mode.LYRIC:
            thread.finished.connect(self._lyric)
        else:
            thread.finished.connect(self._kill_task)
        thread.start()

    def download_lyric(self, task_name, n=None):
        if self.source == "酷狗音乐":
            self.task_name = task_name
            thread = TaskExecuter(
                mode=Mode.LYRIC,
                downloader=self,
                n=n
            )
            self.thread_task.update(
                {self.task_name: thread}
            )
            thread.task_finish.connect(self._task_finish)
            thread.finished.connect(self._kill_task)
            thread.start()
        else:
            for music in self.music:
                content = music.lyric.encode("utf-8")
                with open(fr"{self.music_path}/{task_name}.txt", "wb+") as f:
                    f.write(content)

    def import_music(self, info):
        thread = TaskExecuter(
            mode=Mode.IMPORT,
            downloader=self,
            info=info
        )
        self.task_name = info
        self.thread_task.update(
            {self.task_name: thread}
        )
        thread.task_finish.connect(self._task_finish)
        thread.finished.connect(self._kill_task)
        thread.start()

    def update(self, version):
        self.update_thread = TaskExecuter(
            mode=Mode.UPDATE,
            downloader=self,
            version=version
        )
        self.update_thread.start()
        self.update_thread.task_finish.connect(self._task_finish)

    def _lyric(self):
        self.download_lyric(self.task_name)
        self._kill_task()

    def _kill_task(self):
        self.thread_task.pop(self.task_name)
