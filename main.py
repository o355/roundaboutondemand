# (c) 2017, o355 under the GNU GPL 3.0 license.
# version thereisnoversiontothisprogram

import pygame
from appJar import gui
import sys

def musicButtons(btnName):
    if btnName == "Play it":
        pygame.mixer.music.load("song.mp3")
        pygame.mixer.music.play()
    elif btnName == "Stop Music":
        pygame.mixer.music.stop()
    elif btnName == "Close":
        pygame.mixer.music.stop()
        sys.exit()
app = gui()
pygame.mixer.init()
app.addButton("Play it", musicButtons)
app.addButton("Stop Music", musicButtons)
app.addButton("Close", musicButtons)

app.go()
