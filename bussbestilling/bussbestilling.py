import json
import uuid
import datetime

def loadJson(path):
    with open(path, "r") as file:
        return json.load(file)

def dumpJson(dumpObject, path):
    with open(path, "w") as file:
        json.dump(dumpObject, file, indent=4)

busses = loadJson("bussbestilling/busses.json")
brukere = loadJson("bussbestilling/brukere.json")

# Legge til ny buss
def leggeTilBuss():
    buss = {
        "bussNavn": input("Skriv inn navn på bussen: "),
        "bussID": str(uuid.uuid4()),
        "antallSeter": int(input("Skriv antall passasjerer: ")),
        "ledig": True,
        "pris": int(input("Prisen på bussen per dag: ")),
    }
    busses.append(buss)
    dumpJson(busses, "bussbestilling/busses.json")
    print(f"Bussen {buss['bussNavn']} er lagt til!")

# Legge til bestilling
def leggeTilBestilling():
    bruker = {
        "fornavn": input("Skriv fornavnet ditt her: "),
        "etternavn": input("Skriv etternavnet ditt her: "),
        "antallPassasjerer": int(input("Skriv antall passasjerer: ")),
        "antallDagerLeie": int(input("Skriv antall dager bussen skal leies: ")),
        "totalDistanse": int(input("Skriv distanse av turen her i kilometer: ")),
        "valgtBuss": None,
        "bussID": busses["bussID"],
        "totalpris": None,
        "turFullført": False,
        "datoForBestilling": datetime.datetime.now().strftime("%c")
    }

    valgtBuss = input("Velg en buss (skriv navnet): ").lower()
    for buss in busses:
        if valgtBuss == buss["bussNavn"].lower():
            if bruker["antallPassasjerer"] > buss["antallSeter"]:
                print(f"Bussen {buss['bussNavn']} har ikke nok seter. Bestillingen ble ikke fullført.")
                return

            bruker["valgtBuss"] = buss["bussNavn"]
            bruker["totalpris"] = int(buss["pris"]) * bruker["antallDagerLeie"] + 90 * bruker["totalDistanse"]
            buss["ledig"] = False
            break

    else:
        print("Ugyldig bussvalg. Bestillingen ble ikke fullført.")
        return

    brukere.append(bruker)
    dumpJson(brukere, "bussbestilling/brukere.json")
    dumpJson(busses, "bussbestilling/busses.json")
    print(f"Bestilling for {bruker['fornavn']} {bruker['etternavn']} er lagt til!")

# se alle bestillinger
def seBestillinger():
    for bruker in brukere:
        print(bruker["valgtBuss"])

# slette bestillinger
def sletteBestilling():
    bussNavn = input("Navn på bussen: ").lower()
    bussFunnet = False

    for buss in busses:
        if buss["bussNavn"].lower() == bussNavn:
            buss["ledig"] = True
            bussFunnet = True
            print(f"Bussen '{buss['bussNavn']}' er nå satt som ledig.")
            break

    if not bussFunnet:
        print("Ingen buss med det navnet ble funnet i systemet.")
        return

    bestillingFunnet = False
    for bruker in brukere:
        if bruker["valgtBuss"].lower() == bussNavn:
            brukere.remove(bruker)
            bestillingFunnet = True
            print(f"Bestillingen for {bruker['fornavn']} {bruker['etternavn']} er slettet.")
            break

    if not bestillingFunnet:
        print("Ingen bestillinger ble funnet for denne bussen.")


    dumpJson(busses, "bussbestilling/busses.json")
    dumpJson(brukere, "bussbestilling/brukere.json")
    print("Bestillingen er fullført og slettet")

# Meny
def meny():
    print("-----------Hovedmeny----------")
    print("   1. Legg til ny buss")
    print("   2. Legg til ny bestilling")
    print("   3. se bestillinger")
    print("   4. fullføre bestillinger / fjerne bestillinger")
    print("   0. Avslutt")
    valg = input("Velg fra menyen: ")
    return valg

# Main
def main():
    run = True
    while run:
        valgt = meny()
        if valgt == "1":
            leggeTilBuss()
        elif valgt == "2":
            leggeTilBestilling()
        elif valgt == "3":
            seBestillinger()
        elif valgt == "4":
            sletteBestilling()
        elif valgt == "0":
            run = False
        else:
            print("Ugyldig valg, prøv igjen!")

main()
