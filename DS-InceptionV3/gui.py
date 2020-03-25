# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os
from gtts import gTTS
from googletrans import Translator
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
root = tk.Tk()
root.title("Indic Image Captioning Prototype")
root.geometry("700x700")
v = tk.IntVar()
v.set(5)
languages = [
    ("Kannada",'kn'),
    ("Marathi",'mr'),
    ("Hindi",'hi'),
    ("Tamil",'ta'),
    ("Bengali",'bn'),
    ("English", 'en')
]
lang = 'en'
def ShowChoice():
    global lang
    if (v.get() == 0):
        lang = 'kn'
    elif (v.get() == 1):
        lang = 'mr'
    elif (v.get() == 2):
        lang = 'hi'
    elif (v.get() == 3):
        lang = 'ta'
    elif (v.get() == 4):
        lang = 'bn'
    elif (v.get() == 5):
        lang = 'en'

tk.Label(root,
         text="""Choose your language:""",
         justify = tk.LEFT,
         padx = 20, font = "Helvetica 16 bold").pack()

tk.Label(root,
         text="""Make Sure Volume is Turned On""",
         justify = tk.LEFT,
         padx = 20, font = "Helvetica 14 bold", fg='red').pack()


for val, language in enumerate(languages):
    tk.Radiobutton(root,
                  text=language,
                  padx = 20,
                  variable=v,
                  command=ShowChoice,
                  value=val).pack(anchor=tk.W)
old_label_image = None
old_label_text = None
filename = None
def submit_lang():
    global old_label_text
    t = Translator()
    cmd = "python sample.py --image='" + filename + "'"
    os.system(cmd)
    f = open("demofile3.txt", "r")
    p = f.read()
    translated_text = t.translate(p, dest=lang).text
    if old_label_text is not None:
        old_label_text.destroy()
    textWidget = tk.Label(root, text = translated_text)
    textWidget.config(font=("fonts-indic", 15))
    textWidget.pack()
    myo = gTTS(text=translated_text, lang=t.detect(translated_text).lang, slow=False)
    myo.save("translated_speech.mp3")
    os.system("mpg321 translated_speech.mp3")
    old_label_text = textWidget

def submit_file():
    global old_label_image
    global filename
    filename = filedialog.askopenfilename(initialdir=".", title="Select A File", filetypes=
    (("jpeg files", "*.jpg"),("png files", "*.png"), ("all files", "*.*")))
    if old_label_image is not None:
        old_label_image.destroy()
    im = Image.open(filename)
    im = Image.open(filename).resize((600,400), Image.ANTIALIAS)
    tkimage = ImageTk.PhotoImage(im)
    myvar = tk.Label(root, image = tkimage)
    myvar.image = tkimage
    myvar.pack()
    old_label_image = myvar

P = tk.Button(root, text ="Select File", command = submit_file)
B = tk.Button(root, text ="Submit Language", command = submit_lang)
P.pack()
B.pack()
root.mainloop()
