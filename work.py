# -*- coding: utf-8 -*-
from requests import get
from re import sub

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"
}

kw_api = "http://ovooa.com/API/kwdg/api.php"
kg_api = "http://ovooa.com/API/kgdg/api.php"
mg_api = "http://ovooa.com/API/migu/api.php"
qq_api = "http://ovooa.com/API/QQ_Music"
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
    music = music_info["musicurl"]

    resp = get(url=music, headers=headers)
    content = resp.content
    resp.close()

    with open(fr"{path}\{song}-{singer}.mp3", "wb+") as f:
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
    music_url = music_info["Music_Url"]

    resp = get(url=music, headers=headers)
    content = resp.content
    resp.close()

    with open(fr"{path}\{song}-{singer}.mp3", "wb+") as f:
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


def mg_download(name, n, path):

    data = {
        "msg": name,
        "n": n,
    }
    resp = get(url=mg_api, headers=headers, params=data)
    music_info = resp.json()["data"]
    resp.close()

    song = sub(r'[\\/:*?"<>|]', "", music_info["musicname"])
    singer = sub(r'[\\/:*?"<>|]', "", music_info["singer"])
    music = music_info["musicurl"]
    lyric = music_info["lyric"]

    resp = get(url=music, headers=headers)
    content = resp.content
    resp.close()

    with open(fr"{path}\{song}-{singer}.mp3", "wb+") as f:
        f.write(content)

    return [song, singer, lyric]


def mg_download_lyric(song, singer, lyric, lyric_path):
    with open(fr"{lyric_path}\{song}-{singer}.txt", "w+", encoding="utf-8") as f:
        f.write(lyric)


# QQ音乐
def qq_get_music(name):
    data = {
        "msg": name,
    }
    resp = get(url=qq_api, headers=headers, params=data)
    music_info = resp.json()["data"]
    resp.close()

    choice_list = []
    for i in music_info:
        music_name = i["song"]
        singers = i["singers"][0]
        choice = f"{music_name}-{singers}"
        choice_list.append(choice)

    return choice_list


def qq_download(name, n, path):
    data = {
        "msg": name,
        "n": n
    }
    resp = get(url=qq_api, headers=headers, params=data)
    info = resp.json()
    music_info = info["data"]
    resp.close()

    song = sub(r'[\\/:*?"<>|]', "", music_info["song"])
    music_url = music_info["url"]
    singer = sub(r'[\\/:*?"<>|]', "", music_info["singer"])
    music = music_info["music"]

    resp = get(url=music, headers=headers)
    content = resp.content
    resp.close()

    with open(fr"{path}\{song}-{singer}.m4a", "wb+") as f:
        f.write(content)

    return [song, singer, music_url]


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
        singers = i["singers"]

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
    music = music_info["dataUrl"]
    music_url = music_info["Url"]

    resp = get(url=music, headers=headers)
    content = resp.content
    resp.close()

    with open(fr"{path}\{song}-{singer}.mp3", "wb+") as f:
        f.write(content)

    return [song, singer, music_url]