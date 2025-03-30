import firebase_admin
from firebase_admin import credentials, firestore
import uuid
import random

########################################################################################

try:
    cred = credentials.Certificate("quizmaskin2/quizmaskin2/quizmaskin69-firebase-adminsdk-fbsvc-a628be7fd3.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
except Exception as e:
    print("Feil ved tilkobling til Firebase:", e)
    exit()


def mellomrom(num):
    for i in range(num):
        print("")

docID = str(uuid.uuid4())

########################################################################################

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
        print(f"En feil skjedde, prøv på nytt.")

    print(f"Quizen er ferdig! Din høyeste poengsum var: {highscore}")
    highscoreNavn = str(input("Skriv inn navn så vi kan lagre highscore: ").lower())

    doc_ref = db.collection("highscore").document(highscoreNavn)
    doc_ref.set({
        'firstName': highscoreNavn,
        'highscore': highscore
    })

########################################################################################

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

########################################################################################

def slettEtSpørsmål():
    collection = input("Hvilken collection er dette spørsmålet i?: ")
    spørsmål_grrr = input("Hvilket spørsmål vil du slette?: ")

    print(f"Spørsmål som skal slettes: {spørsmål_grrr}")  # Debugging print
    
    try:
        # Query for all documents that match the question text
        users = db.collection(collection).where('spørsmål', '==', spørsmål_grrr).stream()
        deleted_count = 0  # Initialize a counter to track the number of deleted questions

        for user in users:
            # Delete the question (document) if found
            db.collection(collection).document(user.id).delete()
            print(f"Slettet spørsmålet: '{spørsmål_grrr}' med ID: {user.id}")
            deleted_count += 1  # Increment the counter for each deleted document

        # If no question was deleted, notify the user
        if deleted_count == 0:
            print(f"Finner ingen spørsmål med: '{spørsmål_grrr}'")
        else:
            print(f"Totalt {deleted_count} spørsmål ble slettet.")
    except Exception as e:
        print(f"En feil oppstod: {e}")

########################################################################################

def rediger():
    collection = input("Hvilken collection er spørsmålet du vil endre i?: ")
    user_id = input("Hvilket spørsmål vil du redigere?: ")
    
    doc_ref = db.collection(collection).document(user_id)
    if not doc_ref.get().exists:
        print(f"Spørsmålet med ID {user_id} finnes ikke.")
        return

    # Fetch the current data from Firestore
    data = doc_ref.get().to_dict()
    
    # Get the question, category, and difficulty with default values
    spørsmål = input(f"Spørsmål (nåværende: {data['spørsmål']}): ") or data['spørsmål']
    kategori = input(f"Kategori (nåværende: {data['kategori']}): ") or data['kategori']
    
    vanskelighetsgrad = input(f"Vanskelighetsgrad (nåværende: {data['vanskelighetsgrad']}): ") or data['vanskelighetsgrad']
    
    # Safely get the 'svar' field, defaulting to an empty dictionary if it doesn't exist
    svar = data.get('svar', {})

    # If the difficulty level is 'Lett' or 'Medium', we'll handle the answers accordingly
    if vanskelighetsgrad in ['Lett', 'Medium']:  # For Lett and Medium difficulty levels
        for option in ['a', 'b', 'c', 'd']:  # Assuming 4 answer options
            answer = input(f"Answer for {option.upper()} (nåværende: {svar.get(option, '')}): ") or svar.get(option, '')
            svar[option] = answer
        
        riktig_svar = input(f"Riktig svar (nåværende: {data['riktig_svar']}): ") or data['riktig_svar']

    elif vanskelighetsgrad == "Vanskelig":  # For "Vanskelig" difficulty level
        for option in ['a', 'b', 'c', 'd']:  # Assuming 4 answer options
            answer = input(f"Answer for {option.upper()} (nåværende: {svar.get(option, '')}): ") or svar.get(option, '')
            svar[option] = answer

        # For "Vanskelig" difficulty, we need to gather an explanation for the correct answer
        riktigsvar = input(f"Riktig svar (nåværende: {data['riktig_svar']}): ") or data['riktig_svar']
        forklaring = input(f"Forklaring på riktig svar (valgfritt): ")

    # Now, update the Firestore document with the new data
    doc_ref.update({
        "spørsmål": spørsmål,
        "kategori": kategori,
        "svar": svar,
        "riktig_svar": riktigsvar,  # Depending on difficulty, this will vary
        "vanskelighetsgrad": vanskelighetsgrad,
        "forklaring": forklaring if vanskelighetsgrad == "Vanskelig" else None
    })
    
    print("Spørsmålet er oppdatert!")

########################################################################################

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
    

def adminValg():
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


def main():
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