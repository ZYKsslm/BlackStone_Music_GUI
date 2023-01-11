# -*- coding: utf-8 -*-
from requests import get
from re import sub
from filetype import guess

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"
}

kw_api = "http://ovooa.com/API/kwdg/api.php"
kg_api = "http://ovooa.com/API/kgdg/api.php"
mg_api = "http://ovooa.com/API/migu/api.php"
qq_vip_api = "http://ovooa.com/API/QQ_Music"
qq_api = "http://ovooa.com/API/qqdg/api.php"
wy_api = "http://ovooa.com/API/wydg/api.php"


# 酷我音乐
def kw_get_music(name):

    data = {
        "msg": name,
    }
    resp = get(url=kw_api, headers=headers, params=data)
    music_info = resp.json()["data"]
    resp.close()

    choice_list = []
    for i in music_info:
        music_name = i["song"]
        singers = i["singer"]

        choice = f"{music_name}-{singers}"
        choice_list.append(choice)

    return choice_list


def kw_download(name, n, path):

    data = {
        "msg": name,
        "n": n,
    }
    resp = get(url=kw_api, headers=headers, params=data)
    music_info = resp.json()["data"]
    resp.close()

    song = sub(r'[\\/:*?"<>|]', "", music_info["musicname"])
    singer = sub(r'[\\/:*?"<>|]', "", music_info["singer"])
    try:
        music = music_info["musicurl"]
    except KeyError:
        return False

    resp = get(url=music, headers=headers)
    content = resp.content
    resp.close()

    kind = guess(content)
    if kind is None:
        return False

    with open(fr"{path}/{song}-{singer}.{kind.extension}", "wb+") as f:
        f.write(content)

    return [song, singer]


# 酷狗音乐
def kg_get_music(name):

    data = {
        "msg": name,
    }
    resp = get(url=kg_api, headers=headers, params=data)
    music_info = resp.json()["data"]
    resp.close()

    choice_list = []
    for i in music_info:
        music_name = i["name"]
        singers = i["singer"]

        choice = f"{music_name}-{singers}"
        choice_list.append(choice)

    return choice_list


def kg_download(name, n, path):

    data = {
        "msg": name,
        "n": n,
    }
    resp = get(url=kg_api, headers=headers, params=data)
    music_info = resp.json()["data"]
    resp.close()

    song = sub(r'[\\/:*?"<>|]', "", music_info["song"])
    singer = sub(r'[\\/:*?"<>|]', "", music_info["singer"])
    music = music_info["url"]
    try:
        music_url = music_info["Music_Url"]
    except KeyError:
        return False

    resp = get(url=music, headers=headers)
    content = resp.content
    resp.close()

    kind = guess(content)
    if kind is None:
        return False

    with open(fr"{path}/{song}-{singer}.{kind.extension}", "wb+") as f:
        f.write(content)

    return [song, singer, music_url]


# 咪咕音乐
def mg_get_music(name):

    data = {
        "msg": name,
    }
    resp = get(url=mg_api, headers=headers, params=data)
    music_info = resp.json()["data"]
    resp.close()
    choice_list = []
    for i in music_info:
        music_name = i["song"]
        singers = i["singer"]

        choice = f"{music_name}-{singers}"
        choice_list.append(choice)

    return choice_list


def mg_download(name, n, path, get_lyric=False):

    data = {
        "msg": name,
        "n": n,
    }
    resp = get(url=mg_api, headers=headers, params=data)
    music_info = resp.json()["data"]
    resp.close()

    song = sub(r'[\\/:*?"<>|]', "", music_info["musicname"])
    singer = sub(r'[\\/:*?"<>|]', "", music_info["singer"])
    try:
        music = music_info["musicurl"]
        lyric = music_info["lyric"]
    except KeyError:
        return False

    resp = get(url=music, headers=headers)
    content = resp.content
    resp.close()

    if get_lyric is False:
        kind = guess(content)
        if kind is None:
            return False

        with open(fr"{path}/{song}-{singer}.{kind.extension}", "wb+") as f:
            f.write(content)

        return [song, singer, lyric]
    else:
        return


