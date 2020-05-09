import os


import pygame
from tkinter.filedialog import Tk, Button, askdirectory, Label, Listbox, LEFT, RIGHT

from mutagen.id3 import ID3

root = Tk()

listofsongs = []
formattedlist = []
realnames = []

index = 0

def directorychoose():
    filename = askdirectory()
    os.chdir(filename)

    for file in os.listdir(filename):
        if file.endswith(".mp3"):
            realdir = os.path.realpath(file)
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])
            listofsongs.append(file)

    for file in realnames:
        formattedlist.append(file + "\n")

    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()


def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()


def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()


def stopsong(event):
    pygame.mixer.music.stop()


directorychoose()

label = Label(root, text='Music player')
label.pack()

listbox = Listbox(root)

listbox.pack()
for item in formattedlist:
    listbox.insert(0, item)

button = Button(root, text='Next')
button.pack(side=LEFT)
button2 = Button(root, text='Prev')
button2.pack(side=RIGHT)
stopbutton = Button(root, text='Stop')
stopbutton.pack()

button.bind("<Button-1>", nextsong)
button2.bind("<Button-1>", prevsong)
stopbutton.bind("<Button-1>", stopsong)

root.mainloop(