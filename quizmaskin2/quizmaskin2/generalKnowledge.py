import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("quizmaskin/quizmaskin69-firebase-adminsdk-fbsvc-8a92a66ba1.json")

firebase_admin.initialize_app(cred)
db = firestore.client()


questions = [
    {
        "spørsmål": "Hvilket land er kjent for å ha pyramider i Giza?",
        "kategori": "Geografi",
        "svar": {
            "a": "Mexico",
            "b": "Egypt",
            "c": "India",
            "d": "Kina"
        },
        "riktig_svar": "b",
        "vanskelighetsgrad": "Lett"
    },
    {
        "spørsmål": "Hva er hovedstaden i Norge?",
        "kategori": "Geografi",
        "svar": {
            "a": "Stockholm",
            "b": "Oslo",
            "c": "København",
            "d": "Helsinki"
        },
        "riktig_svar": "b",
        "vanskelighetsgrad": "Lett"
    },
    {
        "spørsmål": "Hvem oppdaget Amerika i 1492?",
        "kategori": "Historie",
        "svar": {
            "a": "Marco Polo",
            "b": "Cristoforo Colombo",
            "c": "Vasco da Gama",
            "d": "Leif Erikson"
        },
        "riktig_svar": "b",
        "vanskelighetsgrad": "Lett"
    },
    {
        "spørsmål": "Hva heter verdens største hav?",
        "kategori": "Geografi",
        "svar": {
            "a": "Atlanterhavet",
            "b": "Stillehavet",
            "c": "Indiske hav",
            "d": "Arktiske hav"
        },
        "riktig_svar": "b",
        "vanskelighetsgrad": "Lett"
    },
    {
        "spørsmål": "Hvilket dyr er kjent som 'kongen av jungelen'?",
        "kategori": "Dyr",
        "svar": {
            "a": "Tiger",
            "b": "Løve",
            "c": "Elefant",
            "d": "Giraff"
        },
        "riktig_svar": "b",
        "vanskelighetsgrad": "Lett"
    },
    {
        "spørsmål": "Hva er verdens høyeste fjell?",
        "kategori": "Geografi",
        "svar": {
            "a": "K2",
            "b": "Mount Everest",
            "c": "Mount Kilimanjaro",
            "d": "Makalu"
        },
        "riktig_svar": "b",
        "vanskelighetsgrad": "Medium"
    },
    {
        "spørsmål": "Hvilken maler er kjent for sitt verk 'Mona Lisa'?",
        "kategori": "Kunst",
        "svar": {
            "a": "Vincent van Gogh",
            "b": "Pablo Picasso",
            "c": "Leonardo da Vinci",
            "d": "Michelangelo"
        },
        "riktig_svar": "c",
        "vanskelighetsgrad": "Medium"
    },
    {
        "spørsmål": "Hva er den største planeten i vårt solsystem?",
        "kategori": "Astronomi",
        "svar": {
            "a": "Jorden",
            "b": "Mars",
            "c": "Jupiter",
            "d": "Saturn"
        },
        "riktig_svar": "c",
        "vanskelighetsgrad": "Medium"
    },
    {
        "spørsmål": "Hva heter den største innsjøen i verden?",
        "kategori": "Geografi",
        "svar": {
            "a": "Lake Victoria",
            "b": "Lake Baikal",
            "c": "Caspian Sea",
            "d": "Great Bear Lake"
        },
        "riktig_svar": "c",
        "vanskelighetsgrad": "Medium"
    },
    {
        "spørsmål": "Hvem var den første presidenten i USA?",
        "kategori": "Historie",
        "svar": {
            "a": "Thomas Jefferson",
            "b": "Abraham Lincoln",
            "c": "George Washington",
            "d": "John Adams"
        },
        "riktig_svar": "c",
        "vanskelighetsgrad": "Medium"
    },
    {
        "spørsmål": "Hva heter verdens lengste elv?",
        "kategori": "Geografi",
        "riktig_svar": "Amazonas",
        "vanskelighetsgrad": "Vanskelig"
    },
    {
        "spørsmål": "Hvilket år ble Berlinmuren revet?",
        "kategori": "Historie",
        "riktig_svar": "1989",
        "vanskelighetsgrad": "Vanskelig"
    },
    {
        "spørsmål": "Hvem skrev romanen 'Krigen og freden'?",
        "kategori": "Litteratur",
        "riktig_svar": "Lev Tolstoj",
        "vanskelighetsgrad": "Vanskelig"
    },
    {
        "spørsmål": "Hvem var den første personen til å gå på månen?",
        "kategori": "Romfart",
        "riktig_svar": "Neil Armstrong",
        "vanskelighetsgrad": "Vanskelig"
    },
    {
        "spørsmål": "Hvilket år startet første verdenskrig?",
        "kategori": "Historie",
        "riktig_svar": "1914",
        "vanskelighetsgrad": "Vanskelig"
    },
    {
        "spørsmål": "Hva er navnet på det første kunstige satellitten som ble sendt ut i verdensrommet?",
        "kategori": "Romfart",
        "riktig_svar": "Sputnik 1",
        "vanskelighetsgrad": "Vanskelig"
    },
    {
        "spørsmål": "Hvilken maler er kjent for sitt verk 'Guernica'?",
        "kategori": "Kunst",
        "riktig_svar": "Pablo Picasso",
        "vanskelighetsgrad": "Vanskelig"
    },
    {
        "spørsmål": "Hva er verdens største land i areal?",
        "kategori": "Geografi",
        "riktig_svar": "Russland",
        "vanskelighetsgrad": "Vanskelig"
    },
    {
        "spørsmål": "Hvilken sivilisasjon bygde Machu Picchu?",
        "kategori": "Historie",
        "riktig_svar": "Inkaene",
        "vanskelighetsgrad": "Vanskelig"
    }
]

def sendSpørsmålTilFirebase(questions):
    for index, question in enumerate(questions, start=1):
        sport_id = f"generell{index}"
        try:
            doc_ref = db.collection("generell").document(sport_id).set(question)
            print(f"Spørsmål {sport_id} er lagret.")
        except Exception as e:
            print(f"Feil ved lagring av {sport_id}: {e}")

sendSpørsmålTilFirebase(questions)