# her importerer vi json så vi kan lese og sende ting til json filer
import json
# her importerer vi datetime så vi kan se akkurat når brukeren blir lagd
import datetime

# her leser vi fra json filen
def loadJson(path):
    with open(path, "r") as file:
        return json.load(file)

# her skriver vi til json filen
def dumpJson(dumpObject, path):
    with open(path, "w") as file:
        json.dump(dumpObject, file, indent=4)


brukere = loadJson("Brukere/lagring.json")

# funkjon for å lage nye brukere og sende de inn i json filen og lagre de inni en liste
def leggeTilBestilling():
    bruker = {
        "fornavn": input("skriv fornavnet ditt her: "),
        "etternavn": input("skriv etternavnet ditt her: "),
        "antallPassasjerer": input("skriv antall passasjerer: "),
        "antallDagerLeie": input("skriv antall dager bussen skal leies: "),
        "totalDistanse": input("skriv distanse av turen her i kilometer: "),
        "tildeltBuss": None,
        "totalpris": None,
        "turFullført": False,
        "datoForBestilling": datetime.datetime.now().strftime("%c")
        }
    brukere.append(bruker)
    dumpJson(brukere, "Brukere/lagring.json")
    print(bruker["fornavn"] + " har lagt inn en bestilling!")

tildeltbuss = "tildeltBuss"
antallPassjaserer = "antallPassasjerer"

busser = [
    {"antallSeter": 7, "antallBusser": 3, "prisPrDøgn": 1250, "kilometerPris": 90},
    {"antallSeter": 15, "antallBusser": 3, "prisPrDøgn": 1600, "kilometerPris": 90},
    {"antallSeter": 23, "antallBusser": 2, "prisPrDøgn": 1900, "kilometerPris": 90},
]

def finnBuss(antallPassjaserer):
    for bruker in busser:
        if antallPassjaserer <= "antallSeter":



# printer brukerne ved hjelp av en for loop som viser aller brukerne sine fornavn for seg selv
def seBrukere():
    for bruker in brukere:
        print(bruker["fornavn"])


# meny er bare hva de forskjellige funksjonene gjør
def meny():
    print("-----------Hovedmeny----------")
    print("   1. legg til bruker")
    print("   2. se brukere")
    print("   0. avslutt")
    valg = input("velg fra menyen: ")
    return valg

# main gjør så jeg kan velge mellom å kjøre de forskjellige funkjonene til koden
def main():
    run = True
    while run:
        valgt = meny()
        if(valgt == "1"):
            leggeTilBestilling()
        elif(valgt == "2"):
            seBrukere()
        elif(valgt == "0"):
            run = False
        else:
            print("Ugyldig valg, prøv igjen!")


# her kjører vi main funksjonen som gjør at man kan velge mellom de forskjellige funkjosnene
main()