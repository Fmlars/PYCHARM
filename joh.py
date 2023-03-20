import random
score = 0

tall1 = random.randint(1,10)
tall2 = random.randint(1,10)
answer = tall1 + tall2

print(tall1, "+", tall2)
playerGuess = int(input(""))
if answer == playerGuess:
    score += 1

print("score =", score)