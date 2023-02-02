import cv2 as cv
import numpy
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(10000)

def recherche_voisinage(A,M,N,i0,j0):
    if A[i0,j0]==255:
        return([i0,j0])
    q=0
    while True:
        q+=1
        for i in range(i0-q,i0+q+1):
            j=j0-q
            if i>=0 and i<M and j>=0 and j<N and A[i,j]==255:
                return([i,j])
            j=j0+q
            if i>=0 and i<M and j>=0 and j<N and A[i,j]==255:
                return([i,j])
        for j in range(j0-q+1,j0+q):
            i=i0-q
            if i>=0 and i<M and j>=0 and j<N and A[i,j]==255:
                return([i,j])
            i=i0+q
            if i>=0 and i<M and j>=0 and j<N and A[i,j]==255:
                return([i,j])



def test_pixel_objet(A,M,N,i,j,liste_pixels):
    liste_pixels.append([i,j])
    A[i,j]=100
    voisins=[(i+1,j),(i-1,j),(i,j-1),(i,j+1)]
    for (k,l) in voisins:
        if k>=0 and k<M and l>=0 and l<N:
            if A[k,l]==255:
                test_pixel_objet(A,M,N,k,l,liste_pixels)
                

def barycentre(liste_pixels):
    N=len(liste_pixels)
    xG=0.0
    yG=0.0
    for pixel in liste_pixels:
        xG += pixel[1]
        yG += pixel[0]
    xG /= N
    yG /= N
    return ([xG,yG])


    

video = cv.VideoCapture("billes-2.mp4")

def onMouse(event,x,y,flags,param):
    global i0,j0
    if event==cv.EVENT_LBUTTONUP:
        j0=x
        i0=y
        print(i0,j0)

        
cv.namedWindow("frame")

cv.setMouseCallback('frame',onMouse)
f=0
while f<141:
    success,frame=video.read()
    f += 1

cv.imshow('frame',frame)
print(cv.waitKey())

cv.imwrite("billes-2-frame141.jpg",frame)
hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
hue = hsv[:,:,0]
sat = hsv[:,:,1]
val = hsv[:,:,2]
plt.figure(figsize=(8,12))
plt.subplot(311)
plt.imshow(hue,cmap=plt.cm.gray)
plt.subplot(312)
plt.imshow(sat,cmap=plt.cm.gray)
plt.subplot(313)
plt.imshow(val,cmap=plt.cm.gray)
plt.savefig('billes-2-frame141-HSV.png')
plt.show()

