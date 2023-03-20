#et primtall er et tall som er bare delelig på seg selv og 1 uten at det
#blir et desimaltegn

def tallinput():
    tall = int(input("Skriv inn et heltall"))

def primtallsjekk():
    tall = int(input("Skriv inn et heltall: "))
    primtall = 0
    for i in range(2,tall):
        if tall % i == 0:
            print("Tallet har faktoren ", i)
            print("Tallet er IKKE et primtall")
            primtall = 1
            break
    if primtall == 0:
        print("Tallet vårt er et primtall")

for i in range(10):
    primtallsjekk()

