text=input("Vad är näst sista siffran i ditt personnummer?")
tal=int(text)
if tal % 2 == 0 and tal < 10:
    print("Du är tjej.")
if tal % 2 == 1 and tal < 10:
    print("Du är kille.")
if tal > 9:
    print("Du ljuger.")