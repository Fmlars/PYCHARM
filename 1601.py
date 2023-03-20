import random as r

heleklassen = ["fredrik","iben","sofie","selma K", "sophia","nils","sigurd","felix P", "felix W", "hannah", "eivind", "philip", "olav", "sebastian"]
grp1 = []
grp2 = []
grp3 = []
grp4 = []

lengde = len(heleklassen)
print("Antall i klassen: ",lengde)

#print(heleklassen[r.randint(0,13)])
#print("-------")
#print(r.choice(heleklassen))



for i in range(4):
    elev = r.choice(heleklassen)
    grp1.append(elev) #legge til en tilfeldig person fra heleklassen inn i grp1
    heleklassen.remove(elev)
    #print(grp1)


for i in range(4):
    elev = r.choice(heleklassen)
    grp2.append(elev) #legge til en tilfeldig person fra heleklassen inn i grp1
    heleklassen.remove(elev)
    #print(grp2)

print(grp1)
print("-----")
print(grp2)
print("----")
print(len(heleklassen))