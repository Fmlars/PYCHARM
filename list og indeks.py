listenmin = []
#lager tom liste

for index in range(5):
    inputt = str(input("Skriv inn det du vil legge til: "))
#vi blir spurt om å skrive inn noe

    listenmin.append(inputt)
#legger til det vi skrev inn

hvormange = int(input("Hvor mange vil du skrive ut: "))

for i in range(hvormange):
    print(listenmin[i])

#for i, value in enumerate(listenmin):
#    print(i, value)














#print(listenmin[0]+listenmin[1]
#+listenmin[2]+listenmin[3]+listenmin[4])
#skriver ut det som står i listen til
#konsoll