print("== Hva er din vekt på andre planeter? ==")

din_vekt = input(" Hva er din vekt på jorden (i hele kg)") 
if din_vekt. isnumeric() == True:
    din_vekt = int(din_vekt)
    print("ok")
else: 
    print(f" {din_vekt} er ikke en gyldig vekt")
    exit()

if din_vekt <= 0: 
    print(f" Din vekt, {din_vekt} kg er ikke positiv. Prøv igjen")
    exit()
elif din_vekt >= 600:
    print(f"{din_vekt} er enten verdensrekord, eller så lyver du.")
    exit()

planetnavn = input("Hva er planetens navn?")
if planetnavn == "Pluto" or planetnavn == "pluto": 
    print("Pluto er ikke en planet, men OK.")

planetens_tyngdekraft = input("Hva er planetens tyngdekraft?")
planetens_tyngdekraft = float(planetens_tyngdekraft)
if planetens_tyngdekraft <= 0: 
    print(f"Tyngdekraften {planetens_tyngdekraft} kan ikke være 0 eller lavere.")
    exit()

jorden_tyngdekraft = 9.807 

din_masse = din_vekt / jorden_tyngdekraft
din_planet_vekt = din_masse * planetens_tyngdekraft 
din_planet_vekt = round(din_planet_vekt, 2)

print (f"Din vekt på planeten {planetnavn}, med en tyngdekraft på {planetens_tyngdekraft} m/s2 er {din_planet_vekt} kg")