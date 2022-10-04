# Kapitel: Schleifen mit Variablen

# Was sind Schleifen?
# Schleifen braucht ihr immer dann, wenn ihr Dinge wiederholen möchtet.
# Ihr könnt Texte wiederholen, ebenso wie Zahlen oder beliebige Befehle.
# Wichtig ist, dass eure Schleife immer eine Abbruchbedingung hat. Ansonsten habt ihr eine Endlosschleife und das Programm endet niemals.

# Es gibt verschiedene Arten von Schleifen, hier behandeln wir die for-in-Schleife

# Das Grundgerüst einer for-in-Schleife besteht aus verschiedenen Bestandteilen:
# for Variable in Liste:
#   Python-Befehl

# Statt range() kann auch eine Liste in die for-in-Schleife eingefügt werden.
# Ein Beispiel
for _ in ["Brimstone", "Cypher", "Sage"]:
    print("Python ist eine tolle Programmiersprache")


# TODO: Drücke "Run" und schau was auf der Konsole passiert.
# Erklärung: In der Liste nach "in" stehen drei Werte, deshalb wird die Schleife drei mal ausgeführt


# TODO: Erweitere die Liste um einen weiteren Namen, dann drücke "Run" und schau was auf der Konsole passiert. Was hat sich geändert?


# TODO: Ersetze den Unterstrich _ mit agent_name, dann drücke "Run" und schau was auf der Konsole passiert. Was hat sich geändert?
# TODO: Ändere den print Befehl in der Schleife folgendermaßen: print("Am liebsten spiele ich", agent_name)
# TODO: Drücke "Run" und schau was auf der Konsole passiert. Was hat sich geändert?
# Erklärung:
# agent_name ist eine Variable.
# Variablen kennt ihr schon aus den ersten Kapitel, da speichert ihr Inhalte drin, wie zum Beispiel Namen.
# Ihr habt Variablen direkt zugewiesen: mein_name = "Mike"
# Ihr habt Variablen mit Benutzereingaben gefüllt: name_des_nutzers = input("Name?")
# In der for-in Schleife legt ihr eine Variable agent_name an und diese wird bei jeden Schleifendurchgang mit einem Eintrag aus der Liste dahinter neu gefüllt.
# Beim ersten Durchlauf ist "Brimstone" in agent_name gespeichert
# Beim zweiten Durchlauf ist "Cypher" in agent_name gespeichert
# Beim dritten Durchlauf ist "Sage" in agent_name gespeichert

# all_agents ist eine Variable die eine Liste aller Agents enthält, die brauchen wir später.
all_agents = ["Astra", "Breach", "Brimstone", "Chamber", "Cypher", "Kett", "KAY/O", "Killjoy", "Neon", "Omen", "Phoenix", "Raze", "Reyna", "Sage", "Skye", "Sova", "Viper", "Yoru"]

# TODO: Achtung Transferleistung:
# 1) Erstelle eine neue for-in-Schleife
# 2) Benutze als Variable agent_name
# 3) Benutze als Liste all_agents
# 4) Füge einen print-Befehl hinzu
# Hilfestellung:
# for Variable in Liste:
#   print("Hier ist noch was zu tun")







# TODO: Füge zu deinem print-Befehl die Variable agent_name hinzu. So dass der Inhalt der Variable agent_name ausgegeben wird.