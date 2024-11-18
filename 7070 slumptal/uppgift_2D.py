import random
print("Välkommen att spela Lucky Seven")
print("Tre tal slumpas, tre lika tal ger vinst")
print("Tre sjuor ger dubbel vinst")
print("Ett spel kostar en krona")
para = 100
print("Kvar att spela för: ", para, " kronor")
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
        para = para + 100
    elif tal1 == tal2 == tal3:
        print("Vinst!")
        para = para + 50
    elif tal1 == tal2 or tal1 == tal3 or tal2 == tal3:
        print("Minivinst!")
        para = para + 5
    elif tal1 == 7 or tal2 == 7 or tal3 == 7:
        print("Sjuvinst!")
        para = para + 2
    else:
        print("Förlust")
        para = para - 1
    if para <= 0:
        print("Slut på pengar...")
        exit()
    print("Kvar att spela för: ", para, " kronor")
    text = input("Skriv j för att spela och n för att sluta ")
else:
    print("Tack för att du spelade, välkommen åter!")