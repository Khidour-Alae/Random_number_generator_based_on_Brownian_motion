import numpy as np
import math
from scipy.stats import chisquare
import matplotlib.pyplot as plt


def egalite2tab(tab1,tab2):                 #Ce programme teste si 2 tableaux sont les mêmes
    a=True
    i=0
    n=len(tab1)
    while a and i<n:
        a=(tab1[i]==tab2[i])
        i+=1
    return(a)





def suivant(nb):
    #Ce programme donne à partir d'un nombre "nb" à n chiffres le plus petit
    #nombre supérieur à "nb" constitué des mêmes chiffres que "nb". L'intérêt de ce programme se voit dans la suite
    #Ce programme se base sur l'algorithme suivant:
    #1)On repère la plus longue suite croissante en partant de la droite.Exemple:dans 13542 ça va être 542 
    #2)On note le premier chiffre qui n'est pas dans la suite et on cherche le plus petit chiffre dans la suite d'avant qui lui est supérieur.Dans l'exemple d'avant c'est 4.
    #3)On échange la place de ces 2 chiffres. Dans l'exemple on est passé de 13542 à 14532
    #4)On renverse l'ordre des n premiers chiffres avec n la taille de la suite croissante du début.14532-->14235
    #5)En résumé: 13542-->13|542-->14532-->14|532-->14235


    if egalite2tab(np.flip(np.sort(nb)),nb): # np.flip(np.sort(nb)) correspond au plus grand nombre que nous pouvons créer avec les chiffres du départ
        return(nb)
    else:
        suiv=np.copy(nb)
        n=len(nb)
        suite_decr=[nb[-1]]
        i=0
        while nb[n-1-i]<=nb[n-2-i]:
            i+=1
            suite_decr.append(nb[n-1-i])
        pluspetitplusgrand=9
        for a in suite_decr :
            if a>nb[-i-2] and a<=pluspetitplusgrand:
                pluspetitplusgrand=a
        indice_pluspetitplusgrand=0
        while nb[-1-indice_pluspetitplusgrand]!=pluspetitplusgrand:
            indice_pluspetitplusgrand+=1
        b=len(suite_decr)
        (suiv[n-1-b],suiv[-1-indice_pluspetitplusgrand])=(suiv[-1-indice_pluspetitplusgrand],suiv[n-1-b])
        last_step=np.flip(suiv[n-1-i:n])
        suiv[n-1-i:n]=last_step
        return(suiv)

def TableauToNombre(nb):
    #Ce programme transforme un tableau en l'entier correspondant. Ex: TableauToNombre(np.array([1,2,5]))=125
    n=len(nb)
    i=0
    s=0
    while i!=n:
        s+=(10**i)*nb[-1-i]
        i+=1
    return(int(s))

def recherche_dicho(x,t):
    """Données: t est une liste triée de nombres ou de chaînes de caractères
    x est un nombre ou une chaîne de caractère
    Résultat: si x est un élément de liste, renvoie l’indice de x dans t,
    sinon ne renvoie rien "
    Traitement: on utilise une méthode de dichotomie
    """
    a=0
    b=len(t)-1
    while b-a >= 0:                         # tant qu’il y a un élement d’indice dans [a,b]
        m = (a+b)//2                        # indice médian
        if x == t[m]:
            return(m)
        elif x < t[m]:
            b = m - 1
        else:
            a = m + 1
    return(None)                        #arrivé ici b-a < 0 donc il n’y a plus de mots d’indice dans [a,b], le mot est donc absent



def occurence(tab,nombre):
    #tab=tableau contenant une suite de nombres générés aléatoirement
    #nombre= nombre dont on va chercher l'occurence des 120 états
    #Pour chaque nombre à n chiffres il existe n! façons de réarranger ces chiffres pour en créer de nouveaux.
    #Exemple: avec 1,2,3 on peut créer 6 nombres à 3 chiffres: 123,132,213,...Dans la suite chaqun de ses nombres est appelé "un état"
    #Ce programme permet à partir d'une séquence de chiffres et d'un nombre à n chiffres de compter le nombre de
    #d'occurence de chacun de ses états afin de fournir un tableau (tableau_final) qui donne pour chaque état le nombre de fois qu'il est apparu.
    #La théorie du Test OPERM5 prédit que pour n=5 les états doivent être uniformément distribués.
    #Pour vérifier cela on effectue un test du Chi2 par rapport à une loi uniforme de paramètre (1/(nombre d'états differents))
    #Le programme renvoie la valeur du chi2 et de la p-value. Plus la p-value est proche de 0 plus la loi empirique suit la loi théorique.

    
    n=len(nombre)                           
    t=math.factorial(n)
    tableau_occurence=np.zeros((2,t))
    premier=np.sort(nombre) #Le plus petit nombre qu'on peut former avec n chiffres est le nombre formé à partir des chiffres mis dans l'ordre croissant
    tableau_occurence[0][0]=TableauToNombre(premier)
    for i in range(1,t):
        premier=suivant(premier)
        tableau_occurence[0][i]=TableauToNombre(premier)
    #L'intérêt de la fonction suivant est donc de génerer le tableau déja trié au lieu de le trier après l'avoir générer avec des boucles imbriquées.
    #L'idée derrière le tri est de faire une recherche dichotomique plus tard afin d'optimiser la recherche
    taille_suite=len(tab)
    for i in range(taille_suite-n+1):
        sous_suite=tab[i:i+n]
        liste_possibilité=np.copy(tableau_occurence[0])
        indice=recherche_dicho(TableauToNombre(sous_suite),liste_possibilité)
        if indice or indice==0:
            tableau_occurence[1][indice]+=1

    taille_tableau_final=len(np.unique(tableau_occurence[0]))
    tableau_final=np.zeros((3,taille_tableau_final))
    tableau_final[0]=np.copy(tableau_occurence[0][0:taille_tableau_final])
    tableau_final[1]=np.copy(tableau_occurence[1][0:taille_tableau_final])
    #tableau_occurence pouvait contenir plusieurs fois le même états si le nombre de départ contenait 2 chiffres pareils, tableau_final est juste tableau_occurence sans les répétitions
    tot=sum(tableau_final[1])
    for i in range (taille_tableau_final):
        tableau_final[2][i]=tableau_final[1][i]/tot
    tableau_théorique=(1/taille_tableau_final)*np.ones(taille_tableau_final)
    (chi_square,p)=chisquare(tableau_final[1],(tot/120)*np.ones(taille_tableau_final))
    return(tableau_final,tableau_théorique,chi_square,p)

        
            

