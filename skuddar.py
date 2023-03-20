#hva er skuddår? et år som har en ekstra dag

#hvordan sjekke for skuddår? om året vi er i er delelig på 4
#bruk modulo ( % )

import numpy as np

aar = 2024

if aar % 4 == 0:
    print(str(aar)+" er skuddår")
else:
    print(str(aar)+" er ikke skuddår")

#enkelt og greit, men hvordan sjekke de siste 200 årene? eller de 200 neste årene
#og legge inn alle disse skuddårene inn i tabell som printes ut med informasjon
#om hva tabellen gir oss



arr = np.array([["Område","Frekvens"],["0-9","test"]])

print(arr)
#for i in range(aar, aar+20):
    # print(arr)
    # if i % 4 == 0:
    #     np.append(arr,i,axis=None)


