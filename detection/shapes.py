import cv2 as cv
import numpy as np

def detect_posts(im: np.array, debug: bool = False) -> list[tuple[int,int,int,int]]:
    """
    Expects instagram to have a dark background yiealds coordinates of posts in the image
    Gives the top left most post as the last post!!!

    :param im: image on which we wish to detect the posts in numpy format
    :param debug: gives a picture of the detected posts
    """
    im = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
    kernel = np.ones((5, 5), np.uint8)
    mask = im.copy()
    mask[mask != 0] = 255
    mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
    if debug:
        cv.imshow("maska", mask)
    ret, thresh = cv.threshold(mask, 50, 255, 0)
    contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        x1, y1 = cnt[0][0]
        apprx = cv.approxPolyDP(cnt, 0.01 * cv.arcLength(cnt, True), True)
        # apprx holds the approximated polygon as a list of points
        if len(apprx) == 4:
            # check if its a square
            x, y, w, h = cv.boundingRect(apprx)
            if w < 10 and h < 10:
                continue
            ratio = float(w) / h
            if ratio >= 0.9 and ratio <= 1.1:
                im = cv.drawContours(im, [cnt], -1, (0, 255, 255), 3)
                cv.putText(im, 'Square', (x1, y1), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
                yield (x, y, w, h)
            else:
                im = cv.drawContours(im, [cnt], -1, (0, 255, 0), 3)
                cv.putText(im, 'Rectangle', (x1, y1), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

    if(debug):
        cv.imshow("Shapes", im)
        #cv.waitKey(0)
        cv.destroyAllWindows()