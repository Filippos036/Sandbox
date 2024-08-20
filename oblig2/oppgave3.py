# Har laget en liste med tolkiens sine bøker
bøker = ["The Hobbit", 
         "Farmer Gile of Ham", 
         "The Fellowship of the Ring", 
         "The Two Towers", 
         "The Return og the King", 
         "The Adventures of Tom Bombadil", 
         "Tree and Leaf"]

# Printer de to første bøkene og de to siste i lista
print(bøker[0])
print(bøker[1])
print(bøker[5])
print(bøker[6])

# Her legger jeg inn de bøkene som ble utgitt etter hans død
bøker.append("The Silmarillion")
bøker.append("Unfinished Tales")

#
bøker.pop(2)
bøker.pop(2)
bøker.pop(2)

# Gjør endringer i lista
bøker.insert(2,"Lord of The Rings: The Fellowship of the Ring")
bøker.insert(3,"Lord of The Rings: The Two Towers")
bøker.insert(4,"Lord of The Rings: The Return og the King")
print(bøker)

# Her sorterer jeg lista og printer den ut
bøker.sort()
print(bøker)






