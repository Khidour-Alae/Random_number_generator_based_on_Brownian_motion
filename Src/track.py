import cv2
import numpy as np

vidpath = "video1.mp4"

def seuil(vpath,val_seuil):
vid = cv2.VideoCapture(vpath)
c = 0
ret, frame = vid.read()
img = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
img = img[0:1080,20:1100]
img = cv2.resize(img,(300,300))
while ret:
    for y in range(300):
        for x in range(300):
            if img[y,x] < val_seuil and (x-150)**2 + (y-150)**2 <= 120*120 : img[y,x] = 0
            else : img[y,x] = 255
    cv2.imwrite("video1bis/video1bis_" + str(c) + ".jpg",img)
    ret, frame = vid.read()
    img = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    img = img[0:1080,20:1100]
    img = cv2.resize(img,(300,300))
    c = c + 1
seuil(vidpath,70)
