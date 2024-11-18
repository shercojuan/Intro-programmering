text = input("Säg ett tal: ")
tal = int(text)
while tal != 4:
    text = input("Du gissade fel. Gissa på ett annat tal: ")
    tal = int(text)
print("Du gissade rätt")