region = frame[334:384,594:638,:]
cv.imshow('frame',region)
cv.waitKey()
hsv = cv.cvtColor(region,cv.COLOR_BGR2HSV)
hist1 = cv.calcHist([hsv],[0,1],None,[30,30],[0,180,0,255])
cv.normalize(hist1, hist1, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
plt.matshow(hist1,extent=[0,255,0,180],cmap=plt.cm.gray)
plt.ylabel("Hue")
plt.xlabel("Sat")
plt.savefig("billes-2-frame141-hist1.png")
plt.show()

region = frame[333:377,31:70,:]
cv.imshow('frame',region)
cv.waitKey()
hsv = cv.cvtColor(region,cv.COLOR_BGR2HSV)
hist2 = cv.calcHist([hsv],[0,1],None,[30,30],[0,180,0,255])
cv.normalize(hist2, hist2, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
plt.matshow(hist2,extent=[0,255,0,180],cmap=plt.cm.gray)
plt.ylabel("Hue")
plt.xlabel("Sat")
plt.savefig("billes-2-frame141-hist2.png")
plt.show()

region = frame[500:600,100:200,:]
cv.imshow('frame',region)
cv.waitKey()
hsv = cv.cvtColor(region,cv.COLOR_BGR2HSV)
hist_fond = cv.calcHist([hsv],[0,1],None,[30,30],[0,180,0,255])
cv.normalize(hist_fond, hist_fond, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
plt.matshow(hist_fond,extent=[0,255,0,180],cmap=plt.cm.gray)
plt.ylabel("Hue")
plt.xlabel("Sat")
plt.savefig("billes-2-frame141-hist_fond.png")
plt.show()




hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
hue,sat,val=cv.split(hsv)
back_proj = cv.calcBackProject([hsv],[0,1],hist1,[0,180,0,255],scale=1)
cv.imshow('frame',back_proj)
cv.imwrite("billes-2-frame141-b1.jpg",back_proj)
cv.waitKey()
r,img = cv.threshold(back_proj,100,255,cv.THRESH_BINARY)
cv.imwrite("billes-2-frame141-b1-seuil.jpg",img)

dilatation=13
element = cv.getStructuringElement(cv.MORPH_RECT,(dilatation,dilatation))
img = cv.dilate(img,element)
cv.imwrite("billes-2-frame141-b1-seuil-dilatation.jpg",img)
img = cv.erode(img,element)
cv.imwrite("billes-2-frame141-b1-seuil-dilatation-erosion.jpg",img)

back_proj = cv.calcBackProject([hsv],[0,1],hist2,[0,180,0,255],scale=1)
cv.imshow('frame',back_proj)
cv.imwrite("billes-2-frame141-b2.jpg",back_proj)
cv.waitKey()

i1=364
j1=615

i2=357
j2=53



(M,N,c)=frame.shape
liste_G2 = []
liste_G1 = []


f=0
trace=True

videoWriter = cv.VideoWriter("billes-2-positions.avi",cv.VideoWriter_fourcc('I','4','2','0'),10,(N,M))

while success:
    success,frame=video.read()
    
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    val = hsv[:,:,2]
    
    back_proj = cv.calcBackProject([hsv],[0,1],hist1,[0,180,0,255],scale=1)
    r,img = cv.threshold(back_proj,100,255,cv.THRESH_BINARY)
    
    img = cv.dilate(img,element)
    [i1,j1] = recherche_voisinage(img,M,N,i1,j1)
    liste_pixels=[]
    test_pixel_objet(img,M,N,i1,j1,liste_pixels)
    [xG,yG]=barycentre(liste_pixels)
    j1=int(xG)
    i1=int(yG)
    liste_G1.append([xG,M-yG])
    L=50
    img[i1-L:i1+L,j1]=200
    img[i1,j1-L:j1+L]=200
    if trace:
        cv.imshow('frame',img)
        if cv.waitKey(500)==113: break

    back_proj = cv.calcBackProject([hsv],[0,1],hist2,[0,180,0,255],scale=1)
    r,img = cv.threshold(back_proj,100,255,cv.THRESH_BINARY)
    img = cv.dilate(img,element)
    [i2,j2] = recherche_voisinage(img,M,N,i2,j2)
    liste_pixels=[]
    test_pixel_objet(img,M,N,i2,j2,liste_pixels)
    [xG,yG]=barycentre(liste_pixels)
    j2=int(xG)
    i2=int(yG)
    liste_G2.append([xG,M-yG])
    L=50
    img[i2-L:i2+L,j2]=200
    img[i2,j2-L:j2+L]=200
    if trace:
        cv.imshow('frame',img)
        if cv.waitKey(500)==113: break

    frame[i1-L:i1+L,j1]=[255,255,255]
    frame[i1,j1-L:j1+L]=[255,255,255]
    frame[i2-L:i2+L,j2]=[255,255,255]
    frame[i2,j2-L:j2+L]=[255,255,255]
    cv.imshow('frame',frame)
    videoWriter.write(frame)
    if cv.waitKey(500)==113: break
    f+=1
    
videoWriter.release()
    
liste_G1=numpy.array(liste_G1)
liste_G2=numpy.array(liste_G2)
plt.figure()
plt.axes().set_aspect('equal')
plt.plot(liste_G1[:,0],liste_G1[:,1],"r.")
plt.plot(liste_G2[:,0],liste_G2[:,1],"b.")
plt.xlim(0,N)
plt.ylim(0,M)
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.savefig("billes-2-positions.png")
plt.show()
