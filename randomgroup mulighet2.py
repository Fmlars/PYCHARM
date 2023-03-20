import random

klasse9b1 = ["Jennie", "Maria", "Lykke",
             "Philip", "Mats", "Frida",
             "Magnus","Simen","Herman",
             "Mathias","Maud","Selma",
             "Weiwei","Oda","Axel",
             "Finn","Lea","Iver",
             "Mattis","Nora","Aurora",
             "Ingrid","Felix","Erik",
             "Amy","Erling","Mads","Marcus","My"]
klasse9b2 = ["Walid", "Sigurd", "Karoline",
             "Adam", "Peder", "Jørgen", "Philip",
             "Selma K", "Sebastian", "Selma U", "Aurora",
             "Fredrik", "Felix W","Felix P","Nasrin",
             "Olav","Torstein","Sophia","Sofie","Izabela","Eivind",
             "Erik","Hannah","Marius","Nils", "Olaug","Iben" ]

# a list of tuple where each tuple contains two people that should not be in the same group
not_together = [("Mats", "Marcus"), ("Marcus", "Iver"), ("Oda", "Erik")]

def create_group(people_list, not_together_list):
    group = []
    for i in range(4):
        person = random.choice(people_list)
        while person in group or any(x in group for x in not_together_list if person in x):
            person = random.choice(people_list)
        group.append(person)
        people_list.remove(person)
    return group

num_groups = 7

def laggr():
    for i in range(num_groups):
        if len(klasse9b1) < 4:
            print("Not enough people to create another group.")
            break
        print(f"Group {i+1}: {create_group(klasse9b1, not_together)}")

laggr()
print(klasse9b1)