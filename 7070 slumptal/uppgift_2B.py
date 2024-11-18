import random
print("Välkommen att spela Lucky Seven")
print("Tre tal slumpas, tre lika tal ger vinst")
print("Tre sjuor ger dubbel vinst")
text = input("Skriv j för att spela och n för att sluta ")
if text == "n":
    print("Skit i det då")
    exit()
while text == "j":
    tal1 = random.randrange(1, 10)
    tal2 = random.randrange(1, 10)
    tal3 = random.randrange(1, 10)
    print(tal1, tal2, tal3)
    if tal1 == tal2 == tal3 == 7:
        print("Dubbel vinst!")
    elif tal1 == tal2 == tal3:
        print("Vinst!")
    elif tal1 == tal2 or tal1 == tal3 or tal2 == tal3:
        print("Minivinst!")
    else:
        print("Förlust")
    text = input("Skriv j för att spela och n för att sluta ")
else:
    print("Tack för att du spelade, välkommen åter!")