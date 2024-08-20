#import math
from math import log 

def hundealder_til_mennskealder(hundealder):
    menneskealder =  16 * log(hundealder) + 31
    return menneskealder

#print(hundealder_til_mennskealder(50))
menneskealder = hundealder_til_mennskealder(10)
print(menneskealder)

def inkluder_moms(pris, moms=0.25):
    pris_med_moms = pris + (pris * moms)
    return pris_med_moms

pris_uten_moms = 100

inkluder_moms(100)
print(inkluder_moms(pris_uten_moms))