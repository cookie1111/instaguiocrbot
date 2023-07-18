import pyautogui as gui
import numpy as np
from detection.shapes import detect_posts
from random import randint,random
import logging
from interaction.interactions import *
from detection.shapes import *
from db.db_interaction import DataBase


def open_all_fully_visible(debug=False):
    """
    Opens all the posts visible on the screen in new tabs returns amount of
    posts opened
    :param debug:
    :return: int of posts opened, and the coords of top left most post
    """
    im = np.array(gui.screenshot())
    posts = list(detect_posts(im))

    if debug:
        logging.basicConfig(level=logging.DEBUG)
        logging.debug(f"Detected {len(posts)} posts.")

    for i in posts:
        x, y, w, h = i
        rand_x = randint(x + 10, x + w - 10)
        rand_y = randint(y + 10, y + h - 10)
        duration = random() * 0.5 + 0.5

        if debug:
            logging.debug(f"Moving to coordinates: ({rand_x}, {rand_y}) over a duration of {duration}s.")

        gui.moveTo(rand_x, rand_y, duration)
        gui.click(button='middle')

        if debug:
            logging.debug(f"Middle click performed on post: {i}")

        print(i)

    return len(posts), (x,y,w,h)


# TODO go through the posts given in the previous step(these should be open in new tabs)
#  and like each one and close the tab afterwards
def like_all_opened_posts(amount, debug=False):
    """
    Goes through the post witht he change tab, and likes it and afterwards closes the tab

    :param amount:
    :param debug:
    :return:
    """
    #change tab to the first opened post
    switch_tab(debug)

    for i in range(amount):
        like_post(debug=True)
        check_post_liked(debug=True)
        close_tab(debug)

