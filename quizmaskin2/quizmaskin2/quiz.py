######################################################################################## import av alle funksjonene som ikke kommer standard i python

import firebase_admin
from firebase_admin import credentials, firestore
import uuid
import random

######################################################################################## koble til databasen og noen universale variabler og funksjoner

try:
    cred = credentials.Certificate("quizmaskin2/quizmaskin69-firebase-adminsdk-fbsvc-9e07390b6a.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    print("Koblet til databasen!")
except:
    print("Feil ved tilkobling til Firebase!")
    run = False


def mellomrom(num): #formatere output sånn at programmet blir lettere å lese
    for i in range(num):
        print("")

docID = str(uuid.uuid4())

######################################################################################## funksjon for å starte quizen

def startQuiz():

    highscore = 0

    print("1. Lett")
    print("2. Medium")
    print("3. Vanskelig")
    vanskelighetsgradSvar = input("Velg vanskelighetsgrad du vil spille på: ").strip()

    vanskelighetsgradValg = {
        "1": "Lett",
        "2": "Medium",
        "3": "Vanskelig"
    }

    vanskelighetsgrad = vanskelighetsgradValg.get(vanskelighetsgradSvar)
    if not vanskelighetsgrad:
        print("Ugyldig valg av vanskelighetsgrad.")
        return

    print("1. Sport")
    print("2. Generell")
    print("3. Spesiell")

    temaValg = {
        "1": "sport",
        "2": "generell",
        "3": "rar"
    }

    temaSvar = input("Velg et tema for quiz: ").strip()
    tema = temaValg.get(temaSvar)
    if not tema:
        print("Ugyldig valg av tema.")
        return

    try:
        print(f"Kategori: {tema}")  # Debugging-print
        dokumenter = list(db.collection(tema).stream())
        
        spørsmålsliste = [doc.to_dict() for doc in dokumenter if doc.to_dict().get("vanskelighetsgrad") == vanskelighetsgrad]

        if len(spørsmålsliste) < 5:
            print("Ikke nok spørsmål tilgjengelig for å spille 5 runder.")
            return

        # Bruk `random.sample()` for å velge 5 unike spørsmål
        valgte_spørsmål = random.sample(spørsmålsliste, 5)

        for spørsmål in valgte_spørsmål:

            # Vis spørsmålet og svaralternativer
            print("Spørsmål:", spørsmål['spørsmål'])
            
            svaralternativer = spørsmål.get('svar', None)  

            if isinstance(svaralternativer, dict):  # Bare loop hvis det faktisk er en ordbok
                for key, value in svaralternativer.items():
                    print(f"{key.upper()}: {value}")
                svar = input("Ditt svar (a, b, c, d): ").strip().lower()
            else:
                svar = input("Skriv inn svaret ditt: ").strip().lower()

            if svar == spørsmål['riktig_svar'].lower():
                print("Rett! +10 poeng")
                highscore += 10
            else:
                if isinstance(svaralternativer, dict):
                    print(f"Feil, riktig svar var: {spørsmål['riktig_svar'].upper()} Eller {svaralternativer.get(spørsmål['riktig_svar'], '')}")
                else:
                    print(f"Feil, riktig svar var: {spørsmål['riktig_svar'].upper()}")
    
    except:
        print(f"En feil skjede, igjen.")

    print(f"Quizen er ferdig! Din høyeste poengsum var: {highscore}")
    highscoreNavn = str(input("Skriv inn navn så vi kan lagre highscore: ").lower())

    doc_ref = db.collection("highscore").document(highscoreNavn)
    doc_ref.set({
        'firstName': highscoreNavn,
        'highscore': highscore
    })

######################################################################################## printe ut highscore (bare de 5 beste scorene)

def printTopHighscores():
    print("Topp 5 highscores:")

    users = db.collection("highscore").order_by("highscore", direction=firestore.Query.DESCENDING).limit(5).stream()

    top_scores = []
    for user in users:
        data = user.to_dict()
        top_scores.append((data.get('firstName', 'Ukjent'), data.get('highscore', 0)))

    if not top_scores:
        print("En feil skjedde, prøv på nytt")
        return

    for index, (name, score) in enumerate(top_scores, start=1):
        print(f"{index}. {name}: {score} poeng")

######################################################################################## slett et spørsmål (fungerer ikke)

def slettEtSpørsmål():
    collection = input("Hvilken collection er dette spørsmålet i?: ").strip()
    spørsmål_grrr = input("Hvilket spørsmål vil du slette?: ").strip()

    print(f"Spørsmål som skal slettes: {spørsmål_grrr}")
    
    try:
        users = db.collection(collection).filter('spørsmål', '==', spørsmål_grrr).stream()

        deleted_count = 0
        for user in users:
            db.collection(collection).document(user.id).delete()
            print(f"Slettet spørsmålet: '{spørsmål_grrr}' med ID: {user.id}")
            deleted_count += 1

        if deleted_count == 0:
            print(f"Ingen spørsmål funnet med teksten: '{spørsmål_grrr}'.")

    except:
        print(f"En feil oppstod!")

######################################################################################## redigering av et spørsmål

def rediger():
    collection = input("Hvilken collection er spørsmålet du vil endre i?: ")
    user_id = input("Hvilket spørsmål vil du redigere?: ")
    
    doc_ref = db.collection(collection).document(user_id)
    doc = doc_ref.get()

    if not doc.exists:
        print(f"Spørsmålet med ID {user_id} finnes ikke.")
        return

    data = doc.to_dict()
    
    # Sikkerhetskopi av eksisterende verdier
    spørsmål = input(f"Spørsmål (nåværende: {data.get('spørsmål', 'Ingen')}): ") or data.get('spørsmål', 'Ingen')
    kategori = input(f"Kategori (nåværende: {data.get('kategori', 'Ingen')}): ") or data.get('kategori', 'Ingen')
    vanskelighetsgrad = input(f"Vanskelighetsgrad (nåværende: {data.get('vanskelighetsgrad', 'Ingen')}): ") or data.get('vanskelighetsgrad', 'Ingen')

    # Hent eksisterende svar eller en tom dictionary
    svar = data.get('svar', {})

    if isinstance(svar, dict):  # Bare oppdater svar hvis det er en dict
        for option in ['a', 'b', 'c', 'd']:  
            svar[option] = input(f"Answer for {option.upper()} (nåværende: {svar.get(option, '')}): ") or svar.get(option, '')

    riktig_svar = input(f"Riktig svar (nåværende: {data.get('riktig_svar', 'Ingen')}): ") or data.get('riktig_svar', 'Ingen')

    forklaring = ""
    if vanskelighetsgrad == "Vanskelig":
        forklaring = input(f"Forklaring på riktig svar (valgfritt, nåværende: {data.get('forklaring', '')}): ") or data.get('forklaring', '')

    # Oppdater Firestore
    oppdatert_data = {
        "spørsmål": spørsmål,
        "kategori": kategori,
        "svar": svar,
        "riktig_svar": riktig_svar,
        "vanskelighetsgrad": vanskelighetsgrad
    }

    if vanskelighetsgrad == "Vanskelig":
        oppdatert_data["forklaring"] = forklaring

    doc_ref.update(oppdatert_data)
    
    print("Spørsmålet er oppdatert!")

######################################################################################## logge på admin menyen sånn at man kan gjøre administrative oppgaver fra programmet

def adminpassord(): #admin sånn at man kan skifte på ting man normalt ikke kunne ha gjort
    password = "6969" #passordet
    for i in range(3): #den kjører 3 ganger før den stopper
        passord = input("Skriv inn admin passord: ")
        if passord == password:
            adminValg()
            return
        else:
            print("Feil passord! Prøv igjen.")
    print("For mange feil forsøk. Tilbake til hovedmenyen.")


def meny(): #meny
    print("-----------Quizmaskin----------")
    print("        1. Start quiz")
    print("        2. se highscores")
    print("        3. Admin")
    print("        0. Avslutt")
    valg = input("Velg fra menyen: ")
    return valg


def admin(): #admin meny
    print("-----------Quizmaskin-Admin----------")
    print("        1. legg til et spørsmål")
    print("        2. slett et spørsmål")
    print("        3. rediger et spørsmål")
    print("        0. Avslutt")
    valg = input("Velg fra menyen: ")
    return valg
    

def adminValg(): #utvalg av admin funksjoner
    run = True
    while run:
        valgt = admin()
        if valgt == "1":
            pass
        elif valgt == "2":
            slettEtSpørsmål()
        elif valgt == "3":
            valgt = rediger()
        elif valgt == "0":
            run = False


def main(): #utvalg av funksjoner
    run = True
    while run:
        valgt = meny()
        if valgt == "1":
            startQuiz()
        elif valgt == "2":
            printTopHighscores()
        elif valgt == "3":
            valgt = adminpassord()
        elif valgt == "0":
            run = False
        
main()


#peudokode
# --------------------------------------------
# HOVEDMENY
# --------------------------------------------
# 1. Vis menyvalg:
#    - 1: Start quiz
#    - 2: Se highscores
#    - 3: Admin-meny
#    - 0: Avslutt
# 2. Brukeren velger et alternativ
# 3. Kjør tilsvarende funksjon

# --------------------------------------------
# START QUIZ
# --------------------------------------------
# 1. Be brukeren velge vanskelighetsgrad
# 2. Be brukeren velge et tema
# 3. Hent spørsmål fra databasen basert på valgene
# 4. Hvis det er nok spørsmål, velg 5 tilfeldige
# 5. For hvert spørsmål:
#    - Vis spørsmålet og eventuelle svaralternativer
#    - Brukeren skriver inn svaret
#    - Sjekk om svaret er riktig og oppdater poengsum
# 6. Etter quizen, vis sluttresultatet
# 7. Be brukeren skrive inn navn for å lagre poengsummen

# --------------------------------------------
# VIS HIGHSCORES
# --------------------------------------------
# 1. Hent de 5 beste highscore-oppføringene fra databasen
# 2. Skriv ut resultatene i synkende rekkefølge

# --------------------------------------------
# ADMIN-MENY
# --------------------------------------------
# 1. Vis menyvalg:
#    - 1: Slett et spørsmål
#    - 2: Vis highscores
#    - 0: Tilbake
# 2. Brukeren velger et alternativ
# 3. Utfør tilsvarende handling

# --------------------------------------------
# SLETT SPØRSMÅL
# --------------------------------------------
# 1. Be brukeren oppgi kategori og spørsmålstekst
# 2. Søk i databasen etter spørsmålet
# 3. Hvis funnet, slett det
# 4. Bekreft slettingen eller gi feilmelding