"""np.array([1,5,2,4,8,6,3,1,2,5,9,6,3,2,1,5])
np.array([1,2,6,8,5])

s=np.random.random_sample(1000000)
for i in range(len(s)):
    s[i]=int(10*s[i])


with open("Data_vid/data_vid_1_to_9_torandomnumber.txt") as f:
    content=f.read().splitlines()
s=content[0]
s = np.array(list(s),dtype=int)
"""



def OPERM5(n):
    #Afin d'avoir des résultats plus précis, nous réitérons le programme occurence n fois et nous faisons une moyenne de la valeur du chi2 et de la p-value
    #et en prenant à chaque fois une nouvelle valeur à tester prise aléatoirement entre 0 et 99 999 grâce au générateur pseudo-aléatoire de python.
    #Le programme renvoie la valeur moyenne du chi2 et de la p-value pour les n répétitions
    with open("Data_vid/données modifiées mod 7.txt") as f:
        content=f.read().splitlines()
    nos_données=content[0]
    nos_données= np.array(list(nos_données),dtype=int)
    Somme_chi=0
    tableau_chi=np.zeros((2,n))
    for i in range(n):
        c1=np.random.randint(0,10)
        c2=np.random.randint(0,10)
        while c2==c1: c2=np.random.randint(0,10)
        c3=np.random.randint(0,10)
        while c3==c2 or c3==c1:c3=np.random.randint(0,10)
        c4=np.random.randint(0,10)
        while c4==c3 or c4==c2 or c4==c1: c4=np.random.randint(0,10)
        c5=np.random.randint(0,10)
        while c5==c4 or c5==c3 or c5==c2 or c5==c1: c5=np.random.randint(0,10)
        c=np.array([c1,c2,c3,c4,c5])
        tableau_chi[0][i]=TableauToNombre(c)
        tableau_final,tableau_théorique,chi,p=occurence(nos_données,c)
        tableau_chi[1][i]=chi
        Somme_chi+=chi
    moyenne_chi=Somme_chi/n
    return(tableau_chi,moyenne_chi)

    








pythondata=np.random.random_sample(5000000)
for i in range(len(pythondata)):
    pythondata[i]=int(10*pythondata[i])

"""
with open("Data_vid/données modifiées mod 7.txt") as f:
    content=f.read().splitlines()
s=content[0]
s = np.array(list(s),dtype=int)
"""


with open("Data_vid/data_vid_all_better_randomnumbers.txt") as f:
    content=f.read().splitlines()
s=content[0]
s = np.array(list(s),dtype=int)


"""for k in range(1):
    c1=np.random.randint(1,10)
    c2=np.random.randint(1,10)
    while c2==c1: c2=np.random.randint(1,10)
    c3=np.random.randint(1,10)
    while c3==c2 or c3==c1:c3=np.random.randint(1,10)
    c4=np.random.randint(1,10)
    while c4==c3 or c4==c2 or c4==c1: c4=np.random.randint(1,10)
    c5=np.random.randint(1,10)
    while c5==c4 or c5==c3 or c5==c2 or c5==c1: c5=np.random.randint(1,10)
    c=np.array([c1,c2,c3,c4,c5])"""



"""


test=[np.array([7,2,8,4,6]),np.array([3,8,5,1,6]),np.array([2,3,7,5,8])] 
for i in test:
    tableau_final,tableau_théorique,chi,p=occurence(s,i)
    états=np.arange(1,121)
    expérience=tableau_final[2]
    plt.plot(états,expérience,label='valeurs expérimentales pour '+str(TableauToNombre(i))+ ' \ncomme valeur de départ')
    #plt.ylim(-0.03,0.05)
    plt.ylim(-0.1,0.3)
plt.plot(états,tableau_théorique,label='valeurs théoriques \n y=1/120=0.008333')
plt.xlabel("états")
plt.ylabel("probabilité")
plt.title("Courbes expérimentales pour quelques valeurs")
plt.legend()
plt.show()




"""

tableau_final,tableau_théorique,chi,p=occurence(s,np.array([7,1,4,2,8]))
p_tableau_final,p_tableau_théorique,p_chi,p_p=occurence(pythondata,np.array([7,1,4,2,8]))
états=np.arange(1,121)
expérience=tableau_final[2]
p_expérience=p_tableau_final[2]
plt.plot(états,expérience,label='valeurs expérimentales pour nos données')
plt.plot(états,p_expérience,label='valeurs expérimentales pour le générateur de python')
#plt.ylim(-0.03,0.05)
plt.ylim(-0.1,0.3)
plt.plot(états,tableau_théorique,label='valeurs théoriques \n y=1/120=0.008333')
plt.xlabel("états")
plt.ylabel("probabilité")
plt.title("Comparaisons courbes expérimentales pour "+str(TableauToNombre(np.array([7,1,4,2,8])))+ " \ncomme valeur de départ")
plt.legend()
plt.show()





