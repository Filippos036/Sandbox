
# Dette programmet regner volumet på en tredimensjonelt objekt
def regn_volum(lengde, bredde, høyde):
    volum = lengde * bredde * høyde
    return volum

lengde1, bredde1, høyde1 = 12, 13, 4
volum1 = regn_volum(lengde1, bredde1, høyde1)
print(f"volumet er {volum1}")

lengde2, bredde2, høyde2 = 9, 20, 15
volum2 = regn_volum(lengde2, bredde2, høyde2)
print(f"volumet er {volum2}")

lengde3, bredde3, høyde3 = 16, 7, 24
volum3 = regn_volum(lengde3, bredde3, høyde3)
print(f"volumet er {volum3}")