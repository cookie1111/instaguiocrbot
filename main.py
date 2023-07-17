import cv2 as cv
import pyautogui as gui
import numpy as np
from detection.shapes import detect_posts

#TODO detection of personal accounts.

#NOTES
#search can type in instantly
#cutecats is a good hashtag and puppies etc

def main():
    screenWidth, screenHeight = gui.size()
    currentMouseX, currentMouseY = gui.position()
    im = np.array(gui.screenshot())
    for i in detect_posts(im):
        print(i)
    """kernel = np.ones((5, 5), np.uint8)
    #set every pixel in im thats not 0,0,0 to 255,255,255
    #maska = im.copy()
    #maska[im!=0] = 255
    print(im)

    im = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
    print(im)
    mask = im.copy()
    mask[mask != 0] = 255
    mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
    cv.imshow("maska", mask)

    ret,thresh = cv.threshold(mask,50,255,0)

    contours, _ =  cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        x1,y1 = cnt[0][0]
        apprx = cv.approxPolyDP(cnt,0.01*cv.arcLength(cnt, True), True)
        # apprx holds the approximated polygon as a list of points
        if len(apprx) == 4:
            # check if its a square
            x,y,w,h = cv.boundingRect(apprx)
            if w<10 and h<10:
                continue
            ratio = float(w)/h
            if ratio >=0.9 and ratio<=1.1:
                im = cv.drawContours(im, [cnt], -1, (0, 255, 255), 3)
                cv.putText(im,'Square',(x1, y1),cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
            else:
                im = cv.drawContours(im, [cnt], -1, (0, 255, 0), 3)
                cv.putText(im,'Rectangle',(x1, y1),cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

    cv.imshow("Shapes", im)
    cv.waitKey(0)
    cv.destroyAllWindows()
    """
main()