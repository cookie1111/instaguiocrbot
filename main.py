from time import sleep

import cv2 as cv
import pyautogui as gui
import numpy as np
from detection.shapes import detect_posts
from random import randint,random
from interaction.interactions import *
from interaction.actions import *
from db.db_interaction import DataBase

#TODO detection of personal accounts.

#NOTES
#search can type in instantly
#cutecats is a good hashtag and puppies etc

TEST_DB = True


#MAKE SURE TO RUN UNCLUTTER TO HIDE YOUR MOUSE CURSOR WHEN USING THE SCROLL LIKE

def main():
    pics_liked = 0
    #im = np.array(gui.screenshot())
    if check_ig_open():
        for i in range(3):
            print("ig open")
            amnt, coords = open_all_fully_visible()
            im = pyautogui.screenshot(region=coords)
            like_all_opened_posts(amnt)
            pics_liked = pics_liked + amnt
            scroll_till_im_not_visible(im)
    print(f"liked_pics: {pics_liked}")



sleep(10)
main()