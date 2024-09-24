text = input("Säg ett tal.")
tal=int(text)
count = 1
while count < 4 and tal != 42:
    if tal <42:
        print("För litet.")
        count = count + 1
    if tal >42:
        print("För stort.")
        count = count + 1
if tal == 42:
    print("Rätt svar! Det tog "+str(count)+" gissning(ar).")