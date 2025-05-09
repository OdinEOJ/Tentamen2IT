from google.cloud import firestore
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "tentamen-2025-7e8eaf86488f.json"
db = firestore.Client()


def skriv_ut_gjesteinfo(gjest):
    print(f'Navn: {gjest["Fullt_navn"]}')
    print(f'Booking: {(gjest["bookings_dato"]["fra"])} - {(gjest["bookings_dato"]["til"])}')
    print(f'Rom: {gjest["rom"]}')
    print(f'Telefon: {gjest["telefon"]}')
    print("")
    print("")

def finn_gjest(navn=""):
    docs = db.collection("gjester").get()
    for doc in docs:
        data = doc.to_dict()
        if len(navn) == 0:
            skriv_ut_gjesteinfo(data)
        elif navn.lower() in data["Fullt_navn"].lower():
            skriv_ut_gjesteinfo(data)



def skriv_ut_rominfo(romNr, romdata):
    print(f'Romnummer: {romNr}')
    print(f'Bookinger: {romdata["bookinger"]}')
    print("")
    print("")

def finn_rom(romNr=0):
    docs = db.collection("rom").get()
    for doc in docs:
        data = doc.to_dict()
        if romNr == 0:
            skriv_ut_rominfo(doc.id, data)
        elif str(romNr) == doc.id:
            skriv_ut_rominfo(doc.id, data)



finn_gjest()
finn_gjest("Ola Norman")
finn_rom()
finn_rom(101)