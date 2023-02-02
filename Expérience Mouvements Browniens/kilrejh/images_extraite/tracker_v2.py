import numpy as np
import cv2


def track(fpath):
    print(fpath)
    img = cv2.imread(fpath,0) # 0 = grayscale
    if img == None : print("Error loading the file")

    stop = False
    while not stop :
        seuil = int(input("seuil (0-255) : "))

        stop = bool(input("stop ? True/False"))
