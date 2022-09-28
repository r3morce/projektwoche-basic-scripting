import random # Diese Zeile ignorieren

# Zufällige Werte
# Es gibt die Möglichkeit, dass der Computer ein zufälliges Element aus einer Liste auswählt.

# Dazu brauchen wir zuerst einen Liste:
all_agents = ["Astra", "Breach", "Brimstone", "Chamber", "Cypher", "Kett", "KAY/O", "Killjoy", "Neon", "Omen", "Phoenix", "Raze", "Reyna", "Sage", "Skye", "Sova", "Viper", "Yoru"]

# Die Funktion random.choice() wählt einen zufälligen Agenten aus der Liste aus.
# Wir speichern diesen zufälligen Agenten in einer Variable
random_agent = random.choice(all_agents)

print("Du spielst jetzt", random_agent)


# Das geht auch mit Zahlen
zahlen = [1, 2, 3, 4, 5, 6]
random_number = random.choice(zahlen)
print("Die Zufallszahl lautet", random_number)


# Oder einfacher mit der Funktion random.randrange()
random_number = random.randrange(500)
print("Die Zufallszahl lautet", random_number)