text1=input("Skriv ett tal.")
text2=input("Skriv ett tal till.")
tal1=int(text1)
tal2=int(text2)
if tal1 > tal2:
    print("Tal ett är störst.")
if tal2 > tal1:
    print("Tal två är störst.")
else:
    print("Talen är lika stora.")