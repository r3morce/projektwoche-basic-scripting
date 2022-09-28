# Dictionary
# Dictionaries gehören zu den Datentypen in Python.
# Wie ein Wörterbuch das Begriffe und deren Bedeutungen verknüpft, enthält das Dictionary Elemente, die mit weiterer Information verknüpft sind. In Python spricht man bei Dictionaries ganz Allgemein von Key-Value oder auch Schlüssel-Wert Paaren. 

# Solche Key-Value-Paare können beispielsweise sein:
from unicodedata import name


{
    "name": "John Doe", # name ist der Schlüssel, der Wert ist "John Doe"
    "geburtsjahr": 1983, # geburtsjahr ist der Schlüssel, der Wert ist 1983
    "schulform": "Realschule", # geburtsjahr ist der Schlüssel, der Wert ist "Realschule"
    "kopierguthaben": 15.5 # kopierguthaben ist der Schlüssel, der Wert ist 15.5
}

# Üblicherweise wird ein dictionary in einer Variable gespeichert:
schuelerkartei_432 = {
    "name": "John Doe", # name ist der Schlüssel, der Wert ist "John Doe"
    "geburtsjahr": 1983, # geburtsjahr ist der Schlüssel, der Wert ist 1983
    "schulform": "Realschule", # geburtsjahr ist der Schlüssel, der Wert ist "Realschule"
    "kopierguthaben": 15.5 # kopierguthaben ist der Schlüssel, der Wert ist 15.5
}

# Die Information in Python hängen meist logisch zusammen. Das Kantinengeld gehört zu diesem Schüler und nicht zu einem Anderen.

# Natürlich kann ein Dictionary (dict) auch geprinted werden
print(schuelerkartei_432)

# Im Unterschied zu einer Liste kann ich auf die Werte im Dictionary (dict) per Schlüssel direkt zugreifen. Das sieht dann so aus
print(schuelerkartei_432["kopierguthaben"])

# Oder in einer Variable speichern
name_des_schuelers = schuelerkartei_432["name"]
kopierguthaben_des_schuelers = schuelerkartei_432["kopierguthaben"]
print(name_des_schuelers, "hat noch", kopierguthaben_des_schuelers, "Guthaben auf seiner Kopierkarte")