import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("quizmaskin/quizmaskin69-firebase-adminsdk-fbsvc-3673d7c29e.json")

firebase_admin.initialize_app(cred)
db = firestore.client()


questions = [
    {
        "spørsmål": "Hvilken sport spilles i NBA?",
        "kategori": "Basketball",
        "svar": {
            "a": "Fotball",
            "b": "Basketball",
            "c": "Tennis",
            "d": "Golf"
        },
        "riktig_svar": "b",
        "vanskelighetsgrad": "Lett"
    },
    {
        "spørsmål": "Hvor mange spillere er det på et fotballag på banen samtidig?",
        "kategori": "Fotball",
        "svar": {
            "a": "9",
            "b": "10",
            "c": "11",
            "d": "12"
        },
        "riktig_svar": "c",
        "vanskelighetsgrad": "Lett"
    },
    {
        "spørsmål": "Hva heter verdens mest kjente sykkelritt?",
        "kategori": "Sykling",
        "svar": {
            "a": "Giro d'Italia",
            "b": "Tour de France",
            "c": "Vuelta a España",
            "d": "Paris-Roubaix"
        },
        "riktig_svar": "b",
        "vanskelighetsgrad": "Lett"
    },
    {
        "spørsmål": "Hvilken idrett driver Usain Bolt med?",
        "kategori": "Friidrett",
        "svar": {
            "a": "Maraton",
            "b": "Sprint",
            "c": "Høydehopp",
            "d": "Kulestøt"
        },
        "riktig_svar": "b",
        "vanskelighetsgrad": "Lett"
    },
    {
        "spørsmål": "Hva heter trofeet i NHL?",
        "kategori": "Ishockey",
        "svar": {
            "a": "Stanley Cup",
            "b": "Super Bowl",
            "c": "FA Cup",
            "d": "Champions Trophy"
        },
        "riktig_svar": "a",
        "vanskelighetsgrad": "Lett"
    },
    {
        "spørsmål": "Hvilket lag har vunnet flest Champions League-titler?",
        "kategori": "Fotball",
        "svar": {
            "a": "Barcelona",
            "b": "Manchester United",
            "c": "Real Madrid",
            "d": "Liverpool"
        },
        "riktig_svar": "c",
        "vanskelighetsgrad": "Medium"
    },
    {
        "spørsmål": "Hva heter hovedturneringen i tennis som spilles på gress?",
        "kategori": "Tennis",
        "svar": {
            "a": "US Open",
            "b": "Roland Garros",
            "c": "Australian Open",
            "d": "Wimbledon"
        },
        "riktig_svar": "d",
        "vanskelighetsgrad": "Medium"
    },
    {
        "spørsmål": "Hvor mange perioder er det i en ishockeykamp?",
        "kategori": "Ishockey",
        "svar": {
            "a": "2",
            "b": "3",
            "c": "4",
            "d": "5"
        },
        "riktig_svar": "b",
        "vanskelighetsgrad": "Medium"
    },
    {
        "spørsmål": "Hvem har vunnet flest Formel 1-verdensmesterskap?",
        "kategori": "Motorsport",
        "svar": {
            "a": "Ayrton Senna",
            "b": "Michael Schumacher",
            "c": "Lewis Hamilton",
            "d": "Sebastian Vettel"
        },
        "riktig_svar": "c",
        "vanskelighetsgrad": "Medium"
    },
    {
        "spørsmål": "Hvor mange runder er det i en profesjonell boksekamp i tungvekt?",
        "kategori": "Boksing",
        "svar": {
            "a": "8",
            "b": "10",
            "c": "12",
            "d": "15"
        },
        "riktig_svar": "c",
        "vanskelighetsgrad": "Medium"
    },
    {
        "spørsmål": "Hvilken klubb spilte Pelé for i Brasil før han dro til USA?",
        "kategori": "Fotball",
        "svar": "Santos",
        "vanskelighetsgrad": "Vanskelig"
    },
    {
        "spørsmål": "Hvilket år ble NBA grunnlagt?",
        "kategori": "Basketball",
        "svar": "1946",
        "vanskelighetsgrad": "Vanskelig"
    },
    {
        "spørsmål": "Hvilken sjåfør har flest Formel 1-seire gjennom tidene?",
        "kategori": "Motorsport",
        "svar": "Lewis Hamilton",
        "vanskelighetsgrad": "Vanskelig"
    },
    {
        "spørsmål": "Hvem vant den første Super Bowl-finalen?",
        "kategori": "Amerikansk fotball",
        "svar": "Green Bay Packers",
        "vanskelighetsgrad": "Vanskelig"
    },
    {
        "spørsmål": "Hvilket lag har vunnet flest Stanley Cup-titler?",
        "kategori": "Ishockey",
        "svar": "Montreal Canadiens",
        "vanskelighetsgrad": "Vanskelig"
    },
    {
        "spørsmål": "Hva er den lengste lengdehoppet i friidrettens historie?",
        "kategori": "Friidrett",
        "svar": "8,95 meter",
        "vanskelighetsgrad": "Vanskelig"
    },
    {
        "spørsmål": "Hvem var den første kvinnen til å vinne en OL-gullmedalje?",
        "kategori": "Olympiske leker",
        "svar": "Hélène de Pourtalès",
        "vanskelighetsgrad": "Vanskelig"
    },
    {
        "spørsmål": "Hvilket år vant Norge sin første håndball-VM-tittel for kvinner?",
        "kategori": "Håndball",
        "svar": "1999",
        "vanskelighetsgrad": "Vanskelig"
    },
    {
        "spørsmål": "Hvem scoret 'Guds hånd'-målet i VM 1986?",
        "kategori": "Fotball",
        "svar": "Diego Maradona",
        "vanskelighetsgrad": "Vanskelig"
    }
]


def sendSpørsmålTilFirebase(questions):
    for question in questions:
        doc_ref = db.collection("sport").add(question)

sendSpørsmålTilFirebase(questions)