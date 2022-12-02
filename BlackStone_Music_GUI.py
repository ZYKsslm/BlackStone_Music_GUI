#!usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.messagebox as msgbox
import tkinter.filedialog as tkFile
from Work import work


window = tk.Tk()
sWidth = window.winfo_screenwidth()
sHeight = window.winfo_screenheight()
wSize = f"800x500+{int((sWidth - 800) / 2)}+{int((sHeight - 500) / 2)}"
window.geometry(wSize)
window.resizable(False, False)
window.iconbitmap(r".\Image\icon.ico")
window.title("Music_Download_Tool_GUI")
window.tk.call("source", r".\Azure-ttk-theme\azure.tcl")


# 读取设置
with open(r"Setting/config.ini", "r") as f:
    setting = f.readlines()

    wTheme = setting[0].rstrip()
    v = float(setting[1].rstrip())

    path = tk.StringVar()
    path.set(setting[2].rstrip())

    lyric_path = tk.StringVar()
    lyric_path.set(setting[3].rstrip())

    img_file = setting[4].rstrip()
    img_width = setting[5].rstrip()
    img_height = setting[6]


window.tk.call("set_theme", wTheme)
window.attributes("-alpha", v)

wallLb = tk.Label(master=window)
wallLb.pack()
img = ""
if img_file != "none":
    img = Image.open(img_file)
    img = ImageTk.PhotoImage(img)
    wallLb.config(image=img)

if img_width != "none" and img_height != "none":
    img_width = int(img_width)
    img_height = int(img_height)
    # 系统BUG，窗口高度要加20
    window.geometry(f"{img_width}x{img_height + 20}")


def save_setting():
    with open(r"Setting/config.ini", "w") as s:
        s.write(f"{wTheme}\n")
        s.write(f"{v}\n")
        s.write(f"{path.get()}\n")
        s.write(f"{lyric_path.get()}\n")
        s.write(f"{img_file}\n")
        s.write(f"{img_width}\n")
        s.write(f"{img_height}")


def light_theme():
    global wTheme
    wTheme = "light"
    if window.tk.call("ttk::style", "theme", "use") == "azure-light":
        return
    window.tk.call("set_theme", "light")


def dark_theme():
    global wTheme
    wTheme = "dark"
    if window.tk.call("ttk::style", "theme", "use") == "azure-dark":
        return
    window.tk.call("set_theme", "dark")


def vis():
    global visT
    visT = tk.Toplevel(master=window)
    visT.title("透明度设置")
    wWidth = window.winfo_screenwidth()
    wHeight = window.winfo_screenheight()
    rSize = f"250x200+{int((wWidth - 200) / 2)}+{int((wHeight - 200) / 2)}"
    visT.geometry(rSize)
    visT.attributes("-alpha", v)
    visT.resizable(False, False)
    visT.iconbitmap(r".\Image\icon.ico")

    visS = ttk.Scale(master=visT, from_=0.1, to=1, orient=tk.HORIZONTAL, length=200, command=change_vis)
    visS.place(x=30, y=80)


def change_vis(vf):
    global v
    window.attributes("-alpha", vf)
    visT.attributes("-alpha", vf)
    v = vf


def wallPaper():
    global img_file, img, img_width, img_height
    img_file = tkFile.askopenfilename(title="选择图片", filetypes=[("PNG", "*png"), ("JPG", "*jpg"), ("GIF", "*gif")])
    if not img_file:
        msgbox.showwarning(title="提示", message="您没有选择任何文件")
        return
    img = Image.open(img_file)
    img = ImageTk.PhotoImage(img)
    wallLb.config(image=img)
    img_width = "none"
    img_height = "none"


def wallAuto():
    global img_file, img, img_width, img_height
    img_file = tkFile.askopenfilename(title="选择图片", filetypes=[("PNG", "*png"), ("JPG", "*jpg"), ("GIF", "*gif")])
    if not img_file:
        msgbox.showwarning(title="提示", message="您没有选择任何文件")
        return
    img = Image.open(img_file)
    w, h = img.size

    f1 = 800.0 / w
    f2 = 500.0 / h
    factor = min(f1, f2)
    img_width = int(w * factor)
    img_height = int(h * factor)
    img_size = (img_width, img_height)
    wall_img = img.resize(img_size)

    wall_img.save(fr".\Image\wallpaper.{img.format}")
    img_file = fr".\Image\wallpaper.{img.format}"

    window.geometry(f"{img_width}x{img_height}")

    wall_img = ImageTk.PhotoImage(wall_img)
    wallLb.config(image=wall_img)


