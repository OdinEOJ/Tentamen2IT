import firebase_admin
import uuid
from firebase_admin import credentials, firestore

cred = credentials.Certificate("database/mongodb-c9c44-firebase-adminsdk-t0fim-9f731cb975.json")

firebase_admin.initialize_app(cred)


db = firestore.client()

firstName = 'firstName'

def leggTilEnBruker():
    collection = str(input("Hvor vil du legge til brukeren?: "))
    docID = str(uuid.uuid4())
    doc_ref = db.collection(collection).document(docID)
    doc_ref.set({
        'firstName': input("Fornavn: "),
        'lastName': input("Etternavn: "),
        'age': int(input("Alder: ")),
        'class': input("Klasse: "),
    })
    print(f"Bruker med ID: {docID} er lagt til!")


def printBrukerInfo():
    collection = str(input("Hvilken collection er denne brukeren i?: "))
    first_name = input("Legg til dokument ID for å se bruker: ")
    users = db.collection(collection).where('firstName', '==', first_name).stream()
    for user in users:
        print(user.id)
        print(user.to_dict())
    

def slettEnBruker():
    collection = input("Hvilken collection er denne brukeren i?: ")
    first_name = input("Hvilken bruker vil du slette?: ")

    users = db.collection(collection).where('firstName', '==', first_name).stream()
    deleted_count = False

    for user in users:
        db.collection(collection).document(user.id).delete()
        print(f"Slettet bruker med navnet: '{first_name}' og ID: {user.id}")
        deleted_count = True

    if deleted_count == False:
        print(f"Finner ingen bruker med navnet '{first_name}'")

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

    elif collection == "Elever":
        doc_ref_Elever = db.collection("Elever").document(first_name)
        firstName = input("fornavn: ")
        lastName = input("etternavn: ")
        klasse = input("klasse: ")
        age = input("alder: ")
    
        doc_ref_Elever.update({
            "firstName": firstName,
            "lastName": lastName,
            "klasse": klasse,
            "age": age
        })


def meny():
    print("-----------Hovedmeny----------")
    print("   1. Legg til ny bruker")
    print("   2. Slett en bruker")
    print("   3. Se bruker")
    print("   4. rediger bruker")
    print("   0. Avslutt")
    valg = input("Velg fra menyen: ")
    return valg

def main():
    run = True
    while run:
        valgt = meny()
        if valgt == "1":
            leggTilEnBruker()
        elif valgt == "2":
            slettEnBruker()
        elif valgt == "3":
            printBrukerInfo()
        elif valgt == "4":
            rediger()
        elif valgt == "0":
            run = False
        
main()