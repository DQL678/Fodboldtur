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

def registrer_betaling():
    navn = input("Indtast navn: ")
    beløb = float(input("Indtast beløb: "))

    if navn in fodboldtur:
        fodboldtur[navn].append(beløb)
    else:
        fodboldtur[navn] = [beløb]

    print(f"Registreret {beløb} kroner for {navn}")

def udskriv_status():
    mangler_liste = []

    for navn, betalinger in fodboldtur.items():
        total = sum(betalinger)
        mangler = 4500 - total

        if mangler <= 0:
            print(f"{navn}: Har betalt {total} kroner")
        else:
            print(f"{navn}: Har betalt {total} kroner. Mangler {mangler} kroner")

    mangler_liste.sort(key = lambda x: x[1], reverse = True)

    print("Top 3")
    for navn, mangler in mangler_liste[:3]:
        if mangler > 0:
            print(f"{navn}: Mangler {mangler} kroner")

def gem_data():
    with open(filename, 'wb') as f:
        pickle.dump(fodboldtur, f)
    print("Data gemt.")

def nulstil():
    global fodboldtur
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
    gem_data()
    print("Data er nulstillet")

def menu():
    print("MENU")
    print("1: Registrer betaling")
    print("2: Udskriv status")
    print("3: Gem data")
    print("4: Afslut")
    print("5: Nulstil data")

    valg = input("Vælg: ")

    if valg == '1':
        registrer_betaling()
    elif valg == '2':
        udskriv_status()
    elif valg == '3':
        gem_data()
    elif valg == '4':
        gem_data()
        print("Program afsluttet.")
        return
    elif valg == '5':
        nulstil()
    menu()

menu()
