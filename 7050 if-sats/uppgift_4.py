text=input("Säg ett tal.")
tal=int(text)
if tal >= 0 and tal <= 9:
    print("Talet är ensiffrigt.")
if tal >= 10 and tal <= 99:
    print("Talet är tvåsiffrigt.")
if tal >= 100 and tal <= 999:
    print("Talet är tresiffrigt.")
if tal >= 1000:
    print("Talet är minst fyrsiffrigt.")
if tal < 0:
    print("Talet är negativt.")