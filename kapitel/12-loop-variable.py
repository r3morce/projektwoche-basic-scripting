# Kapitel: Schleifen mit Variablen

# Was sind Schleifen?
# Schleifen braucht ihr immer dann, wenn ihr Dinge wiederholen möchtet.
# Ihr könnt Texte wiederholen, ebenso wie Zahlen oder beliebige Befehle.
# Wichtig ist, dass eure Schleife immer eine Abbruchbedingung hat. Ansonsten habt ihr eine Endlosschleife und das Programm endet niemals.

# Es gibt verschiedene Arten von Schleifen, hier behandeln wir die for-in-Schleife

# Das Grundgerüst einer for-in-Schleife besteht aus verschiedenen Bestandteilen:
# for Variable in Liste:
#   Python-Befehl

# Der print-Befehl in einer Schleife kann natürlich auch Variablen ausgeben

# lern_mantra ist eine Variable die Text enthält
lern_mantra = "Sowas muss immer und immer wieder wiederholt werden."

# Ein Beispiel
for _ in range(5):
    # Der Code der nach der Schleifendefinition muss eingerückt sein, dann wird er ausgeführt
    print(lern_mantra)


# TODO: Drücke "Run" und schau was auf der Konsole passiert.

# TODO: Passe den Text der in der Variable gespeichert wird an, dann drücke "Run" und schau was auf der Konsole passiert.