import random

people = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heather", "Igor", "Jack"]

def generate_group(people_list):
    group = random.sample(people_list, 4)
    for person in group:
        people_list.remove(person)
    return group

group1 = generate_group(people)
print("Group 1:", group1)
group2 = generate_group(people)
print("Group 2:", group2)

random.sample