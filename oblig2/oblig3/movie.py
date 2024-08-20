# denne funksjonen leser
def skriv_ut_fil(filnavn):
    with open(filnavn, 'r') as fil:
        innhold = fil.read()
        print(innhold)

skriv_ut_fil("movies.txt")
