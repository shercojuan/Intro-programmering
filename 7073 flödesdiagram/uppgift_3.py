text1 = input("Säg ett tal: ")
text2 = input("Säg ett tal till: ")
tal1 = int(text1)
tal2 = int(text2)
if tal1 > tal2:
    print("Tal ett är störst")
elif tal2 > tal1:
    print("Tal två är störst")