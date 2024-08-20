import random 

# genererer en tilfeldig tall
def gi_tilfeldig_tall(tall_en, tall_to):
    tilfeldig_tall = random.randrange(tall_en, tall_to)
    return tilfeldig_tall

# printer tallet 
print("******")
print(f"**{gi_tilfeldig_tall(0,101)}**")
print("******") 
