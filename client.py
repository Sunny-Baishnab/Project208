from msilib.schema import ListBox
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

PORT = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096
select_label = None
listbox = None
info_label = None

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    musicWindow()

def musicWindow():
    window = Tk()
    window.title('Music Window')
    window.geometry("300x300")
    window.configure(bg = 'LightSkyBlue')

    select_label = Label(window, text = "Select Song", bg = 'LightSkyBlue', font = ("Calibri",8))
    select_label.place(x = 2,y = 1)

    list_box = Listbox(window, height = 10, width = 39, activestyle='dotbox', bg = 'LightSkyBlue', borderwidth = 2, font = ("Calibri",10))
    list_box.place(x = 10, y = 10)

    scroll_bar1 = Scrollbar(list_box)
    scroll_bar1.place(relheight = 1, relx = 1)
    scroll_bar1.config(command = list_box.yview)

    play_button = Button(window,text = "play", width = 10, bd = 1, bg = 'skyBlue', font = ("Calibri",10))
    play_button.place(x = 30, y = 200)

    stop = Button(window, text = "Stop", bd = 1, width = 10, bg = "skyBlue", font = ("Calibri",10))
    stop.place(x = 200, y = 200)

    upload = Button(window, text = "Uplaod",width = 10, bd = 1, bg = "skyBlue", font = ("Calibri",10))
    upload.place(x = 30, y = 250)

    download = Button(window, text = "Download", width = 10, bd = 1, bg = "skyBlue", font = ("Calibri",10))
    download.place(x = 200, y = 250)

    info_label = Label(window, text = "", fg = "blue", font = ("Calibri",8))
    info_label.place(x = 4, y = 200)

    window.mainloop()

setup()