import math
from time import sleep

import pyautogui
import pyautogui as gui
import numpy as np
from detection.shapes import detect_posts
from random import randint,random
import logging
from logme import setup_logger

# CTRL + L selects the address bar and ctrl + c will copy it other shortcuts still work


def open_post_new_window(x, y, w, h, debug=False):
    """

    :param x:
    :param y:
    :param w:
    :param h:
    :param debug:
    """
    setup_logger(debug)

    rand_x = randint(x + 10, x + w - 10)
    rand_y = randint(y + 10, y + h - 10)
    duration = random() * 0.5 + 0.5

    if debug:
        logging.debug(f"Moving to coordinates: ({rand_x}, {rand_y}) over a duration of {duration}s.")

    gui.moveTo(rand_x, rand_y, duration)

    if debug:
        logging.debug("Middle click performed.")

    gui.click(button='middle')


def copy(debug=False):
    setup_logger(debug)

    if debug:
        logging.debug("Copying with 'ctrl + c' command.")

    with gui.hold('ctrl'):
        gui.press('c')


def switch_tab(debug=False):
    setup_logger(debug)

    if debug:
        logging.debug("Switching tab with 'ctrl + tab' command.")

    with gui.hold('ctrl'):
        gui.press('tab')


def close_tab(debug=False):
    setup_logger(debug)

    if debug:
        logging.debug("Closing tab with 'ctrl + w' command.")

    with gui.hold('ctrl'):
        gui.press('w')


def like_post(debug=False):
    setup_logger(debug)

    coords = pyautogui.locateOnScreen("template_match/not_liked_full.png")
    if coords is None:
        logging.debug("Coordinates not found.")
        return
    x, y, w, h = coords
    x = int(math.floor((x + int(math.floor(x + w / 3 - 2)))/2))
    rand_x = randint(x-3,x+3)
    rand_y = randint(y + 4, y + h - 4)
    duration = random() * 0.5 + 0.5

    logging.debug(f"Moving cursor to x={rand_x}, y={rand_y}, duration={duration}")
    gui.moveTo(rand_x, rand_y, duration)
    sleep(0.5)

    if pyautogui.locateOnScreen("template_match/not_liked_full.png") is None and pyautogui.locateOnScreen("template_match/not_liked_full_hover.png") is None:
        adjust = randint(-30, -20)
        gui.moveRel(adjust,None,random() * 0.5 + 0.5)
        gui.moveRel(-adjust, None, random() * 0.5 + 0.5)
    gui.click(button='left')
    logging.debug(f"Post liked.")


def check_ig_open(debug=False):
    setup_logger(debug)
    logging.debug('Checking wether Instagram is open.')
    return False if pyautogui.locateOnScreen("template_match/ig_logo.png") is None else True


def check_post_liked(debug=False):
    setup_logger(debug)

    coords = pyautogui.locateOnScreen("template_match/already_liked.png")
    logging.debug('Checking wether post has already been liked.')
    return False if coords is None else True