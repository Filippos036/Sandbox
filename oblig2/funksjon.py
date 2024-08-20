import random
#skjellet 

def funksjon():
    # logikk
    return #verdi

funksjon()

def skriv_hei():
    print("-------")
    print("--Hei--")
    print("-------")
    return

skriv_hei()
#skriv_hei()
#skriv_hei()


def gi_tilfeldig_tall(tall_en, tall_to):
    tilfeldig_tall = random.randrange(tall_en, tall_to)
    return tilfeldig_tall
    #print(tilfeldig_tall)
    

gi_tilfeldig_tall(10,1300)
#print(gi_tilfeldig_tall(100,1000))
tallet = gi_tilfeldig_tall(10,1300)
print("variabelen tallets verdi:")
print(tallet)