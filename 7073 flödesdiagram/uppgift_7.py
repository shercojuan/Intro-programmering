import random
text = input("Vill du spela sten sax påse? j/n: ")
if text == "n":
    print("Skit i det då")
while text == "j":
    ssp = input("Sten sax påse: ")
    ssp = ssp.lower()
    if ssp != "sten" and ssp != "sax" and ssp != "påse" :
        print("Säg sten, sax eller påse, pucko!")
    else:
        tal2 = random.randrange(1, 4)
        if tal2 == 1:
            ssp2 = "sten"
        elif tal2 == 2:
            ssp2 = "sax"
        elif tal2 == 3:
            ssp2 = "påse"
        print(ssp2)
        if ssp2 == "sten" and ssp == "sax":
          print("Jag vann!")
        elif ssp2 == "påse" and ssp == "sten":
            print("Jag vann!")
        elif ssp2 == "sax" and ssp == "påse":
            print("Jag vann!")
        elif ssp2 == "sax" and ssp == "sten":
            print("Du vann!")
        elif ssp2 == "sten" and ssp == "påse":
            print("Du vann!")
        elif ssp2 == "påse" and ssp == "sax":
            print("Du vann!")
        else:
            print("Ingen vann")
    text = input("Vill du spela igen? j/n: ")
    if text == "n":
        print("Kul att du ville spela en stund!")