import cv2
import numpy as np
import matplotlib.pyplot as plt


def resize():
    img = cv2.imread('cropped_cellede3sec_0.jpg')
    print(img.shape)
    x = int(input("x : "))
    y = int(input("y : "))
    img = cv2.resize(img, (y,x))
    cv2.imwrite('cropped_cellede3sec_0.jpg',img)

def crop():
    img = cv2.imread('cellede3sec_0.jpg')
    
    print(img.shape)
    x = int(input("x : "))
    y = int(input("y : "))
    hx = int(input("hx : "))
    hy = int(input("hy : "))


    crop_img = img[x-hx:x+hx,y-hy:y+hy]
    cv2.imwrite('cropped_cellede3sec_0.jpg',crop_img)
    


def get_frames(filename):
    cap = cv2.VideoCapture(filename + '.mp4')
    i = 0
    frame_skip = 10
    c = 0
    nb_frames = 0
    while cap.isOpened():
        nb_frames += 1
        ret, frame = cap.read()
        if not ret:
            break
        if i > frame_skip - 1:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imwrite('cellede3sec_'+str(c)+'.jpg', frame)
            c += 1
            i = 0
            continue
        i += 1

    cap.release()
    cv2.destroyAllWindows()
    print("Nombre de frames : " + str(nb_frames))
