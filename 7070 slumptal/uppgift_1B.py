import random
text = input("Vill du spela? j/n: ")
if text == "n":
    print("Skit i det då.")
while text == "j":
    tal1 = random.randrange(1, 7)
    tal2 = random.randrange(1, 7)
    print(tal1, tal2)
    if tal1 or tal2 == 6:
        print("sexvinst")
    elif tal1 == tal2:
        print("vinst")
    else:
        print("förlust")
    text = input("Vill du spela igen? j/n: ")
    if text == "n":
        print("Vad roligt att du spelade en stund!")