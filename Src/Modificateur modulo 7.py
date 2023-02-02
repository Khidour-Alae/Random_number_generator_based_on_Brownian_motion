import numpy as np
with open("Data_vid/data_vid_1_to_9_torandomnumber.txt") as f:
    content=f.read().splitlines()
s=content[0]
s = np.array(list(s),dtype=int)
liste1=[]
liste2=[]
liste3=[]
liste4=[]
liste5=[]
liste6=[]
liste7=[]
for i in range(len(s)):
    if i%7==0:
        liste1.append(s[i])
    if i%7==1:
        liste2.append(s[i])
    if i%7==2:
        liste3.append(s[i])
    if i%7==3:
        liste4.append(s[i])
    if i%7==4:
        liste5.append(s[i])
    if i%7==5:
        liste6.append(s[i])
    if i%7==6:
        liste7.append(s[i])
s=np.array(liste1+liste2+liste3+liste4+liste5+liste6+liste7)
s=np.array(list(s),dtype=str).tolist()
string=""
for i in s:
    string+=i
with open('Data_vid/données modifiées mod 7.txt','w') as f:
    f.write(string)

