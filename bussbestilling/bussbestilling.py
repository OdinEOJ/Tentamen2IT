import json
import uuid
import datetime

def loadJson(path):
    with open(path, "r") as file:
        return json.load(file)

# skrive ting til json
def dumpJson(dumpObject, path):
    with open(path, "w") as file:
        json.dump(dumpObject, file, indent=4)

busses = loadJson("bussbestilling/busses.json")
brukere = loadJson("bussbestilling/brukere.json")

#legge til buss
def leggeTilBuss():
    buss = {
        "bussNavn": input("skriv inn navn på bussen: "),
        "bussID": str(uuid.uuid4()),
        "antallSeter": input("skriv antall passasjerer: "),
        "ledig": True,
        "pris": input("prisen på bussen: "),
        }
    busses.append(buss)
    dumpJson(busses, "bussbestilling/busses.json")


#bestille buss
def leggeTilBestilling():
    bruker = {
        "fornavn": input("skriv fornavnet ditt her: "),
        "etternavn": input("skriv etternavnet ditt her: "),
        "antallPassasjerer": input("skriv antall passasjerer: "),
        "antallDagerLeie": input("skriv antall dager bussen skal leies: "),
        "totalDistanse": input("skriv distanse av turen her i kilometer: "),
        "valgtBuss": input("hvilken buss som skal kjøre: "),
        "totalpris": valgtBuss["pris"] * "antallDagerleie" + 90 * "totalDistanse",
        "turFullført": False, 
        "datoForBestilling": datetime.datetime.now().strftime("%c")
        }
    if bruker("antallPassasjerer") > busses["antallSeter"]:
        print("nuh uh")
    elif bruker("antallPassasjerer") <= busses["antallSeter"]:
        print(bruker["fornavn"] + " har lagt inn en bestilling!")
        print(bruker["totalpris"])
    brukere.append(bruker)
    dumpJson(brukere, "Brukere/lagring.json")


#meny
def meny():
    print("-----------Hovedmeny----------")
    print("   1. legg til bruker")
    print("   2. legge til bestilling")
    print("   0. avslutt")
    valg = input("velg fra menyen: ")
    return valg

# main gjør så jeg kan velge mellom å kjøre de forskjellige funkjonene til koden
def main():
    run = True
    while run:
        valgt = meny()
        if(valgt == "1"):
            leggeTilBuss()
        elif(valgt == "2"):
            leggeTilBestilling()
        elif(valgt == "0"):
            run = False
        else:
            print("Ugyldig valg, prøv igjen!")

main()