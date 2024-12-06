import json  # For å lese og skrive JSON-filer
import uuid  # For å generere unike ID-er for busser
import datetime  # For å få dato og tid


def loadJson(path):
    with open(path, "r") as file:  # Åpner filen i lesemodus, dette er pga "r"
        return json.load(file)  # Returnerer innholdet som et Python-objekt

# Funksjon for å skrive data til JSON filer
def dumpJson(dumpObject, path):
    with open(path, "w") as file:  # Åpner filen i skrivemodus, dette er pga "w"
        json.dump(dumpObject, file, indent=4)  # Skriver objeket til fil med 4 mellomrom for innrykk


# Laster inn eksisterende busser og bestillinger lister fra JSONfiler
busser = loadJson("HTSpelle/busser.json")
bestillinger = loadJson("HTSpelle/bestillinger.json")


#### KOMMENTAR FOR FUNKSJONEN: bestill_buss() ######
# 1. Jeg ser du bruker print("") for å gjøre menyen og valgene mer lesbar, 
# det er flott, men kanskje man kunne laget en funksjon for å lage antall mellomrom mellom linjene man ønsker?           OK
def mellomrom(num):
    for i in range(num):
        print("")

# 2. bestillingsId bør være en autogenerert id, ikke en id vi skirver inn selv            OK
# Her bruker vi uuid som lager randome ider for oss (se linje 59)

# 3. Vi bør heller ikke skrive inn id for tildelt buss selv. kunden bør automatisk få tildelt en ledig buss som passer antall passasjerer.   fikk desverre ikke tid.
#    Husk at vi også må hondter sitvasjoner der det ikke er ledige busser som passer antall passasjerer

# 4. koden krasjer når vi prøver å legge sammen totalPris, dette må rettes.            OK

# 5. er det noe vi kan gjøre for å hondtere eventuelle feil som oppstår hvis bruker skriver inn ugyldige verdier i input?          OK  (try og except)

# 6. Det mangler dato for når bestillingen ble opprettet.        OK   (datetime)


def bestill_buss():
    try:
        mellomrom(2)
        kundeNavn = input("Skriv inn navn på kunde: ")
        antall = int(input("Antall passasjerer: "))
        dager = int(input("Hvor mange dager skal bussen leies: "))
        distanse = int(input("Antall forventet km: "))

        
        mellomrom(1)
        tildeltBuss = input("skriv inn id på ønsket buss: ")

    except:
        print("En feil skjedde, husk det skal kun hele tall inn i (antall, dager og distanse)")
        meny()
        mellomrom(1)

    nyBestilling = {
        "bestillingsId": str(uuid.uuid4()),
        "bussId": tildeltBuss,
        "kontaktPerson": kundeNavn,
        "passasjerer": antall,
        "dager": dager,
        "distanse": distanse,
        "totalPris": None,
        "datoForBestilling": datetime.datetime.now().strftime("%c")
    }

    for buss in busser:
        if buss == tildeltBuss:
            bestillinger["tildeltbuss"] = buss["bussID"]
            

    nyBestilling["totalPris"] = int(buss["pris"]) * nyBestilling["dager"] + 90 * nyBestilling["distanse"]
    

    bestillinger.append(nyBestilling)
    dumpJson(bestillinger, "HTSpelle/bestillinger.json")
    dumpJson(busser, "HTSpelle/busser.json")
    mellomrom(4)
    print("Gratulerer bestillingen ble fullført, hva ønsker du å gjøre nå?")
    mellomrom(1)


def meny():
    print("1. Bestill busstur")
    print("2. List ut bestilte bussturer")
    print("3. avslutt busstur")
    print("0. avslutt")
    return int(input("velg ett nummer fra menyen: "))


# funksjonen printer ut alle bestillinger som hele dictionary.
# Formatter printen så den er mer lesbar for en vanlig bruker.          OK

def list_ut_bestillinger():
    print("Her er alle allerede bestillte turer: ")
    for bestilling in bestillinger:
        print(f"{bestilling['kontaktPerson']}:  {bestilling['bestillingsId']}")

# Denne funksjonen må fullføres, det beste er om man bare kan skrive inn navn på kontaktpersonen som man ønsker å avslutte turen til
def avslutt_tur():
    kontaktPerson = input("Navn på kontakt person: ").lower()
    bussFunnet = False

    for buss in busser:
        kontaktPerson = buss["bussID"]
        if buss["bussID"].lower() == kontaktPerson:
            buss["ledig"] = True
            bussFunnet = True
            print(f"Bussen '{buss['bussID']}' er nå satt som ledig.")
            break

    if not bussFunnet:
        print("Ingen med det navnet ble funnet i systemet.")
        return
    
    # det over fungerer, trengte lengere tid

    bestillingFunnet = False
    for bestilling in bestillinger:     # vil ikke fungere fordi jeg åpner bestillinger og den har ikke tilgang på bussID
        kontaktPerson = buss["bussID"]
        if bestilling["kontaktPerson"].lower() == kontaktPerson:
            bestillinger.remove(bestilling)
            bestillingFunnet = True
            print(f"Bestillingen for {bestilling['kontaktPerson']} er slettet.")
            break

    if not bestillingFunnet:
        print("Ingen bestillinger ble funnet for denne personen.")

    dumpJson(busser, "HTSpelle/busser.json")
    dumpJson(bestillinger, "HTSpelle/bestillinger.json")
    print("Bestillingen er fullført og slettet.")
    mellomrom(1)

def main():
    while True:
        valg = meny()
        # er dette beste måten å sett opp if-setninger?
        if valg == 0:
            break
        elif valg == 1:
            bestill_buss()
        elif valg == 2:
            list_ut_bestillinger()
        elif valg == 3:
            avslutt_tur()


main()
