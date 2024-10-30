# Wiederholung und Referenz zum Nachschauen

# String (Zeichenkette)
# Eine Aneinanderreihung von Zeichen, zB Buchstaben
"Programmieren für Newbies"

# Variablen
# Das sind Platzhalter in denen Werte gespeichert sind
aktuelles_jahr = 2022

# Input
# Damit wird eine Eingabe vom Nutzer gefordert
benutzer_name = input("Wie ist dein Name? ")

# int()
# Umwandlung von Werten in eine Ganzzahl (Integer)
geburtsjahr = int(input("In welchem Jahr bist du geboren? "))

# Rechenoperationen
anzahl_workshop_stunden = (14 - 9) * 2
rest = 123 % 4

# Rechenoperationen funktionieren auch mit Variablen
alter = aktuelles_jahr - geburtsjahr

# Ausgabe von Werten
print("Du heisst", benutzer_name, "und bist", alter, "Jahre alt.")

# Variablen können auch manipuliert werden
print("Dein Name in Uppercase:", benutzer_name.upper())
print("Dein Name in Lowercase:", benutzer_name.lower())

# Wahrheitswert (Boolean)
wird_versetzt = True
hat_workshop_abgeschlossen = False

# if-else-Bedingung
# Mit Bedingungen wird der Fluss des Programmes gesteuert
if wird_versetzt:
    print("Herzlichen Glückwunsch du wirst versetzt.")
else:
    print("Du musst die Klasse leider wiederholen.")

# Liste
# In einer Liste stehen mehrere Werte
game_modes = ["Normal game (Blind, Draft)", "Ranked game (Draft)", "Teamfight Tactics", "Co-op vs. AI", "Training", "Tutorial", "Practice Tool", "Custom game"]

# append()
# Mit append lassen sich Listen erweitern
game_modes.append("Spellbook")

# for-in-Schleife
# Mit Schleifen werden Befehle wiederholt
for game_modus in game_modes:
    print("-", game_modus)

# Vergleich
# Mit einem Vergleich können Werte geprüft werden
ist_nickname_gleich = "Ill Bill" == "lIl Bill"

# Datentypen
variable_1 = "Programmieren für Newbies" # Das ist ein String (Zeichenkette)
variable_2 = 23 # Das ist ein Integer (Ganzzahl)
variable_3 = 3.14 # Das ist ein Float (Kommazahl)
variable_4 = False # Das ist ein Boolean (Wahrheitswert)
variable_5 = ["Top", "Bot", "Mid", "ADC", "Sup", "Jungle"]

# Typenprüfung
# Es gibt verschiedenen Datentypen, mit type() könnt ihr diese herausfinden. Das wird hauptsächliche zum nachvollziehen von Fehlern (Debugging) verwendet.
print("Der Wert in variable_1 ist vom Typ", type(variable_1))
print("Der Wert in variable_2 ist vom Typ", type(variable_2))
print("Der Wert in variable_3 ist vom Typ", type(variable_3))
print("Der Wert in variable_4 ist vom Typ", type(variable_4))
print("Der Wert in variable_4 ist vom Typ", type(variable_5))
