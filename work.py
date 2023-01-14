# -*- coding: utf-8 -*-
from httpx import Client, stream
from os import rename
from random import choice
from re import sub, compile
from filetype import guess

try:
    from ujson import load, dump
except ModuleNotFoundError:
    from json import load, dump

kw_api = "http://ovooa.com/API/kwdg/api.php"
kg_api = "http://ovooa.com/API/kgdg/api.php"
mg_api = "http://ovooa.com/API/migu/api.php"
qq_vip_api = "http://ovooa.com/API/QQ_Music"
qq_api = "http://ovooa.com/API/qqdg/api.php"
wy_api = "http://ovooa.com/API/wydg/api.php"

with open("User-Agent.json") as u:
    user_agent_json = load(u)


def set_name(string):
    """剔除字符 /:*?"<>| Windows操作系统下文件或文件夹名字中不允许出现以上字符"""
    pattern = compile(r'[/:*?"<>|]')
    new_string = sub(pattern=pattern, repl="", string=string)

    return new_string


def get_user_agent():
    """获取随机UA"""
    user_agent = choice(choice(list(choice(user_agent_json).values())))
    return user_agent


# 酷我音乐
def kw_get_music(name):
    headers = {
        "User-Agent": get_user_agent()
    }

    data = {
        "msg": name,
        "sc": 50
    }

    with Client(headers=headers, params=data, follow_redirects=True, timeout=None) as client:
        resp = client.get(url=kw_api)
        music_info = resp.json()["data"]

    choice_list = []
    for i in music_info:
        music_name = i["song"]
        singers = i["singer"]

        choose = f"{music_name}-{singers}"
        choice_list.append(choose)

    return choice_list


def kw_download(name, n, path):
    headers = {
        "User-Agent": get_user_agent()
    }

    data = {
        "msg": name,
        "n": n,
    }

    with Client(headers=headers, params=data, follow_redirects=True, timeout=None) as client:
        resp = client.get(url=kw_api)
        music_info = resp.json()["data"]

    song = set_name(music_info["musicname"])
    singer = set_name(music_info["singer"])

    try:
        music = music_info["musicurl"]
    except KeyError:
        return False

    with Client(headers=headers, follow_redirects=True, timeout=None) as client:
        resp = client.get(url=music)
        content = resp.content

    kind = guess(content)
    if kind is None:
        return False

    with open(fr"{path}/{song}-{singer}.{kind.extension}", "wb+") as f:
        f.write(content)

    return [song, singer]


