#!/usr/bin/env python3

import os
import time

from datetime import datetime
from tkinter import *

# Main


root = Tk()

root.configure(background = "white")
root.attributes("-fullscreen", True)

root.title = "TiOS"

# Tiri Card

tiriResponse = PhotoImage(file = "TiriResponse.png")
tiriCard = Label(root, image=tiriResponse, font = "Roboto 24", anchor="center", text="Hi! I'm Tiri!", compound=CENTER)
tiriCard.pack(pady=(30,30))

def updateCard():
	if os.path.isfile('TiPodFinalResponse.txt'):
		response = open("TiPodFinalResponse.txt", "r")
		tiriCard['text'] = response.read()
		response.close()
	else:
		tiriCard['text'] = "Hello! I'm Tiri and I'm ready to help"
	tiriCard.after(1, updateCard)
	
updateCard()


	
# Time Label

clock = Label(root, text = "?:??", font = "Roboto 54", bg = "white")

clock.pack(pady = (25, 25))

def tick():
	clock.configure(text = time.strftime("%H:%M:%S"))
	clock.after(1000, tick)

tick()