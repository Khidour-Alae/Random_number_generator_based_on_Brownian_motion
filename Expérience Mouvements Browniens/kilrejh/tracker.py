import numpy as np
from PIL import Image


img = Image.open('D:/Alae/Prépa/TIPE/Expérience Mouvements Browniens/kilrejh/images_extraite/cropped_cellede3sec_0.jpg')
##r,g,b=img.split()
##r=np.array(r)
##g=np.array(g)
##b=np.array(b)
##r=r.astype(np.int)
##g=g.astype(np.int)
##b=b.astype(np.int)
##X,Y=img.size

img = img.convert('L')

largeur, hauteur = img.size

seuil = 140

for x in range(largeur):
    for y in range(hauteur):
        pixel = img.getpixel((x,y))
        if pixel > seuil : img.putpixel((x,y), 250)

img.show()
