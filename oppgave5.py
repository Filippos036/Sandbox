# Oppgave 5
# Oversikt over hvor mange småkaker de 5 personene har spist
Person1 = 5 
Person2 = 9
Person3 = 2.5
Person4 = 21 
Person5 = 0 

# Antall personer viktig for koden senere siden det skal deles med 5 
antall_pers = 5

# Programmet regner ut gjennomsnittlige antall spiste småkaker  
answer = (Person1 + Person2 + Person3 + Person4 + Person5) / antall_pers
# Her printer programmet svaret. int runder svaret om int var ikke med hadde svaret vært 7.5 
print(int(answer)) 
