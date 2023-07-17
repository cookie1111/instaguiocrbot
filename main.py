from time import sleep

import cv2 as cv
import pyautogui as gui
import numpy as np
from detection.shapes import detect_posts
from random import randint,random
from interaction.interactions import *

#TODO detection of personal accounts.

#NOTES
#search can type in instantly
#cutecats is a good hashtag and puppies etc

def main():
    screenWidth, screenHeight = gui.size()
    currentMouseX, currentMouseY = gui.position()
    im = np.array(gui.screenshot())
    posts = list(detect_posts(im))
    for i in posts:
        x, y, w, h = i
        gui.moveTo(randint(x+10, x+w-10),randint(y+10, y+h-10),random()*0.5+0.5)
        gui.click(button='middle')
        print(i)
    switch_tab()
    for i in range(len(posts)):
        sleep(1)
        close_tab()

main()