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

not_together = [("Mats", "Marcus"), ("Marcus", "Iver"), ("Oda", "Erik")]


# Create a dictionary where the keys are the names of the people
# and the values are the lists of people they cannot be in the same group with
not_together_dict = {person: [other for (person, other) in not_together if person == person] for person in klasse9b1}

def create_group(people_list, not_together_dict):
    group = []
    for i in range(4):
        person = random.choice(people_list)
        while person in group or any(x in group for x in not_together_dict[person]):
            person = random.choice(people_list)
        group.append(person)
        people_list.remove(person)
    return group

# the number of groups you want to create
num_groups = 7

def printgrupper():
    for i in range(num_groups):
        if len(klasse9b1) < 4:
            print("Not enough people to create another group.")
            break
        print(f"Group {i+1}: {create_group(klasse9b1, not_together_dict)}")

#printgrupper()