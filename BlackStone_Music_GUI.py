# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.messagebox as msgbox
import tkinter.filedialog as tkFile
import json
from os import execl
from sys import executable, argv
import work

window = tk.Tk()
sWidth = window.winfo_screenwidth()
sHeight = window.winfo_screenheight()
# 让主窗口处于屏幕中间
wSize = f"800x600+{int((sWidth - 800) / 2)}+{int((sHeight - 600) / 2)}"
window.geometry(wSize)
window.resizable(False, False)
window.iconbitmap(r"Image/icon.ico")
window.title("BlackStone_Music_GUI")
# 美化脚本
window.tk.call("source", r"Azure-ttk-theme/azure.tcl")

# 读取设置
with open(r"config.json", "r") as f:
    setting = json.load(f)

    wTheme = setting["wTheme"]
    v = setting["v"]

    path = tk.StringVar()
    path.set(setting["path"])

    lyric_path = tk.StringVar()
    lyric_path.set(setting["lyric_path"])

    img_file = setting["img_file"]

# 设置主窗体样式
window.tk.call("set_theme", wTheme)
# 透明度
window.attributes("-alpha", v)

# 壁纸
wallLb = ttk.Label(master=window)
wallLb.pack()
if img_file is not None:
    img = Image.open(img_file)
    img = ImageTk.PhotoImage(img)
    wallLb.config(image=img)


# 自动保存设置
def save_setting():
    with open(r"config.json", "w") as s:
        config = {
            "wTheme": wTheme,
            "v": v,
            "path": path.get(),
            "lyric_path": lyric_path.get(),
            "img_file": img_file,
        }

        json.dump(config, s)


def light_theme():
    global wTheme
    wTheme = "light"
    if window.tk.call("ttk::style", "theme", "use") == "azure-light":
        return
    else:
        window.tk.call("set_theme", "light")


def dark_theme():
    global wTheme
    wTheme = "dark"
    if window.tk.call("ttk::style", "theme", "use") == "azure-dark":
        return
    else:
        window.tk.call("set_theme", "dark")


def vis():
    # 窗口设置
    visT = tk.Toplevel(master=window)
    visT.title("透明度设置")
    vWidth = window.winfo_screenwidth()
    vHeight = window.winfo_screenheight()
    vSize = f"250x200+{int((vWidth - 250) / 2)}+{int((vHeight - 200) / 2)}"
    visT.geometry(vSize)
    visT.attributes("-alpha", v)
    visT.resizable(False, False)
    visT.iconbitmap(r".\Image\icon.ico")

    def change_vis(vf):
        global v
        window.attributes("-alpha", vf)
        visT.attributes("-alpha", vf)
        v = vf

    visS = ttk.Scale(master=visT, from_=0.1, to=1, orient=tk.HORIZONTAL, length=200, command=change_vis)
    visS.place(x=30, y=80)


def wallpaper():
    global img_file, img
    img_file = tkFile.askopenfilename(title="选择图片", filetypes=[("PNG", "*png"), ("JPG", "*jpg"), ("GIF", "*gif")])
    if not img_file:
        msgbox.showwarning(title="提示", message="您没有选择任何文件")
        return
    img = Image.open(img_file)
    suffix = img.format

    if img.size[0]/img.size[1] == 4/3:
        img = img.resize((800, 600))
        img_file = f'Image/wallpaper.{suffix}'

    img.save(f'Image/wallpaper.{suffix}')
    img = ImageTk.PhotoImage(img)
    wallLb.config(image=img)


def default():
    global img_file, wTheme, v
    v = 0.9
    wTheme = "dark"
    img_file = None
    save_setting()
    # 重启程序
    execl(executable, executable, *argv)


def bye():
    rs = msgbox.askyesnocancel(title="提示", message="确定退出吗?\n点击“是”以退出，点击“否”以最小化窗口")
    if rs is True:
        save_setting()
        window.quit()
    elif rs is False:
        window.iconify()


def get_path():
    pathT = tk.Toplevel(master=window)
    pathT.title("路径设置")
    wWidth = window.winfo_screenwidth()
    wHeight = window.winfo_screenheight()
    rSize = f"300x160+{int((wWidth - 200) / 2)}+{int((wHeight - 100) / 2)}"
    pathT.geometry(rSize)
    pathT.iconbitmap(r".\Image\icon.ico")

    def change_path():
        global path
        file = tkFile.askdirectory(title="选择文件夹")
        if not file:
            msgbox.showwarning(title="提示", message="您没有选择任何文件夹", parent=pathT)
        else:
            path.set(file)
            msgbox.showinfo(title="提示", message="更改成功")

    def change_lyric_path():
        global lyric_path
        file = tkFile.askdirectory(title="选择文件夹")
        if not file:
            msgbox.showwarning(title="提示", message="您没有选择任何文件夹", parent=pathT)
        else:
            lyric_path.set(file)
            msgbox.showinfo(title="提示", message="更改成功")

    tk.Label(master=pathT, text="音乐路径：", font=("", 12)).place(x=0, y=0)
    tk.Label(master=pathT, text="歌词路径：", font=("", 12)).place(x=0, y=50)
    tk.Label(master=pathT, textvariable=path, font=("", 12)).place(x=80, y=0)
    tk.Label(master=pathT, textvariable=lyric_path, font=("", 12)).place(x=80, y=50)
    tk.Button(master=pathT, text="更改音乐保存路径", font=("", 13), command=change_path).place(x=0, y=100)
    tk.Button(master=pathT, text="更改歌词保存路径", font=("", 13), command=change_lyric_path).place(x=150, y=100)


