import firebase_admin
from firebase_admin import credentials, firestore
import uuid
import random

########################################################################################

cred = credentials.Certificate("quizmaskin/quizmaskin69-firebase-adminsdk-fbsvc-b15bac77b6.json")

firebase_admin.initialize_app(cred)
db = firestore.client()

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
        "3": "rarespørsmål"
    }

    temaSvar = input("Velg et tema for quiz: ").strip()
    tema = temaValg.get(temaSvar)
    if not tema:
        print("Ugyldig valg av tema.")
        return

    for i in range(5):  # Kjør quizen 5 ganger

        try:
            print(f"Henter spørsmål fra kategori: {tema}")  # Debugging-print
            dokumenter = list(db.collection(tema).stream())
            
            spørsmålsliste = [doc.to_dict() for doc in dokumenter if doc.to_dict().get("vanskelighetsgrad") == vanskelighetsgrad]
            
            if not spørsmålsliste:
                print("Fant ingen spørsmål med valgt vanskelighetsgrad og tema.")
                continue

            # Velg et tilfeldig spørsmål fra listen
            spørsmål = random.choice(spørsmålsliste)

            # Vis spørsmålet og svaralternativer
            print("Spørsmål:", spørsmål['spørsmål'])
            
            svaralternativer = spørsmål.get('svar', None)  

            if isinstance(svaralternativer, dict):  # Bare loop hvis det faktisk er en ordbok
                for key, value in svaralternativer.items():
                    print(f"{key.upper()}: {value}")
                svar = input("Ditt svar (a, b, c, d): ").strip().lower()
            else:
                svar = input("Skriv inn svaret ditt: ").strip().lower()

            if svar == spørsmål['riktig_svar']:
                print("Rett! +10 poeng")
                highscore += 10
            else:
                if isinstance(svaralternativer, dict):
                    print(f"Feil, riktig svar var: {spørsmål['riktig_svar'].upper()} Eller {svaralternativer.get(spørsmål['riktig_svar'], '')}")
                else:
                    print(f"Feil, riktig svar var: {spørsmål['riktig_svar'].upper()}")
        
        except Exception as e:
            print(f"En feil skjedde: {e}. Prøv på nytt.")
            continue

    print(f"Quizen er ferdig! Din høyeste poengsum var: {highscore}")
    HighscoreNavn = input("Skriv inn navn så vi kan lagre highscore: ")


########################################################################################

def printUtAlleSpørsmålene():
    collection = input("Hvilken kategori vil du liste ut spørsmål fra?: ")
    users = db.collection(collection).stream()

    for user in users:
        mellomrom(1)
        print(f"Dokument-ID: {user.id}")
        mellomrom(1)



def slettEtSpørsmål():
    collection = input("Hvilken collection er dette spørsmålet i?: ")
    spørsmål_grrr = input("Hvilket spørsmål vil du slette?: ")

    users = db.collection(collection).where('spørsmål', '==', spørsmål_grrr).stream()
    deleted_count = False

    for user in users:
        db.collection(collection).document(user.id).delete()
        print(f"Slettet spørsmålet: '{spørsmål_grrr}' med ID: {user.id}")
        deleted_count = True

    if deleted_count == False:
        print(f"Finner ingen spørsmål med: '{spørsmål_grrr}'")


def rediger():
    collection = input("Hvilken collection er spørsmålet du vil endre i?: ")
    user_id = input("Hvilket spørsmål vil du redigere?: ")
    
    doc_ref = db.collection(collection).document(user_id)
    if not doc_ref.get().exists:
        print(f"spørsmålet med ID {user_id} finnes ikke.")
        return

    spørsmål = input("spørsmål: ")
    kategori = input("kategori: ")
    svar = input("svar: ")
    vanskelighetsgrad = input("vanskelighetsgrad: ")

    doc_ref.update({
        "spørsmål": spørsmål,
        "kategori": kategori,
        "svar": svar,
        "vanskelighetsgrad": vanskelighetsgrad
    })
    print("spørsmålet er oppdatert!")



def meny():
    print("-----------Quizmaskin----------")
    print("        1. Start quiz")
    print("        2. se highscores")
    print("        3. Admin")
    print("        0. Avslutt")
    valg = input("Velg fra menyen: ")
    return valg

def adminpassord():
    password = "6969"
    passord = input("Skriv inn admin passord: ")
    
    if passord == password:
        adminValg()
    else:
        print("Feil passord!")
        mellomrom(1)
        meny()

def admin():
    print("-----------Quizmaskin-Admin----------")
    print("        1. legg til et spørsmål")
    print("        2. slett et spørsmål")
    print("        3. rediger et av spørsmålene")
    print("        4. print et spørsmål")
    print("        5. print ut alle spørsmålene")
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
        elif valgt == "4":
            pass
        elif valgt == "5":
            valgt = printUtAlleSpørsmålene()
        elif valgt == "0":
            run = False

def main():
    run = True
    while run:
        valgt = meny()
        if valgt == "1":
            startQuiz()
        elif valgt == "2":
            pass
        elif valgt == "3":
            valgt = adminpassord()
        elif valgt == "0":
            run = False
        
main()