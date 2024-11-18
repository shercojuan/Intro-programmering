import random
para = 0
print("Välkommen att kasta tärning")
print("Ett spel kostar 1 krona")
print("Vinstplan:")
print("två lika - 5 kr")
print("en sexa - 3 kr")
print("stege - 3 kr")
text = input("Välj spela (s), sätt in pengar (i), eller avsluta (a): ")
if text == "a":
    print("Skit i det då.")
else:
    spelar = True
    while spelar:
        if text == "i":
            para = para + int(input("Ange belopp att sätta in: "))
            print("Att spela för: " ,para, "kr")
            text = input("Välj spela (s), sätt in pengar (i), eller avsluta (a): ")
        elif text == "s":
            if para < 1 :
                print("Sätt in mer pengar.")
            else:
                tal1 = random.randrange(1, 7)
                tal2 = random.randrange(1, 7)
                print(tal1, tal2)
                if tal1 == 6 or tal2 == 6:
                    print("sex-vinst + 3kr")
                    para = para + 2
                elif tal2 == tal1 + 1:
                    print("stegvinst + 3kr")
                    para = para + 2
                elif tal1 == tal2:
                    print("vinst + 5kr")
                    para = para + 4
                else:
                    print("förlust")
                    para = para - 1
            print("Att spela för: " ,para, "kr")
            text = input("Välj spela (s), sätt in pengar (i), eller avsluta (a): ")
        if text == "a":
            spelar = False
            print("Vad roligt att du spelade en stund!")