text1=input("Säg ett tal.")
text2=input("Säg ett tal till.")
text3=input("Säg ett tal till.")
tal1=int(text1)
tal2=int(text2)
tal3=int(text3)
if tal1 > tal2 and tal1 > tal3 and tal2 > tal3:
    print(tal3 , ", " , tal2 , ", " , tal1 , ".")
if tal1 > tal2 and tal1 > tal3 and tal3 > tal2:
    print(tal3 , ", " , tal3 , ", " , tal2 , ".")
if tal2 > tal1 and tal2 > tal3 and tal1 > tal3:
    print(tal3 , ", " , tal1 , ", " , tal2 , ".")
if tal2 > tal1 and tal2 > tal3 and tal3 > tal1:
    print(tal1 , ", " , tal3 , ", " , tal2 , ".")
if tal3 > tal1 and tal3 > tal2 and tal1 > tal2:
    print(tal2 , ", " , tal1 , ", " , tal3 , ".")
if tal3 > tal1 and tal3 > tal2 and tal2 > tal1:
    print(tal1 , ", " , tal2 , ", " , tal3 , ".")