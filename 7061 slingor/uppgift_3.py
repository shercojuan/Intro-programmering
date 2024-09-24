text = input("Säg ett tal.")
tal=int(text)
count = 1
while count < 4 and tal != 42:
    if tal <42:
        print("För litet.")
        count = count + 1
        if count == 4 :
            print("Du fick slut på gissningar.")
        elif count < 4 :
            text=input("Säg ett tal igen.")
            tal=int(text)
    if tal >42:
        print("För stort.")
        count = count + 1
        if count == 4 :
            print("Du fick slut på gissningar.")
        elif count < 4 :
            text=input("Säg ett tal igen.")
            tal=int(text)
if tal == 42:
    print("Rätt svar! Det tog "+str(count)+" gissning(ar).")