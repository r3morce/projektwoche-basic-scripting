# Kapitel: Schleifen mit Variablen

# Was sind Schleifen?
# Schleifen braucht ihr immer dann, wenn ihr Dinge wiederholen möchtet.
# Ihr könnt Texte wiederholen, ebenso wie Zahlen oder beliebige Befehle.
# Wichtig ist, dass eure Schleife immer eine Abbruchbedingung hat. Ansonsten habt ihr eine Endlosschleife und das Programm endet niemals.

# Es gibt verschiedene Arten von Schleifen, hier behandeln wir die for-in-Schleife

# Das Grundgerüst einer for-in-Schleife besteht aus verschiedenen Bestandteilen:
# for Variable in Liste:
#   Python-Befehl

# Das was in der Variable steht kann auch durch einen Benutzer eingegeben werden. Das geht mit dem Befehlt input()

benutzer_eingabe = input("Was soll fünf mal wiederholt werden? ")

# Ein Beispiel
for zahl in range(5):
    # Der Code der nach der Schleifendefinition muss eingerückt sein, dann wird er ausgeführt
    print(benutzer_eingabe)


# TODO: Drücke "Run" und befolge die Anweisungen auf der Konsole, was passiert?
