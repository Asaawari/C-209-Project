import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from playsound import playsound 
import pygame
from pygame import mixer
import os
import time

PORT = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

name = None
listbox =  None
filePathLabel = None

global song_counter
song_counter = 0

def musicWindow():
    global song_counter
    global filePathLabel
    global listbox
    global infoLabel

    window = Tk()
    window.title('Music Window')
    window.geometry('300x300')
    window.configure(bg='LightSkyBlue')

    selectLabel = Label(window, text='Select Song', bg='LightSkyBlue',font=('Calibri',8))
    selectLabel.place(x=2,y=1)

    listbox = Listbox(window,height=10,width=27,activestyle='dotbox',bg='LightSkyBlue',borderwidth=2,font=('Calibri',10))
    listbox.place(x=10,y=20)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight=1,relx=1)
    scrollbar1.config(command=listbox.yview)

    for file in os.listdir('shared_files'):
        filename = os.fsdecode(file)
        song_counter = song_counter + 1
        listbox.insert(song_counter, filename)

    playButton = Button(window,text="Play",width=10,bd=1,bg='SkyBlue',font=('Calibri',10),command=play)
    playButton.place(x=30,y=200)

    stop = Button(window,text="Stop",bd=1,width=10,bg='SkyBlue',font=('Calibri',10),command=stopFunction)
    stop.place(x=200,y=200)

    upload = Button(window,text='Upload',width=10,bd=1,bg='SkyBlue',font=('Calibri',10))
    upload.place(x=30,y=250)

    download = Button(window, text='Download',width=10,bg='SkyBlue',font=('Calibri',10))
    download.place(x=200,y=250)

    infoLabel = Label(window, text="",fg="blue",font=("Calibri",8))
    infoLabel.place(x=4,y=280)

    window.mainloop()

def play():
    global listbox
    global song_selected
    song_selected=listbox.get(ANCHOR)

    global infoLabel
    
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()
    if(song_selected != ""):
        infoLabel.configure(text="Now Playing: " +song_selected)
    else:
       infoLabel.configure(text="")

def stopFunction():
    global song_selected
    global infoLabel
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()
    infoLabel.configure(text="")

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    musicWindow()

setup()