def mg_download_lyric(song, singer, lyric, lyric_path):
    with open(fr"{lyric_path}/{song}-{singer}.txt", "w+", encoding="utf-8") as f:
        f.write(lyric)


# QQ音乐VIP
def vip_qq_get_music(name):
    data = {
        "msg": name,
        "limit": 50
    }
    resp = get(url=qq_vip_api, headers=headers, params=data)
    music_info = resp.json()["data"]
    resp.close()

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
                    singers += f"{singer_list[s-1]}"
                else:
                    singers += f"{singer_list[s-1]}、"
        else:
            singers = singer_list[0]
        choice = f"{music_name}-{singers}"
        choice_list.append(choice)

    return choice_list


def vip_qq_download(name, n, path):
    data = {
        "msg": name,
        "n": n
    }
    resp = get(url=qq_vip_api, headers=headers, params=data)
    info = resp.json()
    resp.close()
    try:
        music_info = info["data"]
    except KeyError:
        return False

    song = sub(r'[\\/:*?"<>|]', "", music_info["song"])
    music_url = music_info["url"]
    singer = sub(r'[\\/:*?"<>|]', "", music_info["singer"])
    music = music_info["music"]

    resp = get(url=music, headers=headers)
    content = resp.content
    resp.close()

    kind = guess(content)
    if kind is None:
        return False

    with open(fr"{path}/{song}-{singer}.{kind.extension}", "wb+") as f:
        f.write(content)

    return [song, singer, music_url]


# QQ音乐
def qq_get_music(name):
    data = {
        "msg": name,
        "sc": 50
    }
    resp = get(url=qq_api, headers=headers, params=data)
    music_info = resp.json()["data"]
    resp.close()

    choice_list = []
    for i in music_info:
        music_name = i["song"]
        singers = i["singers"]
        choice = f"{music_name}-{singers}"
        choice_list.append(choice)

    return choice_list


def qq_download(name, n, path, get_lyric=False):
    data = {
        "msg": name,
        "n": n
    }
    resp = get(url=qq_api, headers=headers, params=data)
    info = resp.json()
    resp.close()
    try:
        music_info = info["data"]
    except KeyError:
        return False

    song = sub(r'[\\/:*?"<>|]', "", music_info["Music"])
    music_url = music_info["Music_Url"]
    singer = sub(r'[\\/:*?"<>|]', "", music_info["Singer"])
    lyric = music_info["lyric"]
    music = music_info["Url"]

    resp = get(url=music, headers=headers)
    content = resp.content
    resp.close()

    if get_lyric is False:
        kind = guess(content)
        if kind is None:
            return False

        with open(fr"{path}/{song}-{singer}.{kind.extension}", "wb+") as f:
            f.write(content)

        return [song, singer, music_url, lyric]
    else:
        return


def qq_download_lyric(song, singer, lyric, lyric_path):
    with open(fr"{lyric_path}/{song}-{singer}.txt", "w+", encoding="utf-8") as f:
        f.write(lyric)


# 网易云音乐
def wy_get_music(name):

    data = {
        "msg": name,
    }
    resp = get(url=wy_api, headers=headers, params=data)
    music_info = resp.json()["data"]
    resp.close()

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
        choice = f"{music_name}-{singers}"
        choice_list.append(choice)

    return choice_list


def wy_download(name, n, path):

    data = {
        "msg": name,
        "n": n,
    }
    resp = get(url=wy_api, headers=headers, params=data)
    music_info = resp.json()["data"]
    resp.close()

    song = sub(r'[\\/:*?"<>|]', "", music_info["Music"])
    singer = sub(r'[\\/:*?"<>|]', "", music_info["Singer"])
    try:
        music = music_info["dataUrl"]
        music_url = music_info["Url"]
    except KeyError:
        return False

    resp = get(url=music, headers=headers)
    content = resp.content
    resp.close()

    kind = guess(content)
    if kind is None:
        return False

    with open(fr"{path}/{song}-{singer}.{kind.extension}", "wb+") as f:
        f.write(content)

    return [song, singer, music_url]