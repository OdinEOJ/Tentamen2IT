import firebase_admin
from firebase_admin import credentials, firestore
import uuid
import json

cred = credentials.Certificate("quizmaskin/quizmaskin69-firebase-adminsdk-fbsvc-3673d7c29e.json")

firebase_admin.initialize_app(cred)
db = firestore.client()

def mellomrom(num):
    for i in range(num):
        print("")


docID = str(uuid.uuid4())



def leggTilEtSpørsmål():
    collection = str(input("Hvilken kategori er dette spørsmålet? (rarespørsmål, sport, generellespørsmål, MÅ SKRIVES HELT LIKT DU SER FØR!): "))
    doc_ref = db.collection(collection).document(docID)
    doc_ref.set({
        'spørsmål': input("spørsmålet: "),
        'kategori': input("kategori (rarespørsmål, sport, generellespørsmål): "),
        'svar': input("svaret (a,b,c,d eller hvis det er et vanskelighets grad vanskelig skriv inn svaret): "),
        'vanskelighetsgrad': input("vanskelighetsgrad (lett, middels, vanskelig): "),
    })
    mellomrom(1)
    print(f"Spørsmål med ID: {docID} er lagt til!")
    mellomrom(2)

def load_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

questions = load_json("quizmaskin/sportspørsmål.json")

# Funksjon for å sende spørsmålene til Firebase Firestore
def sendTilFirebase(questions):
    for question in questions:
        doc_id = str(uuid.uuid4())  # Unik ID for hvert spørsmål
        db.collection("sport").document(doc_id).set(question)
sendTilFirebase()


def printUtSpørsmålene():
    collection = input("Hvilken collection er dette spørsmålet i?: ")
    spørsmål_id = input("Legg til ID for å se spørsmålet: ")
    doc_ref = db.collection(collection).document(spørsmål_id)
    doc = doc_ref.get()
    if doc.exists:
        mellomrom(1)
        print(doc.id)
        print(doc.to_dict())
        mellomrom(1)
    else:
        print("Fant ikke dokumentet.")

def printUtAlleSpørsmålene():
    collection = input("Hvilken collection er dette spørsmålet i?: ")
    users = db.collection(collection).stream()

    for user in users:
        mellomrom(1)
        print(user.id)
        print(user.to_dict())
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
    collection = input("Hvilken collection er brukeren du vil endre i?: ")
    first_name = input("Hvilken bruker vil du slette?: ")
    
    if collection == "Lærere":
        doc_ref_Lærere = db.collection("Lærere").document(first_name)
        firstName = input("fornavn: ")
        lastName = input("etternavn: ")
        age = input("alder: ")

        fag = []
        while True:
            fag.append(input("Legg til fag: "))
            flereFag = input("Ønsker du å legge til flere fag? ja / nei: ")
            if(flereFag == "nei"):
                break

        doc_ref_Lærere.update({
        "firstName": firstName,
        "lastName": lastName,
        "fag": fag,
        "age": age
        })

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
        admin()

    else:
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
    

def second():
    run = True
    while run:
        valgt = admin()
        if valgt == "1":
            leggTilEtSpørsmål()
        elif valgt == "2":
            slettEtSpørsmål()
        elif valgt == "3":
            valgt = rediger()
        elif valgt == "4":
            valgt = printUtSpørsmålene()
        elif valgt == "5":
            valgt = printUtAlleSpørsmålene()
        elif valgt == "0":
            run = False

def main():
    run = True
    while run:
        valgt = meny()
        if valgt == "1":
            leggTilEtSpørsmål()
        elif valgt == "2":
            highscore()
        elif valgt == "3":
            valgt = adminpassord()
        elif valgt == "0":
            run = False
        
main()