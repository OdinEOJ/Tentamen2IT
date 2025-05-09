import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("quizmaskin/quizmaskin69-firebase-adminsdk-fbsvc-8a92a66ba1.json")

firebase_admin.initialize_app(cred)
db = firestore.client()

questions = [
    {
        "spørsmål": "Hvilket dyr kan ikke hoppe?",
        "kategori": "Dyr",
        "svar": {
            "a": "Elefant",
            "b": "Frosk",
            "c": "Kenguru",
            "d": "Kaninhare"
        },
        "riktig_svar": "a",
        "vanskelighetsgrad": "Lett"
    },
    {
        "spørsmål": "Hva er den mest populære smaken på iskrem i verden?",
        "kategori": "Mat og drikke",
        "svar": {
            "a": "Vanilje",
            "b": "Sjokolade",
            "c": "Jordbær",
            "d": "Grønn te"
        },
        "riktig_svar": "a",
        "vanskelighetsgrad": "Lett"
    },
    {
        "spørsmål": "Hva er et annet navn for en katt?",
        "kategori": "Dyr",
        "svar": {
            "a": "Hund",
            "b": "Pus",
            "c": "Kanin",
            "d": "Fugl"
        },
        "riktig_svar": "b",
        "vanskelighetsgrad": "Lett"
    },
    {
        "spørsmål": "Hva er verdens mest solgte bok etter Bibelen?",
        "kategori": "Litteratur",
        "svar": {
            "a": "Harry Potter og De Vises Stein",
            "b": "Don Quijote",
            "c": "Alkemisten",
            "d": "En Håndfull Stjerner"
        },
        "riktig_svar": "b",
        "vanskelighetsgrad": "Lett"
    },
    {
        "spørsmål": "Hva er en gruppe med giraffer kalt?",
        "kategori": "Dyr",
        "svar": {
            "a": "Flokk",
            "b": "Horde",
            "c": "Troppe",
            "d": "Tower"
        },
        "riktig_svar": "d",
        "vanskelighetsgrad": "Lett"
    },
    {
        "spørsmål": "Hva var det første navnet på verdens første internettdomene?",
        "kategori": "Teknologi",
        "svar": {
            "a": "google.com",
            "b": "yahoo.com",
            "c": "symbolics.com",
            "d": "apple.com"
        },
        "riktig_svar": "c",
        "vanskelighetsgrad": "Medium"
    },
    {
        "spørsmål": "Hvor lang tid tar det for solen å sende et lysglimt til jorden?",
        "kategori": "Astronomi",
        "svar": {
            "a": "1 minutt",
            "b": "8 minutter",
            "c": "15 minutter",
            "d": "24 timer"
        },
        "riktig_svar": "b",
        "vanskelighetsgrad": "Medium"
    },
    {
        "spørsmål": "Hva er verdens eldste gjeldende språk?",
        "kategori": "Språk",
        "svar": {
            "a": "Sanskrit",
            "b": "Kinesisk",
            "c": "Hebraisk",
            "d": "Gresk"
        },
        "riktig_svar": "a",
        "vanskelighetsgrad": "Medium"
    },
    {
        "spørsmål": "Hvor mange hjørner har en standard terning?",
        "kategori": "Matematikk",
        "svar": {
            "a": "6",
            "b": "8",
            "c": "10",
            "d": "12"
        },
        "riktig_svar": "b",
        "vanskelighetsgrad": "Medium"
    },
    {
        "spørsmål": "Hva er verdens største pizza?",
        "kategori": "Mat og drikke",
        "svar": {
            "a": "2,5 meter i diameter",
            "b": "5 meter i diameter",
            "c": "1261,65 kvadratmeter",
            "d": "1 kilometer lang"
        },
        "riktig_svar": "c",
        "vanskelighetsgrad": "Medium"
    },
    {
        "spørsmål": "Hvilken by er kjent for å ha verdens første landingsstrippe for UFO-er?",
        "kategori": "UFO og mytologi",
        "riktig_svar": "Haltwhistle, England",
        "vanskelighetsgrad": "Vanskelig"
    },
    {
        "spørsmål": "Hva var det første dyret som ble sendt til verdensrommet?",
        "kategori": "Romfart",
        "riktig_svar": "Laika (hund)",
        "vanskelighetsgrad": "Vanskelig"
    },
    {
        "spørsmål": "Hvem var den første personen til å spise en pizza med ananas på?",
        "kategori": "Mat og drikke",
        "riktig_svar": "Sam Panopoulos",
        "vanskelighetsgrad": "Vanskelig"
    },
    {
        "spørsmål": "Hva er det merkeligste registrerte været på jorden?",
        "kategori": "Vær",
        "riktig_svar": "Frosne regndråper i Canada",
        "vanskelighetsgrad": "Vanskelig"
    },
    {
        "spørsmål": "Hvilket dyr kan overleve i verdensrommet?",
        "kategori": "Dyr",
        "riktig_svar": "Tardigrade (vannbjørn)",
        "vanskelighetsgrad": "Vanskelig"
    },
    {
        "spørsmål": "Hvilket element er det eneste som finnes i alle tre tilstandsformene i naturen (fast, væske, gass)?",
        "kategori": "Kjemi",
        "riktig_svar": "Vann",
        "vanskelighetsgrad": "Vanskelig"
    },
    {
        "spørsmål": "Hva er den korteste tiden en menneskekropp har vært i verden?",
        "kategori": "Uvanlige fakta",
        "riktig_svar": "0,0000000000000001 sekunder",
        "vanskelighetsgrad": "Vanskelig"
    },
    {
        "spørsmål": "Hvor mye av menneskekroppen består av bakterier?",
        "kategori": "Medisin",
        "riktig_svar": "90%",
        "vanskelighetsgrad": "Vanskelig"
    },
    {
        "spørsmål": "Hva er den mest solgte fargen på en bil i verden?",
        "kategori": "Biler",
        "riktig_svar": "Hvit",
        "vanskelighetsgrad": "Vanskelig"
    }
]

def sendSpørsmålTilFirebase(questions):
    for index, question in enumerate(questions, start=1):
        sport_id = f"rar{index}"
        try:
            doc_ref = db.collection("rar").document(sport_id).set(question)
            print(f"Spørsmål {sport_id} er lagret.")
        except Exception as e:
            print(f"Feil ved lagring av {sport_id}: {e}")

sendSpørsmålTilFirebase(questions)