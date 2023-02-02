import numpy as np
from PIL import Image


##img = Image.open('P:/TIPE/test2.png')
##r,g,b=img.split()
##r=np.array(r)
##g=np.array(g)
##b=np.array(b)
##r=r.astype(np.int)
##g=g.astype(np.int)
##b=b.astype(np.int)
##X,Y=img.size

##img = img.convert('L')
##
##largeur, hauteur = img.size
##
##seuil = 50
##
##for x in range(largeur):
##    for y in range(hauteur):
##        pixel = img.getpixel((x,y))
##        if pixel > seuil : img.putpixel((x,y), 250)
##
#img.show()


######import cv2 
######
######key = cv2. waitKey(1)
######webcam = cv2.VideoCapture(0)
######while True:
######    try:
######        check, frame = webcam.read()
######        print(check) #prints true as long as the webcam is running
######        print(frame) #prints matrix values of each framecd 
######        cv2.imshow("Capturing", frame)
######        key = cv2.waitKey(1)
######        if key == ord('s'): 
######            cv2.imwrite(filename='saved_img.jpg', img=frame)
######            webcam.release()
######            img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
######            img_new = cv2.imshow("Captured Image", img_new)
######            cv2.waitKey(1650)
######            cv2.destroyAllWindows()
######            print("Processing image...")
######            img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
######            print("Converting RGB image to grayscale...")
######            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
######            print("Converted RGB image to grayscale...")
######            print("Resizing image to 28x28 scale...")
######            img_ = cv2.resize(gray,(28,28))
######            print("Resized...")
######            img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
######            print("Image saved!")
######        
######            break
######        elif key == ord('q'):
######            print("Turning off camera.")
######            webcam.release()
######            print("Camera off.")
######            print("Program ended.")
######            cv2.destroyAllWindows()
######            break
######        
######    except(KeyboardInterrupt):
######        print("Turning off camera.")
######        webcam.release()
######        print("Camera off.")
######        print("Program ended.")
######        cv2.destroyAllWindows()
######        break




#https://github.com/kevinam99/capturing-images-from-webcam-using-opencv-python
import cv2
import time

def tp(tps = 60, nbphoto = 30):
    startingtime = time.time()
    counter = 1
    te = tps/nbphoto
    webcam = cv2.VideoCapture(0)
    while counter <= nbphoto:
        check, frame = webcam.read()
        time.sleep(te)
        cv2.imwrite(filename='img_' + str(counter) + '.jpg', img=frame)
        counter += 1
    endtime = time.time()
    print(endtime - startingtime)



##import cv2
##
##
##def get_frames():
##    cap = cv2.VideoCapture('test.mp4')
##    i = 0
##    # a variable to set how many frames you want to skip
##    frame_skip = 10
##    while cap.isOpened():
##        ret, frame = cap.read()
##        if not ret:
##            break
##        if i > frame_skip - 1:
##            cv2.imwrite('test_'+str(i)+'.jpg', frame)
##            i = 0
##            continue
##        i += 1
##
##    cap.release()
##    cv2.destroyAllWindows()













