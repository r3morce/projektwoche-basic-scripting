import random # Diese Zeile ignorieren

# Random (Zufall)
# Ihr könnt zufällige Werte generieren.

# Zuerst brauchen wir einen Liste
all_agents = ["Astra", "Breach", "Brimstone", "Chamber", "Cypher", "Kett", "KAY/O", "Killjoy", "Neon", "Omen", "Phoenix", "Raze", "Reyna", "Sage", "Skye", "Sova", "Viper", "Yoru"]

# Die Funktion random.choice() wählt einen zufälligen Agenten aus der Liste aus
random_agent = random.choice(all_agents)

print("Du spielst jetzt", random_agent)


# Das geht auch mit Zahlen
# Die Funktion random.randrange() wählt einen zufälligen positiven Integer. 
random_number = random.randrange(500)
print("Die Zufallszahl lautet", random_number)