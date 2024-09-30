import random
print("Välkommen att kasta tärning")
print("Ett spel kostar 1 krona")
print("Vinstplan:")
print("två lika - 5 kr")
print("en sexa - 3 kr")
print("stege - 3 kr")
text = input("Välj spela (s), sätt in pengar (i), eller avsluta (a): ")
if text == "a":
    print("Skit i det då.")
if text == "i":
    text = input("Ange belopp att sätta in: ")
    
while text == "j":
    tal1 = random.randrange(1, 7)
    tal2 = random.randrange(1, 7)
    print(tal1, tal2)
    if tal1 or tal2 == 6:
        print("sexvinst")
    if tal2 == tal1 + 1:
        print("stegvinst")
    elif tal1 == tal2:
        print("vinst")
    else:
        print("förlust")
    text = input("Vill du spela igen? j/n: ")
    if text == "a":
        print("Vad roligt att du spelade en stund!")