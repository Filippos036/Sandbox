# liste med filmer
liste = [
    {"name":"Inception", "Year": 2010, "rating": 8.7},
    {"name":"Inside Ouy", "Year": 2015, "rating": 8.1},
    {"name":"Con Air", "Year": 1997, "rating": 6.9}
]

def legg_inn_film(liste, name, Year, rating=5.0):  # vis en spesifisert rating er ikke gitt, da blir default rating 5.0
    ny_film = {"name": name, "Year": Year, "rating": rating}
    liste.append(ny_film)

# setter inn en ny film i listen
legg_inn_film(liste, "The Godfather", 1972, 9.2)
legg_inn_film(liste, "The Godfather 2", 1974) # setter inn en ny film uten spesifisert rating

# funksjonen printer alle filmene i lista sånn -The Godfather - 1972 has a rating of 9.2-
for film in liste:
    print(f"{film['name']} - {film['Year']} has a rating of {film['rating']}")

# programmet regner ut gjennomsnittrating
def gjennomsnittrating(liste):
    total_rating = 0
    antall_filmer = len(liste)
    for film in liste:
        total_rating += film['rating']
    return total_rating/antall_filmer

# printer gjennomsnittrating
gjennomsnitt = gjennomsnittrating(liste)
print(f"Gjennomsnittlig rating for alle filmer: {gjennomsnitt}")

# printer alle filmene fra 2010 og etter
def filmer_etter_år(film, Year):
    for film in liste:
        if film ['Year'] >= Year: 
            print(f"{film['name']} - {film['Year']} has a rating of {film['rating']}") 

filmer_etter_år(liste, 2010)


# denne funksjonen skriver alle filmene i lista i en ny fil
def skriv_til_movie(liste, filnavn):
    with open(filnavn, 'w') as fil:
        for film in liste:
            fil.write(f"{film['name']} - {film['Year']} has a rating of {film['rating']}\n") # skriver filmene i den nye filen i en fin format

skriv_til_movie(liste, "movies.txt")

# denne funksjonen leser lista med alle filmene
def skriv_ut_fil(filnavn):
    with open(filnavn,'r') as fil:
        innhold = fil.read()
        print(innhold)

skriv_ut_fil("movies.txt")