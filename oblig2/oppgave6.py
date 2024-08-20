
Pakke_reise_liste = ["Pass", "Bagasje", "Penger","Bankkort",]

# En while-løkke som kjører koden om og om igjen fram til brukeren bestemmer å avlutte
while True:
    command = int(input("Skriv 1 for å legge inn noe, 2 for å slette noe, 3 for å skrive ut hele listen, 4 for å avslutte programmet:"))
    # koden gir brukeren valget om de vil legge noe inn i lista 
    if command == 1:
        ting = input("Hva vil du legge inn?")
        Pakke_reise_liste.append(ting)
        print(f"{ting} er lagt inn i pakkelisten")
   # koden gir brukeren valget om de vil fjerne noe fra lista
    elif command == 2:
        ting = input("Hva vil du fjerne fra listen?")
        Pakke_reise_liste.remove(ting)
        print(f"{ting} er nå fjernet fra listen")
   # koden printer lista 
    elif command == 3:
        print(Pakke_reise_liste)
    # koden gir brukeren valget med å avslutte programmet
    if command == 4:
        print("Programmet avsluttes")
        break

    

