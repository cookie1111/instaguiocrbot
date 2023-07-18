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


def main():
    #im = np.array(gui.screenshot())
    amnt = open_all_fully_visible()
    like_all_opened_posts(amnt)



sleep(10)
main()