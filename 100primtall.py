#koden skal printe ut de 100 første primtall

teller = 0
tall = 1
lstprimtall = []


while teller < 100:
    #notprime = False
    if any(tall % i == 0 for i in range(2,tall)): #sjekker om det finnes en delelig faktor
        "" #ingenting skjer
    else: #går inn i else, hvis man ikke gikk inn i forrige "if"
        if tall > 1: #sjekker om variabelen tall er større enn 1
            lstprimtall.append(tall) #legger til variabelen tall inn i listen
    tall = tall + 1 #teller for variabelen tall
    teller = teller + 1 #teller for while løkken

#for i in range(1,len(lstprimtall)):
#   for x in range(2, lstprimtall[x]):
#        if (lstprimtall[x] % x) == 0:
#            lstprimtall.remove(lstprimtall[x])


print(lstprimtall)