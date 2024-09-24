text1=input("Säg ett tal.")
text2=input("Säg ett tal till.")
text3=input("Säg ett tal till.")
tal1=int(text1)
tal2=int(text2)
tal3=int(text3)
if tal1 > tal2 and tal1 > tal3:
    print("Tal 1 är störst.")
if tal2 > tal1 and tal2 > tal3:
    print("Tal 2 är störst.")
if tal3 > tal1 and tal3 > tal2:
    print("Tal 3 är störst.")
else:
    print("Minst två av talen är lika stora.")