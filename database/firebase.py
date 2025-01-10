import firebase_admin
import uuid
from firebase_admin import credentials, firestore

# Path to your service account key
cred = credentials.Certificate("database/mongodb-c9c44-firebase-adminsdk-t0fim-abd6cc14b3.json")

# Initialize Firestore
firebase_admin.initialize_app(cred)

# Reference the Firestore database
db = firestore.client()

firstName = 'firstName'

def leggTilEnBruker():
    collection = str(input("Hvor vil du legge til brukeren?: "))
    docID = str(uuid.uuid4())
    doc_ref = db.collection(collection).document(docID)
    doc_ref.set({
        'firstName': input("Student first name: "),
        'lastName': input("Student last name: "),
        'age': int(input("Student age: ")),
        'class': input("Student class: "),
    })
    print(f"User added with ID: {docID}")


def printBrukerInfo():
    collection = str(input("Hvilken collection er denne brukeren i?: "))
    doc_id = input("Enter the document ID to view: ")
    doc = db.collection(collection).document(doc_id).get()
    if doc.exists:
        print(f"Her er brukeren du lette etter: {doc.to_dict()}")
    else:
        print("Finner ingen bruker med denne id!")


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


def meny():
    print("-----------Hovedmeny----------")
    print("   1. Legg til ny bruker")
    print("   2. Slett en bruker")
    print("   3. Se bruker")
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
        elif valgt == "0":
            run = False
        
main()