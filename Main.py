import os
import sys
from tkinter import *
from tkinter import filedialog
from tkinter.font import Font
import pytube.exceptions
from pytube import YouTube


def resource_path(relative_path):
    global base_path
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("Assets\\Images")

    return os.path.join(base_path, relative_path)


root = Tk()
root.title("PyTuber")
root.minsize(width=450, height=650)
root.maxsize(width=450, height=650)
root.iconbitmap(resource_path("YouTube.ico"))


def youtube_screen():
    global bg
    global button_choose_path
    global button_download
    global button_144p
    global button_240p
    global button_360p
    global button_480p
    global button_720p
    global button_youtube

    bg = PhotoImage(file=resource_path("youtube_screen.png"))
    bg_label = Label(image=bg)
    bg_label.place(x=-6, y=-2)

    default_font = Font(family="MV Boli", size=17)

    def res_getter(resolution):
        global resolution_value
        global button_144p
        global button_240p
        global button_360p
        global button_480p
        global button_720p

        resolution_value = resolution

        if resolution == "144p":
            button_144p = PhotoImage(file=resource_path("selected_144p_button.png"))
            button_144p_label = Label(image=button_144p, borderwidth=0)
            button_144p_label.place(x=30, y=385)
            real_button_144p = Button(root, image=button_144p, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                                      command=lambda: res_getter("144p"))
            real_button_144p.place(x=30, y=385)

            button_240p = PhotoImage(file=resource_path("240p_button.png"))
            button_240p_label = Label(image=button_240p, borderwidth=0)
            button_240p_label.place(x=110, y=385)
            real_button_240p = Button(root, image=button_240p, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                                      command=lambda: res_getter("240p"))
            real_button_240p.place(x=110, y=385)

            button_360p = PhotoImage(file=resource_path("360p_button.png"))
            button_360p_label = Label(image=button_360p, borderwidth=0)
            button_360p_label.place(x=190, y=385)
            real_button_360p = Button(root, image=button_360p, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                                      command=lambda: res_getter("360p"))
            real_button_360p.place(x=190, y=385)

            button_480p = PhotoImage(file=resource_path("480p_button.png"))
            button_480p_label = Label(image=button_480p, borderwidth=0)
            button_480p_label.place(x=270, y=385)
            real_button_480p = Button(root, image=button_480p, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                                      command=lambda: res_getter("480p"))
            real_button_480p.place(x=270, y=385)

            button_720p = PhotoImage(file=resource_path("720p_button.png"))
            button_720p_label = Label(image=button_720p, borderwidth=0)
            button_720p_label.place(x=350, y=385)
            real_button_720p = Button(root, image=button_720p, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                                      command=lambda: res_getter("720p"))
            real_button_720p.place(x=350, y=385)

        if resolution == "240p":
            button_144p = PhotoImage(file=resource_path("144p_button.png"))
            button_144p_label = Label(image=button_144p, borderwidth=0)
            button_144p_label.place(x=30, y=385)
            real_button_144p = Button(root, image=button_144p, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                                      command=lambda: res_getter("144p"))
            real_button_144p.place(x=30, y=385)

            button_240p = PhotoImage(file=resource_path("selected_240p_button.png"))
            button_240p_label = Label(image=button_240p, borderwidth=0)
            button_240p_label.place(x=110, y=385)
            real_button_240p = Button(root, image=button_240p, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                                      command=lambda: res_getter("240p"))
            real_button_240p.place(x=110, y=385)

            button_360p = PhotoImage(file=resource_path("360p_button.png"))
            button_360p_label = Label(image=button_360p, borderwidth=0)
            button_360p_label.place(x=190, y=385)
            real_button_360p = Button(root, image=button_360p, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                                      command=lambda: res_getter("360p"))
            real_button_360p.place(x=190, y=385)

            button_480p = PhotoImage(file=resource_path("480p_button.png"))
            button_480p_label = Label(image=button_480p, borderwidth=0)
            button_480p_label.place(x=270, y=385)
            real_button_480p = Button(root, image=button_480p, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                                      command=lambda: res_getter("480p"))
            real_button_480p.place(x=270, y=385)

            button_720p = PhotoImage(file=resource_path("720p_button.png"))
            button_720p_label = Label(image=button_720p, borderwidth=0)
            button_720p_label.place(x=350, y=385)
            real_button_720p = Button(root, image=button_720p, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                                      command=lambda: res_getter("720p"))
            real_button_720p.place(x=350, y=385)

        if resolution == "360p":
            button_144p = PhotoImage(file=resource_path("144p_button.png"))
            button_144p_label = Label(image=button_144p, borderwidth=0)
            button_144p_label.place(x=30, y=385)
            real_button_144p = Button(root, image=button_144p, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                                      command=lambda: res_getter("144p"))
            real_button_144p.place(x=30, y=385)

            button_240p = PhotoImage(file=resource_path("240p_button.png"))
            button_240p_label = Label(image=button_240p, borderwidth=0)
            button_240p_label.place(x=110, y=385)
            real_button_240p = Button(root, image=button_240p, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                                      command=lambda: res_getter("240p"))
            real_button_240p.place(x=110, y=385)

            button_360p = PhotoImage(file=resource_path("selected_360p_button.png"))
            button_360p_label = Label(image=button_360p, borderwidth=0)
            button_360p_label.place(x=190, y=385)
            real_button_360p = Button(root, image=button_360p, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                                      command=lambda: res_getter("360p"))
            real_button_360p.place(x=190, y=385)

            button_480p = PhotoImage(file=resource_path("480p_button.png"))
            button_480p_label = Label(image=button_480p, borderwidth=0)
            button_480p_label.place(x=270, y=385)
            real_button_480p = Button(root, image=button_480p, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                                      command=lambda: res_getter("480p"))
            real_button_480p.place(x=270, y=385)

            button_720p = PhotoImage(file=resource_path("720p_button.png"))
            button_720p_label = Label(image=button_720p, borderwidth=0)
            button_720p_label.place(x=350, y=385)
            real_button_720p = Button(root, image=button_720p, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                                      command=lambda: res_getter("720p"))
            real_button_720p.place(x=350, y=385)

        if resolution == "480p":
            button_144p = PhotoImage(file=resource_path("144p_button.png"))
            button_144p_label = Label(image=button_144p, borderwidth=0)
            button_144p_label.place(x=30, y=385)
            real_button_144p = Button(root, image=button_144p, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                                      command=lambda: res_getter("144p"))
            real_button_144p.place(x=30, y=385)

            button_240p = PhotoImage(file=resource_path("240p_button.png"))
            button_240p_label = Label(image=button_240p, borderwidth=0)
            button_240p_label.place(x=110, y=385)
            real_button_240p = Button(root, image=button_240p, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                                      command=lambda: res_getter("240p"))
            real_button_240p.place(x=110, y=385)

            button_360p = PhotoImage(file=resource_path("360p_button.png"))
            button_360p_label = Label(image=button_360p, borderwidth=0)
            button_360p_label.place(x=190, y=385)
            real_button_360p = Button(root, image=button_360p, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                                      command=lambda: res_getter("360p"))
            real_button_360p.place(x=190, y=385)

            button_480p = PhotoImage(file=resource_path("selected_480p_button.png"))
            button_480p_label = Label(image=button_480p, borderwidth=0)
            button_480p_label.place(x=270, y=385)
            real_button_480p = Button(root, image=button_480p, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                                      command=lambda: res_getter("480p"))
            real_button_480p.place(x=270, y=385)

            button_720p = PhotoImage(file=resource_path("720p_button.png"))
            button_720p_label = Label(image=button_720p, borderwidth=0)
            button_720p_label.place(x=350, y=385)
            real_button_720p = Button(root, image=button_720p, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                                      command=lambda: res_getter("720p"))
            real_button_720p.place(x=350, y=385)

        if resolution == "720p":
            button_144p = PhotoImage(file=resource_path("144p_button.png"))
            button_144p_label = Label(image=button_144p, borderwidth=0)
            button_144p_label.place(x=30, y=385)
            real_button_144p = Button(root, image=button_144p, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                                      command=lambda: res_getter("144p"))
            real_button_144p.place(x=30, y=385)

            button_240p = PhotoImage(file=resource_path("240p_button.png"))
            button_240p_label = Label(image=button_240p, borderwidth=0)
            button_240p_label.place(x=110, y=385)
            real_button_240p = Button(root, image=button_240p, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                                      command=lambda: res_getter("240p"))
            real_button_240p.place(x=110, y=385)

            button_360p = PhotoImage(file=resource_path("360p_button.png"))
            button_360p_label = Label(image=button_360p, borderwidth=0)
            button_360p_label.place(x=190, y=385)
            real_button_360p = Button(root, image=button_360p, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                                      command=lambda: res_getter("360p"))
            real_button_360p.place(x=190, y=385)

            button_480p = PhotoImage(file=resource_path("480p_button.png"))
            button_480p_label = Label(image=button_480p, borderwidth=0)
            button_480p_label.place(x=270, y=385)
            real_button_480p = Button(root, image=button_480p, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                                      command=lambda: res_getter("480p"))
            real_button_480p.place(x=270, y=385)

            button_720p = PhotoImage(file=resource_path("selected_720p_button.png"))
            button_720p_label = Label(image=button_720p, borderwidth=0)
            button_720p_label.place(x=350, y=385)
            real_button_720p = Button(root, image=button_720p, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                                      command=lambda: res_getter("720p"))
            real_button_720p.place(x=350, y=385)

    def choose_path():
        path = filedialog.askdirectory()
        path_data = path_entry.get()

        if len(path_data) == 0:
            path_entry.insert(0, path)

        else:
            path_entry.delete(0, END)
            path_entry.insert(0, path)

    def download():
        global link

        link = link_entry.get()

        try:
            mp4_video = YouTube(link).streams.filter(res=resolution_value).first().download(
                filename_prefix=f"{resolution_value}_", output_path=path_entry.get())
            link_entry.delete(0, END)
            status_entry.delete(0, END)
            status_entry.insert(0, " Downloaded succsesfully!")

        except pytube.exceptions.RegexMatchError:
            if len(status_entry.get()) == 0:
                status_entry.insert(0, "Not a youtube link!")
            else:
                status_entry.delete(0, END)
                status_entry.insert(0, "Not a youtube link!")

        except NameError:
            if len(status_entry.get()) == 0:
                status_entry.insert(0, "Invalid resolution!")
            else:
                status_entry.delete(0, END)
                status_entry.insert(0, "Invalid resolution!")

        except FileNotFoundError:
            if len(status_entry.get()) == 0:
                status_entry.insert(0, "Enter a valid folder!")
            else:
                status_entry.delete(0, END)
                status_entry.insert(0, "Enter a valid folder!")

        except:
            status_entry.insert(0, "Check your internet connection!")

    link_entry = Entry(root, width=20, borderwidth=0, font=default_font, bg="#121212", foreground="white")
    link_entry.place(x=55, y=152, height=30, width=340)

    path_entry = Entry(root, width=20, borderwidth=0, font=default_font, bg="#121212", foreground="white")
    path_entry.place(x=55, y=270, height=30, width=340)

    status_entry = Entry(root, width=20, borderwidth=0, font=default_font, bg="#121212",
                         foreground="white")
    status_entry.place(x=55, y=580, height=30, width=340)

    button_choose_path = PhotoImage(file=resource_path("choose_path_button.png"))
    button_choose_path_label = Label(image=button_choose_path, borderwidth=0)
    button_choose_path_label.place(x=200, y=315)
    real_button_choose_path = Button(root, image=button_choose_path, borderwidth=0, activebackground="#1F1F1F",
                                     bg="#1F1F1F", command=choose_path)
    real_button_choose_path.place(x=200, y=315)

    button_download = PhotoImage(file=resource_path("download_button.png"))
    button_download_label = Label(image=button_download, borderwidth=0)
    button_download_label.place(x=200, y=460)
    real_button_download = Button(root, image=button_download, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                                  command=download)
    real_button_download.place(x=200, y=460)

    button_144p = PhotoImage(file=resource_path("144p_button.png"))
    button_144p_label = Label(image=button_144p, borderwidth=0)
    button_144p_label.place(x=30, y=385)
    real_button_144p = Button(root, image=button_144p, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                              command=lambda: res_getter("144p"))
    real_button_144p.place(x=30, y=385)

    button_240p = PhotoImage(file=resource_path("240p_button.png"))
    button_240p_label = Label(image=button_240p, borderwidth=0)
    button_240p_label.place(x=110, y=385)
    real_button_240p = Button(root, image=button_240p, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                              command=lambda: res_getter("240p"))
    real_button_240p.place(x=110, y=385)

    button_360p = PhotoImage(file=resource_path("360p_button.png"))
    button_360p_label = Label(image=button_360p, borderwidth=0)
    button_360p_label.place(x=190, y=385)
    real_button_360p = Button(root, image=button_360p, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                              command=lambda: res_getter("360p"))
    real_button_360p.place(x=190, y=385)

    button_480p = PhotoImage(file=resource_path("480p_button.png"))
    button_480p_label = Label(image=button_480p, borderwidth=0)
    button_480p_label.place(x=270, y=385)
    real_button_480p = Button(root, image=button_480p, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                              command=lambda: res_getter("480p"))
    real_button_480p.place(x=270, y=385)

    button_720p = PhotoImage(file=resource_path("720p_button.png"))
    button_720p_label = Label(image=button_720p, borderwidth=0)
    button_720p_label.place(x=350, y=385)
    real_button_720p = Button(root, image=button_720p, borderwidth=0, activebackground="#1F1F1F", bg="#1F1F1F",
                              command=lambda: res_getter("720p"))
    real_button_720p.place(x=350, y=385)


youtube_screen()

root.mainloop()