def sysPaper():
    global img_file, wTheme, v, img_width, img_height
    img_file = "none"
    wTheme = "dark"
    v = 0.9
    img_width = "none"
    img_height = "none"

    msgbox.showinfo(title="提示", message="设置成功")


def bye():
    rs = msgbox.askyesno(title="提示", message="确定退出吗?")
    if rs:
        save_setting()
        window.quit()
    else:
        return


def change_path():
    global path
    file = tkFile.askdirectory(title="选择文件夹")
    if not file:
        msgbox.showwarning(title="提示", message="您没有选择任何文件夹")
    else:
        path.set(file)
        msgbox.showinfo(title="提示", message="更改成功")


def change_lyric_path():
    global lyric_path
    file = tkFile.askdirectory(title="选择文件夹")
    if not file:
        msgbox.showwarning(title="提示", message="您没有选择任何文件夹")
    else:
        lyric_path.set(file)
        msgbox.showinfo(title="提示", message="更改成功")


def get_path():
    pathT = tk.Toplevel(master=window)
    pathT.title("路径设置")
    wWidth = window.winfo_screenwidth()
    wHeight = window.winfo_screenheight()
    rSize = f"300x160+{int((wWidth - 200) / 2)}+{int((wHeight - 100) / 2)}"
    pathT.geometry(rSize)
    pathT.iconbitmap(r".\Image\icon.ico")

    tk.Label(master=pathT, text="音乐路径：", font=("", 12)).place(x=0, y=0)
    tk.Label(master=pathT, text="歌词路径：", font=("", 12)).place(x=0, y=50)
    tk.Label(master=pathT, textvariable=path, font=("", 12)).place(x=80, y=0)
    tk.Label(master=pathT, textvariable=lyric_path, font=("", 12)).place(x=80, y=50)
    tk.Button(master=pathT, text="更改音乐保存路径", font=("", 13), command=change_path).place(x=0, y=100)
    tk.Button(master=pathT, text="更改歌词保存路径", font=("", 13), command=change_lyric_path).place(x=150, y=100)


music_name = ""


def en_search(self):
    search()


def search():
    global music_name

    if musicEn.get() == "":
        msgbox.showwarning(title="提示", message="请输入内容!")
        return

    if origin.get() == "酷狗音乐":
        downloadBtn.config(state=tk.NORMAL)
        dlLyricBtn.config(state=tk.DISABLED)
        music_name = musicEn.get()
        music_list = work.kg_get_music(music_name)
        info.set(music_list)

    elif origin.get() == "QQ音乐":
        downloadBtn.config(state=tk.NORMAL)
        dlLyricBtn.config(state=tk.DISABLED)
        music_name = musicEn.get()
        music_list = work.qq_get_music(music_name)
        info.set(music_list)

    elif origin.get() == "酷我音乐":
        downloadBtn.config(state=tk.NORMAL)
        dlLyricBtn.config(state=tk.DISABLED)
        music_name = musicEn.get()
        music_list = work.kw_get_music(music_name)
        info.set(music_list)

    elif origin.get() == "咪咕音乐":
        downloadBtn.config(state=tk.NORMAL)
        dlLyricBtn.config(state=tk.NORMAL)
        music_name = musicEn.get()
        music_list = work.mg_get_music(music_name)
        info.set(music_list)

    elif origin.get() == "网易云音乐":
        downloadBtn.config(state=tk.NORMAL)
        dlLyricBtn.config(state=tk.DISABLED)
        music_name = musicEn.get()
        music_list = work.wy_get_music(music_name)
        info.set(music_list)

    else:
        msgbox.showwarning(title="提示", message="您还未选择任何音源")
        return


lyric = ""