# 酷狗音乐
def kg_get_music(name):
    headers = {
        "User-Agent": get_user_agent()
    }

    data = {
        "msg": name,
        "sc": 50
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

    return choice_list


def kg_download(name, n, path):
    headers = {
        "User-Agent": get_user_agent()
    }

    data = {
        "msg": name,
        "n": n,
    }

    with Client(headers=headers, params=data, follow_redirects=True, timeout=None) as client:
        resp = client.get(url=kg_api)
        try:
            music_info = resp.json()["data"]
        except KeyError:
            return False

    song = set_name(music_info["song"])
    singer = set_name(music_info["singer"])
    music_url = music_info["Music_Url"]
    try:
        music = music_info["url"]
    except KeyError:
        return False

    with Client(headers=headers, follow_redirects=True, timeout=None) as client:
        resp = client.get(url=music)
        content = resp.content

    kind = guess(content)
    if kind is None:
        return False

    with open(fr"{path}/{song}-{singer}.{kind.extension}", "wb+") as f:
        f.write(content)

    return [song, singer, music_url]


# 咪咕音乐
def mg_get_music(name):
    headers = {
        "User-Agent": get_user_agent()
    }

    data = {
        "msg": name,
        "sc": 50
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

    return choice_list


def mg_download(name, n, path, get_lyric=False, lyric_path=None):
    headers = {
        "User-Agent": get_user_agent()
    }

    data = {
        "msg": name,
        "n": n,
    }

    with Client(headers=headers, params=data, follow_redirects=True, timeout=None) as client:
        resp = client.get(url=mg_api)
        music_info = resp.json()["data"]

    song = set_name(music_info["musicname"])
    singer = set_name(music_info["singer"])
    lyric = music_info["lyric"]
    try:
        music = music_info["musicurl"]
    except KeyError:
        return False

    with Client(headers=headers, follow_redirects=True, timeout=None) as client:
        resp = client.get(url=music)
        content = resp.content

    kind = guess(content)
    if kind is None:
        return False

    with open(fr"{path}/{song}-{singer}.{kind.extension}", "wb+") as f:
        f.write(content)

    if get_lyric is True:
        with open(fr"{lyric_path}/{song}-{singer}.txt", "w+", encoding="utf-8") as f:
            f.write(lyric)

    return [song, singer]


# QQ音乐VIP
def vip_qq_get_music(name):
    headers = {
        "User-Agent": get_user_agent()
    }

    data = {
        "msg": name,
        "limit": 50
    }

    with Client(headers=headers, params=data, follow_redirects=True, timeout=None) as client:
        resp = client.get(url=qq_vip_api)
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

    return choice_list


def vip_qq_download(name, n, br, path):
    headers = {
        "User-Agent": get_user_agent()
    }

    data = {
        "msg": name,
        "n": n,
        "br": br
    }

    with Client(headers=headers, params=data, follow_redirects=True, timeout=None) as client:
        resp = client.get(url=qq_vip_api)
        info = resp.json()
    try:
        music_info = info["data"]
    except KeyError:
        return False

    song = set_name(music_info["song"])
    singer = set_name(music_info["singer"])
    music_url = music_info["url"]
    music = music_info["music"]

    if br > 2:
        with Client(headers=headers, follow_redirects=True, timeout=None) as client:
            resp = client.get(url=music)
            content = resp.content

        kind = guess(content)
        if kind is None:
            return False

        with open(fr"{path}/{song}-{singer}.{kind.extension}", "wb+") as f:
            f.write(content)
    else:
        with Client(headers=headers, follow_redirects=True, timeout=None) as client:
            total = client.head(url=music).headers["Content-Length"]
        with stream(method="GET", url=music, headers=headers, follow_redirects=True, timeout=None) as r:
            with open(fr"{path}/{song}-{singer}", "wb+") as f:
                for data in r.iter_bytes(chunk_size=64*1024):
                    f.write(data)

                kind = guess(f)

        rename(fr"{path}/{song}-{singer}", fr"{path}/{song}-{singer}.{kind.extension}")

    return [song, singer, music_url]


# QQ音乐
def qq_get_music(name):
    headers = {
        "User-Agent": get_user_agent()
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

    return choice_list


def qq_download(name, n, path, get_lyric=False, lyric_path=None):
    headers = {
        "User-Agent": get_user_agent()
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
        return False

    song = set_name(music_info["Music"])
    music_url = music_info["Music_Url"]
    singer = set_name(music_info["Singer"])
    lyric = music_info["lyric"]
    music = music_info["Url"]

    with Client(headers=headers, follow_redirects=True, timeout=None) as client:
        resp = client.get(url=music)
        content = resp.content

    kind = guess(content)
    if kind is None:
        return False

    with open(fr"{path}/{song}-{singer}.{kind.extension}", "wb+") as f:
        f.write(content)

    if get_lyric is True:
        with open(fr"{lyric_path}/{song}-{singer}.txt", "w+", encoding="utf-8") as f:
            f.write(lyric)

    return [song, singer, music_url]


# 网易云音乐
def wy_get_music(name):
    headers = {
        "User-Agent": get_user_agent()
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

    return choice_list


def wy_download(name, n, path):
    headers = {
        "User-Agent": get_user_agent()
    }

    data = {
        "msg": name,
        "n": n,
    }

    with Client(headers=headers, params=data, follow_redirects=True, timeout=None) as client:
        resp = client.get(url=wy_api)
        music_info = resp.json()["data"]

    song = sub(r'[\\/:*?"<>|]', "", music_info["Music"])
    singer = sub(r'[\\/:*?"<>|]', "", music_info["Singer"])
    try:
        music = music_info["dataUrl"]
        music_url = music_info["Url"]
    except KeyError:
        return False

    with Client(headers=headers, follow_redirects=True, timeout=None) as client:
        resp = client.get(url=music)
        content = resp.content

    kind = guess(content)
    if kind is None:
        return False

    with open(fr"{path}/{song}-{singer}.{kind.extension}", "wb+") as f:
        f.write(content)

    return [song, singer, music_url]
