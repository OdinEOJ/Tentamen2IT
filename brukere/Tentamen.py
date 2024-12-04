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


brukere = loadJson("brukere/lagring.json")
tildeltbuss = "tildeltBuss"

# funkjon for å lage nye brukere og sende de inn i json filen og lagre de inni en liste
def leggeTilBruker():
    bruker = {
        "fornavn": input("skriv fornavnet ditt her: "),
        "etternavn": input("skriv etternavnet ditt her: "),
        "antallPassasjerer": input("skriv telefon nummeret ditt her: "),
        "antallDagerLeie": input("skriv adressen din her: "),
        "totalDistanse": input("skriv epost her: "),
        "tildeltBuss": None,
        "totalpris": None,
        "datoForBestilling": datetime.datetime.now().strftime("%c")
        }
    brukere.append(bruker)
    dumpJson(brukere, "brukere/lagring.json")
    print(bruker["fornavn"] + ["etternavn"] + " har lagt inn en bestilling!")


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
            leggeTilBruker()
        elif(valgt == "2"):
            seBrukere()
        elif(valgt == "0"):
            run = False


# her kjører vi main funksjonen som gjør at man kan velge mellom de forskjellige funkjosnene
main()