# 回车以搜索
def en_search(self):
    search()


music_name = None


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


lyric = None


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
    label="说明", command=lambda: msgbox.showinfo(title="说明", message="作者:ZYKsslm\nQQ:3119964735\n该软件仅供学习交流使用!"))
aboutMenu.add_command(label="版本", command=lambda: msgbox.showinfo(
    title="版本", message="ver 0.1.3-GUI\n需要兼容python>=3.10"))

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
bgMenu.add_command(label="选择背景图片（建议尺寸4比3）", command=wallpaper)
bgMenu.add_command(label="恢复默认", command=default)

# 调节透明度
optionMenu.add_command(label="调节透明度", command=vis)

optionMenu.add_separator()

# 设置:退出
optionMenu.add_command(label="退出", command=bye)
window.config(menu=menu)

# 文件
fileMenu.add_command(label="路径设置", command=get_path)

tipLb = ttk.Label(master=window, text="请输入歌名:", font=("", 13))
tipLb.place(x=50, y=45)

musicEn = ttk.Entry(master=window, font=("", 13))
musicEn.place(x=170, y=40, width=450, height=33)
musicEn.bind("<Return>", en_search)

tk.Button(master=window, text="搜索", font=("", 13), command=search).place(x=645, y=40, width=80, height=30)

origin = tk.StringVar()
origin.set("音源:未选择")
ttk.Radiobutton(master=window, text="酷狗音乐", variable=origin, value="酷狗音乐",
                command=lambda: modeLb.configure(background="#1E90FF", foreground="white")).place(x=50, y=88)
ttk.Radiobutton(master=window, text="QQ音乐", variable=origin, value="QQ音乐",
                command=lambda: modeLb.configure(background="gold", foreground="#3CB371")).place(x=150, y=88)
ttk.Radiobutton(master=window, text="酷我音乐", variable=origin, value="酷我音乐",
                command=lambda: modeLb.configure(background="gold", foreground="#FF4500")).place(x=250, y=88)
ttk.Radiobutton(master=window, text="网易云音乐", variable=origin, value="网易云音乐",
                command=lambda: modeLb.configure(background="red", foreground="white")).place(x=450, y=88)
ttk.Radiobutton(master=window, text="咪咕音乐", variable=origin, value="咪咕音乐",
                command=lambda: modeLb.configure(background="#FF1493", foreground="white")).place(x=350, y=88)

ttk.Label(master=window, text="信息:", font=("", 13)).place(x=510, y=135)
ttk.Label(master=window, relief="sunken").place(x=510, y=177, width=250, height=320)
modeLb = ttk.Label(master=window, textvariable=origin, font=("", 13))
modeLb.place(x=520, y=190)

ttk.Label(master=window, text="搜索结果:", font=("", 13)).place(x=50, y=135)
info = tk.StringVar()
infoListB = tk.Listbox(master=window, relief="groove", listvariable=info, font=("", 13))
infoListB.place(x=50, y=177, width=380, height=320)

yScroll = ttk.Scrollbar(master=infoListB, command=infoListB.yview)
yScroll.pack(side="right", fill=tk.Y)
xScroll = ttk.Scrollbar(master=infoListB, command=infoListB.xview, orient=tk.HORIZONTAL)
xScroll.pack(side="bottom", fill=tk.X)
infoListB.config(xscrollcommand=xScroll.set, yscrollcommand=yScroll.set)

song = tk.StringVar()
song.set("无歌名")
songT = tk.Text(master=window, font=("", 13))
songT.place(x=520, y=230, width=230, height=50)
songT.insert(tk.INSERT, song.get())

singer = tk.StringVar()
singer.set("无歌手")
singerT = tk.Text(master=window, font=("", 13))
singerT.place(x=520, y=315, width=230, height=60)
singerT.insert(tk.INSERT, singer.get())

url = tk.StringVar()
url.set("无链接")
urlT = tk.Text(master=window, font=("", 13))
urlT.place(x=520, y=410, width=230, height=65)
urlT.insert(tk.INSERT, url.get())

downloadBtn = tk.Button(master=window, state=tk.DISABLED, text="下\n载\n音\n乐", relief="groove", font=("", 13),
                        command=download)
downloadBtn.place(x=450, y=177, width=40, height=100)

dlLyricBtn = tk.Button(master=window, state=tk.DISABLED, text="下\n载\n歌\n词", relief="groove", font=("", 13),
                       command=download_lyric)
dlLyricBtn.place(x=450, y=310, width=40, height=100)

window.protocol("WM_DELETE_WINDOW", bye)
window.mainloop()
