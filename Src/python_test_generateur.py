# -*- coding: cp1252 -*-
gr = 2463# => graine
np1 = 24375763 # => 1er nombre premier
np2 = 28972763 # => 2e nombre premier
pnp = np1*np2 # => produit des 2 nombres premiers
 
def bitalea():
    """retourne un bit (0 ou 1) tiré au hasard """
    global gr, pnp
    gr = (gr * gr) % pnp
    return gr & 1 # on retourne seulement le bit le moins significatif
 
ch = ""

for i in range(80):
    ch += str(bitalea())
print ch