def download():
    global lyric
    try:
        n = infoListB.curselection()
    except tk._tkinter.TclError:
        msgbox.showwarning(title="提示", message="您还未选择任何音乐")
        return

    if origin.get() == "酷狗音乐":
        info_list = work.kg_download(music_name, n[0] + 1, path.get())
        song.set(info_list[0])
        singer.set(info_list[1])
        url.set(info_list[2])

        songT.delete("1.0", tk.END)
        singerT.delete("1.0", tk.END)
        urlT.delete("1.0", tk.END)

        songT.insert(tk.INSERT, song.get())
        singerT.insert(tk.INSERT, singer.get())
        urlT.insert(tk.INSERT, url.get())

        msgbox.showinfo(title="酷狗音乐", message=f"下载完成\n{song.get()}")

    elif origin.get() == "QQ音乐":
        info_list = work.qq_download(music_name, n[0] + 1, path.get())
        song.set(info_list[0])
        singer.set(info_list[1])
        url.set(info_list[2])

        songT.delete("1.0", tk.END)
        singerT.delete("1.0", tk.END)
        urlT.delete("1.0", tk.END)

        songT.insert(tk.INSERT, song.get())
        singerT.insert(tk.INSERT, singer.get())
        urlT.insert(tk.INSERT, url.get())

        msgbox.showinfo(title="QQ音乐", message=f"音乐下载完成\n{song.get()}")

    elif origin.get() == "咪咕音乐":
        info_list = work.mg_download(music_name, n[0] + 1, path.get())
        song.set(info_list[0])
        singer.set(info_list[1])
        lyric = info_list[2]

        songT.delete("1.0", tk.END)
        singerT.delete("1.0", tk.END)
        urlT.delete("1.0", tk.END)

        songT.insert(tk.INSERT, song.get())
        singerT.insert(tk.INSERT, singer.get())

        msgbox.showinfo(title="咪咕音乐", message=f"音乐下载完成\n{song.get()}")

    elif origin.get() == "网易云音乐":
        info_list = work.wy_download(music_name, n[0] + 1, path.get())
        song.set(info_list[0])
        singer.set(info_list[1])
        url.set(info_list[2])

        songT.delete("1.0", tk.END)
        singerT.delete("1.0", tk.END)
        urlT.delete("1.0", tk.END)

        songT.insert(tk.INSERT, song.get())
        singerT.insert(tk.INSERT, singer.get())
        urlT.insert(tk.INSERT, url.get())

        msgbox.showinfo(title="网易云音乐", message=f"音乐下载完成\n{song.get()}")

    else:
        info_list = work.kw_download(music_name, n[0] + 1, path.get())
        song.set(info_list[0])
        singer.set(info_list[1])

        songT.delete("1.0", tk.END)
        singerT.delete("1.0", tk.END)
        urlT.delete("1.0", tk.END)

        songT.insert(tk.INSERT, song.get())
        singerT.insert(tk.INSERT, singer.get())

        msgbox.showinfo(title="酷我音乐", message=f"下载完成\n{song.get()}")


def download_lyric():
    global lyric
    try:
        infoListB.get(infoListB.curselection())
    except tk._tkinter.TclError:
        msgbox.showwarning(title="提示", message="您还未选择任何音乐")
        return

    if origin.get() == "咪咕音乐":
        if lyric != "":
            work.mg_download_lyric(song.get(), singer.get(), lyric, lyric_path.get())
            msgbox.showinfo(title="咪咕音乐", message=f"歌词下载完成\n{song.get()}")
        else:
            n = infoListB.curselection()
            info_list = work.mg_download(music_name, n[0] + 1, path.get())
            song.set(info_list[0])
            singer.set(info_list[1])
            lyric = info_list[2]

            songT.delete("1.0", tk.END)
            singerT.delete("1.0", tk.END)
            urlT.delete("1.0", tk.END)

            songT.insert(tk.INSERT, song.get())
            singerT.insert(tk.INSERT, singer.get())

            work.mg_download_lyric(music_name, singer.get(), lyric, lyric_path.get())
            msgbox.showinfo(title="咪咕音乐", message=f"歌词下载完成\n{song.get()}")


# 顶级菜单栏
menu = tk.Menu(master=window)
optionMenu = tk.Menu(master=menu, tearoff=False)
aboutMenu = tk.Menu(master=menu, tearoff=False)
fileMenu = tk.Menu(master=menu, tearoff=False)
menu.add_cascade(label="设置", menu=optionMenu)
menu.add_cascade(label="文件", menu=fileMenu)
menu.add_cascade(label="关于", menu=aboutMenu)

# 关于
aboutMenu.add_command(
    label="说明", command=lambda: msgbox.showinfo(title="说明", message="作者:ZYK\nQQ:3119964735\n该软件仅供学习交流使用!"))
aboutMenu.add_command(label="版本", command=lambda: msgbox.showinfo(
    title="版本", message="版本:\nver 3.0\n兼容windows 8及以上的版本"))

# 设置:更换主题
themeMenu = tk.Menu(master=optionMenu, tearoff=False)
optionMenu.add_cascade(label="更换主题", menu=themeMenu)
theme = tk.Menu(master=themeMenu, tearoff=False)
themeMenu.add_cascade(label="Azure-ttk-theme", menu=theme)
theme.add_command(label="light", command=light_theme)
theme.add_command(label="dark(默认)", command=dark_theme)

