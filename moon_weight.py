my_earth_weight = float(input("Hva er din vekt?: "))

earth_gravity = 9.807
moon_gravity = 1.622

moon_weight = my_earth_weight / earth_gravity * moon_gravity

print(f"Din vekt på månen er {moon_weight}kg") 

