# -*- coding: utf-8 -*-
import os
from random import choice
from re import sub, compile, findall
from concurrent.futures import ThreadPoolExecutor

from PySide6.QtWidgets import QListWidgetItem
from PySide6.QtCore import Signal, QObject
from httpx import Client, TimeoutException
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

ua_path = os.path.join(os.getcwd(), "source", "User-Agent.json")
with open(ua_path) as u:
    user_agent_json = load(u) 


def check_network(ua):
    if ua == "random":
        headers = {
            "User-Agent": get_user_agent()
        }
    else:
        headers = {
            "User-Agent": ua
        }
    with Client(headers=headers, follow_redirects=True, timeout=3, verify=False) as client:
        try:
            client.get("https://www.baidu.com")
        except TimeoutException:
            return False
        else:
            return True


def check_update(ua):
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


def update(version, ua):
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

    zip_path = os.path.join(os.getcwd(), f"BlackStone_Music_GUI_{version}.zip")
    with open(zip_path, "wb+") as f:
        f.write(resp.content)

    return True, zip_path


def reset_name(string):
    """剔除字符 /:*?"<>| Windows操作系统下文件或文件夹名字中不允许出现以上字符"""
    pattern = compile(r'[/:*?"<>|]')
    new_string = sub(pattern=pattern, repl="", string=string)

    return new_string


def get_user_agent():
    """获取随机UA"""
    user_agent = choice(choice(list(choice(user_agent_json).values())))
    return user_agent


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
        choose = [music_name, singers]

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


def kg_lyric_download(name, n, path, ua):
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

    with open(fr"{path}/{name}.txt", "wb+") as f:
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

        choose = [music_name, singers]

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
        choose = [music_name, singers]
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
                    os.remove(f"{path}/{song}-{singer}_{o}")

                k = guess(m)

            os.rename(f"{path}/{song}-{singer}", f"{path}/{song}-{singer}.{k.extension}")

        rgs = get_slice()
        with ThreadPoolExecutor(slice_num) as pool:
            for i in rgs.items():
                pool.submit(stream_download, i)

        combine()

    music = Music(song, singer=singer, lyric=None, music_url=music_url, image_url=image_url, source="QQ音乐")

    return True, music


def qq_import(info, ua):
    try:
        songlist_id = int(info)
    except ValueError:
        try:
            songlist_id = findall(r'/(\d+)', info)[0]
        except IndexError:
            return False

    if ua == "random":
        headers = {
            "User-Agent": get_user_agent()
        }
    else:
        headers = {
            "User-Agent": ua
        }

    url = f"https://c.y.qq.com/v8/fcg-bin/fcg_v8_playlist_cp.fcg?cv=10000&ct=19&newsong=1&tpl=wk&id={songlist_id}&g_tk=5381&platform=mac&g_tk_new_20200303=5381&loginUin=0&hostUin=0&format=json&inCharset=GB2312&outCharset=utf-8&notice=0&platform=jqspaframe.json&needNewCode=0"

    with Client(headers=headers, timeout=None) as client:
        resp = client.get(url=url)
        data = resp.json()["data"]["cdlist"][0]

    song_list = data["songlist"]
    tags = ""
    if data["tags"]:
        for i in data["tags"]:
            tags += f"{i} "

    return data, tags, [[i['name'], i['singer'][0]['name'], i["time_public"]] for i in song_list], data[
        "songids"].split(",")


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
        choose = [music_name, singers]

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

        choose = [music_name, singers]
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


class Music(object):
    def __init__(self, name, singer, lyric, music_url, image_url, source):
        self.name = name
        self.singer = singer
        self.lyric = lyric
        self.music_url = music_url
        self.image_url = image_url
        self.source = source


class Downloader(QObject):
    task_done = Signal(tuple)

    def __init__(self, configs):
        super().__init__()

        self.ua = configs["ua"]
        self.music_path = configs["music_path"]
        self.lyric_path = configs["lyric_path"]
        self.thread_num = configs["thread_num"]

        self.music_name = ""
        self.source = ""
        self.music: Music = None
        self.songids = []
        self.n: int = None
        self.task_id: QListWidgetItem = None
        self.version = ""
        self.info = ""

        self.music_search_sources = {
            "酷狗音乐": kg_get_music,
            "QQ音乐": vip_qq_get_music,
            "QQ音乐2": qq_get_music,
            "咪咕音乐": mg_get_music,
            "网易云音乐": wy_get_music
        }
        self.music_download_sources = {
            "酷狗音乐": kg_download,
            "QQ音乐": vip_qq_download,
            "QQ音乐2": qq_download,
            "咪咕音乐": mg_download,
            "网易云音乐": wy_download
        }
        self.music_import_sources = {
            "QQ音乐": qq_import,
        }
        self.lyric_download_sources = {
            "酷狗音乐": kg_lyric_download,
            
        }

    def search_music(self):
        get_music = self.music_search_sources[self.source]
        choice_list, songids = get_music(self.music_name, self.ua)
        self.task_done.emit((choice_list, songids))

    def download_music(self):
        download_music = self.music_download_sources[self.source]
        if self.source == "QQ音乐":
            res = download_music(
                br=2,
                path=self.music_path,
                songid=self.songids[self.n],
                ua=self.ua,
                slice_num=self.thread_num
            )
        else:
            res = download_music(
                name=self.music_name,
                n=self.n + 1,
                path=self.music_path,
                ua=self.ua
            )

        self.task_done.emit((res, self))

    def download_lyric(self, n, source):
        if source == "酷狗音乐":
            info = kg_lyric_download(
                name=self.music_name,
                n=n + 1,
                path=self.lyric_path,
                ua=self.ua
            )
            self.task_done.emit(info)
        else:
            content = self.music.lyric.encode("utf-8")
            with open(fr"{self.music_path}/{self.music_name}.txt", "wb+") as f:
                f.write(content)

    def import_music(self):
        import_songlist = self.music_import_sources[self.source]
        res = import_songlist(self.info, self.ua)
        self.task_done.emit(res)

    def checkUpdate(self):
        version, info = check_update(self.ua)
        self.version = version
        self.task_done.emit((version, info))

    def update(self):
        res = update(self.version, self.ua)
        self.task_done.emit(res)
