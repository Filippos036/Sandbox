
# Input på hvor mange skal spille
import random
spillere = int(input("Hvor mange skal spile?:"))


# Her generer koden random score tre ganger for spillerne.
for i in range(spillere):
    liste = []
    for i in range(3):
        print(random.randrange(0,61))