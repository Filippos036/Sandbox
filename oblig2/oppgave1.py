# Dette programmet tar inn et input-tall fra brukeren
svaret_om_alt = int(input("Hva er svaret på det utimate spørsmålet om livet, universet og alle ting Hint: det er et tall."))

# Her skjekker programmet om verdien brukeren har skrever er lik 42
if svaret_om_alt == 42:
    print("Det stemmer, meningen med livet er 42!")
else:
    print("FEIL!")

# Denne if-testen sjekker om input-tallet er mellom 30 og 50
if 30 < svaret_om_alt < 50:
    print("Nærme, men feil.")