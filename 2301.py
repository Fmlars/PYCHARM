import random

people = ["John", "Mary", "Bob", "Samantha", "Mike", "Emily", "Jessica", "David", "Daniel", "Brian"]
not_together = [("John", "Mary"), ("Bob", "Samantha"), ("Mike", "Emily")]

def create_group(people_list, not_together_list):
    group = []
    for i in range(4):
        person = random.choice(people_list)
        while person in group or any(x in group for x in not_together_list if person in x):
            person = random.choice(people_list)
        group.append(person)
        people_list.remove(person)
    return group

# the number of groups you want to create
num_groups = 3

for i in range(num_groups):
    if len(people) < 4:
        print("Not enough people to create another group.")
        break
    print(f"Group {i+1}: {create_group(people, not_together)}")