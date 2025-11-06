import pickle

filename = 'betalinger.pk'

try:
    with open(filename, 'rb') as f:
        fodboldtur = pickle.load(f)
except FileNotFoundError:
    fodboldtur = {}

for navn, betalinger in fodboldtur.items():
    if isinstance(betalinger, (int, float)):
        fodboldtur[navn] = [betalinger]

def indbetal():
    navn = input("Indtast navn: ")
    navn = navn.title().strip()

    while True:
        try:
            beløb = float(input("Indtast beløb: "))
            beløb = round(beløb, 2)
            break
        except ValueError:
            print("Beløbet skal være et tal.")

    if navn in fodboldtur:
        fodboldtur[navn].append(beløb)
    else:
        fodboldtur[navn] = [beløb]

    print(f"Registreret {beløb:.2f} kroner for {navn}")

def status():
    mangler_liste = []

    for navn, betalinger in fodboldtur.items():
        total = round(sum(betalinger), 2)
        mangler = round(4500 - total, 2)

        if mangler <= 0:
            print(f"{navn}: Har betalt {total:.2f} kroner")
        else:
            print(f"{navn}: Har betalt {total:.2f} kroner. Mangler {mangler:.2f} kroner")

        mangler_liste.append((navn, mangler))

    mangler_liste.sort(key=lambda x: x[1], reverse=True)

    print("Top 3 værste:")
    for navn, mangler in mangler_liste[:3]:
        if mangler > 0:
            print(f"{navn}: Mangler {mangler:.2f} kroner")

def gemd():
    with open(filename, 'wb') as f:
        pickle.dump(fodboldtur, f)
    print("Data gemt.")

def nulstil():
    global fodboldtur
    print("Vil du nulstille:")
    print("1: Alle navne")
    print("2: Et specifikt navn")

    valg = input("Vælg: ")

    if valg == '1':
        fodboldtur = {
            "Hans Hansen": [0],
            "Klaus Klausen": [0],
            "Ole Olsen": [0],
            "Bent Bentsen": [0],
            "Peter Petersen": [0],
            "Anders Andersen": [0],
            "Jens Jensen": [0],
            "Ib Ibsen": [0]
        }
        gem()
        print("Alle data er nulstillet.")
    elif valg == '2':
        navn = input("Indtast navnet der skal nulstilles: ").title().strip()
        if navn in fodboldtur:
            fodboldtur[navn] = [0]
            gem()
            print(f"Data for {navn} er nulstillet.")
        else:
            print(f"{navn} findes ikke i systemet.")
    else:
        print("Ikke en gyldig valgmulighed.")

def menu():
    print("MENU")
    print("1: Indbetal")
    print("2: Status")
    print("3: Gem data")
    print("4: Afslut")
    print("5: Nulstil data")

    valg = input("Vælg: ")

    if valg == '1':
        indbetal()
    elif valg == '2':
        status()
    elif valg == '3':
        gem()
    elif valg == '4':
        gem()
        print("Program afsluttet.")
        return
    elif valg == '5':
        nulstil()
    else:
        print("Ikke en valgmulighed.")
    menu()
menu()
