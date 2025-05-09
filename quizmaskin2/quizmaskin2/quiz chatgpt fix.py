import firebase_admin
from firebase_admin import credentials, firestore
import random

# Koble til databasen
try:
    cred = credentials.Certificate("quizmaskin2/quizmaskin69-firebase-adminsdk-fbsvc-9e07390b6a.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    print("Tilkoblet til databasen!")
except:
    print("Feil ved tilkobling til Firebase: ")
    exit()

def StartQuiz():
    poengsum = 0
    vanskelighetsgradValg = {"1": "Lett", "2": "Medium", "3": "Vanskelig"}
    print("Velg vanskelighetsgrad:")
    for key, value in vanskelighetsgradValg.items():
        print(f"{key}. {value}")
    vanskelighetsgrad = vanskelighetsgradValg.get(input("Ditt valg: ").strip())
    if not vanskelighetsgrad:
        print("Ugyldig valg.")
        return
    
    temaValg = {"1": "sport", "2": "generell", "3": "spesiell"}
    print("Velg tema:")
    for key, value in temaValg.items():
        print(f"{key}. {value.capitalize()}")
    tema = temaValg.get(input("Ditt valg: ").strip())
    if not tema:
        print("Ugyldig valg.")
        return
    
    try:
        spørsmålRef = db.collection(tema).stream()
        spørsmålListe = [doc.to_dict() for doc in spørsmålRef if doc.to_dict().get("vanskelighetsgrad") == vanskelighetsgrad]
        if len(spørsmålListe) < 5:
            print("Ikke nok spørsmål tilgjengelig.")
            return
        
        valgteSpørsmål = random.sample(spørsmålListe, 5)
        for spm in valgteSpørsmål:
            print("Spørsmål:", spm['spørsmål'])
            if isinstance(spm.get('svar'), dict):
                for key, value in spm['svar'].items():
                    print(f"{key.upper()}: {value}")
                svar = input("Ditt svar (a, b, c, d): ").strip().lower()
            else:
                svar = input("Skriv inn svaret ditt: ").strip().lower()
            
            if svar == spm['riktig_svar'].lower():
                print("Riktig! +10 poeng")
                poengsum += 10
            else:
                print(f"Feil! Riktig svar var: {spm['riktig_svar'].upper()}")
    
    except:
        print("En feil oppstod: ")
    
    print(f"Quizen er ferdig! Din poengsum: {poengsum}")
    navn = input("Skriv inn navn for å lagre highscore: ").strip()
    db.collection("highscore").document(navn).set({"navn": navn, "highscore": poengsum})

def VisTopHighscores():
    print("Topp 5 highscores:")
    try:
        brukere = db.collection("highscore").order_by("highscore", direction=firestore.Query.DESCENDING).limit(5).stream()
        for i, bruker in enumerate(brukere, start=1): #enumerate brukes til å holde telling i index
            data = bruker.to_dict()
            print(f"{i}. {data.get('navn', 'Ukjent')}: {data.get('highscore', 0)} poeng")
    except:
        print("En feil oppstod ved henting av highscores.")

def SlettSpørsmål():
    tema = input("Hvilken kategori er spørsmålet i?: ").strip()
    spørsmålstekst = input("Hvilket spørsmål vil du slette?: ").strip()
    try:
        spørsmål = db.collection(tema).where("spørsmål", "==", spørsmålstekst).stream()
        slettet = False
        for spm in spørsmål:
            db.collection(tema).document(spm.id).delete()
            print(f"Spørsmålet '{spørsmålstekst}' er slettet.")
            slettet = True
        if not slettet:
            print("Fant ikke spørsmålet.")
    except:
        print("En feil oppstod: ")

def AdminMeny():
    print("Admin-meny:")
    print("1. Slett et spørsmål")
    print("2. Vis highscores")
    print("0. Tilbake til hovedmeny")
    valg = input("Velg et alternativ: ")
    if valg == "1":
        SlettSpørsmål()
    elif valg == "2":
        VisTopHighscores()
    elif valg == "0":
        return
    else:
        print("Ugyldig valg.")

def Hovedmeny():
    while True:
        print("--- Quizmaskin ---")
        print("1. Start quiz")
        print("2. Se highscores")
        print("3. Admin-meny")
        print("0. Avslutt")
        valg = input("Velg et alternativ: ")
        if valg == "1":
            StartQuiz()
        elif valg == "2":
            VisTopHighscores()
        elif valg == "3":
            AdminMeny()
        elif valg == "0":
            print("Avslutter programmet...")
            break
        else:
            print("Ugyldig valg, prøv igjen.")

Hovedmeny()


# psudokode
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