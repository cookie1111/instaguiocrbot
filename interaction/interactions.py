import pyautogui as gui
import numpy as np
from detection.shapes import detect_posts
from random import randint,random
import logging


def open_post_new_window(x, y, w, h, debug=False):
    """

    :param x:
    :param y:
    :param w:
    :param h:
    :param debug:
    """
    if debug:
        logging.basicConfig(level=logging.DEBUG)

    rand_x = randint(x + 10, x + w - 10)
    rand_y = randint(y + 10, y + h - 10)
    duration = random() * 0.5 + 0.5

    if debug:
        logging.debug(f"Moving to coordinates: ({rand_x}, {rand_y}) over a duration of {duration}s.")

    gui.moveTo(rand_x, rand_y, duration)

    if debug:
        logging.debug("Middle click performed.")

    gui.click(button='middle')


def switch_tab(debug=False):
    if debug:
        logging.basicConfig(level=logging.DEBUG)

    if debug:
        logging.debug("Switching tab with 'ctrl + tab' command.")

    with gui.hold('ctrl'):
        gui.press('tab')


def close_tab(debug=False):
    if debug:
        logging.basicConfig(level=logging.DEBUG)

    if debug:
        logging.debug("Closing tab with 'ctrl + w' command.")

    with gui.hold('ctrl'):
        gui.press('w')