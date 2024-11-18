text = input("Säg ett tal: ")
tal = int(text)
gissningar = 0
while tal != 42:
    gissningar = gissningar + 1
    if tal < 42:
        text = input("För litet. Gissa på ett annat tal: ")
        tal = int(text)
    elif tal > 42:
        text = input("För stort. Gissa på ett annat tal: ")
        tal = int(text)
gissningar = gissningar + 1
print("Du behövde ", gissningar, " gissningar för att hitta rätt svar.")