# 更换背景
bgMenu = tk.Menu(master=optionMenu, tearoff=False)
optionMenu.add_cascade(label="更换背景", menu=bgMenu)
wallMenu = tk.Menu(master=bgMenu, tearoff=False)
bgMenu.add_cascade(label="选择背景图片", menu=wallMenu)
bgMenu.add_command(label="恢复默认（在下一次有效）", command=sysPaper)
wallMenu.add_command(label="图片自适应", command=wallAuto)
wallMenu.add_command(label="自动", command=wallPaper)

# 调节透明度
optionMenu.add_command(label="调节透明度", command=vis)

optionMenu.add_separator()

# 设置:退出
optionMenu.add_command(label="退出", command=bye)
window.config(menu=menu)

# 文件
fileMenu.add_command(label="路径设置", command=get_path)

tipLb = tk.Label(master=window, text="请输入歌名:", font=("", 13))
tipLb.place(x=50, y=25)

musicEn = ttk.Entry(master=window, font=("", 13))
musicEn.place(x=170, y=20, width=450, height=33)
musicEn.bind("<Return>", en_search)

tk.Button(master=window, text="搜索", font=("", 13), command=search).place(x=645, y=20, width=80, height=30)

origin = tk.StringVar()
origin.set("音源:未选择")
ttk.Radiobutton(master=window, text="酷狗音乐", variable=origin, value="酷狗音乐",
                command=lambda: modeLb.config(bg="#1E90FF", fg="white")).place(x=50, y=60)
ttk.Radiobutton(master=window, text="QQ音乐", variable=origin, value="QQ音乐",
                command=lambda: modeLb.config(bg="gold", fg="#3CB371")).place(x=150, y=60)
ttk.Radiobutton(master=window, text="酷我音乐", variable=origin, value="酷我音乐",
                command=lambda: modeLb.config(bg="gold", fg="#FF4500")).place(x=250, y=60)
ttk.Radiobutton(master=window, text="网易云音乐", variable=origin, value="网易云音乐",
                command=lambda: modeLb.config(bg="red", fg="white")).place(x=450, y=60)
ttk.Radiobutton(master=window, text="咪咕音乐", variable=origin, value="咪咕音乐",
                command=lambda: modeLb.config(bg="#FF1493", fg="white")).place(x=350, y=60)

ttk.Label(master=window, text="信息:", font=("", 13)).place(x=510, y=100)
ttk.Label(master=window, relief="sunken").place(x=510, y=135, width=250, height=320)
modeLb = tk.Label(master=window, textvariable=origin, font=("", 13))
modeLb.place(x=520, y=145)

ttk.Label(master=window, text="搜索结果:", font=("", 13)).place(x=50, y=100)
info = tk.StringVar()
infoListB = tk.Listbox(master=window, relief="groove", listvariable=info, font=("", 13))
infoListB.place(x=50, y=135, width=380, height=320)

yScroll = ttk.Scrollbar(master=infoListB, command=infoListB.yview)
yScroll.pack(side="right", fill=tk.Y)
xScroll = ttk.Scrollbar(master=infoListB, command=infoListB.xview, orient=tk.HORIZONTAL)
xScroll.pack(side="bottom", fill=tk.X)
infoListB.config(xscrollcommand=xScroll.set, yscrollcommand=yScroll.set)

song = tk.StringVar()
song.set("无歌名")
songT = tk.Text(master=window, font=("", 13))
songT.place(x=520, y=180, width=230, height=50)
songT.insert(tk.INSERT, song.get())

singer = tk.StringVar()
singer.set("无歌手")
singerT = tk.Text(master=window, font=("", 13))
singerT.place(x=520, y=250, width=230, height=60)
singerT.insert(tk.INSERT, singer.get())

url = tk.StringVar()
url.set("无链接")
urlT = tk.Text(master=window, font=("", 13))
urlT.place(x=520, y=330, width=230, height=65)
urlT.insert(tk.INSERT, url.get())

downloadBtn = tk.Button(master=window, state=tk.DISABLED, text="下\n载\n音\n乐", relief="groove", font=("", 13),
                        command=download)
downloadBtn.place(x=450, y=135, width=40, height=100)

dlLyricBtn = tk.Button(master=window, state=tk.DISABLED, text="下\n载\n歌\n词", relief="groove", font=("", 13),
                       command=download_lyric)
dlLyricBtn.place(x=450, y=255, width=40, height=100)

window.protocol("WM_DELETE_WINDOW", bye)
window.mainloop()
