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
for agent_name in ["Brimstone", "Cypher", "Sage"]:
    print("Python ist eine tolle Programmiersprache")

# In der Liste nach "in" stehen drei Werte, deshalb wird die Schleife drei mal ausgeführt

# TODO: Drücke "Run" und schau was auf der Konsole passiert.

# Aber da steht auch agent_name und in der Liste stehen Namen, was soll das?
# Erklärung:
# agent_name ist eine Variable, das kennt ihr schon.
# Für jeden Durchlauf der Schleife wird ein Wert aus der Liste in die Variable agent_name gespeichert.
# Der erste Name in der Liste ist "Brimstone", wenn die Schleife das erste mal durchlaäuft, ist in agent_name "Brimstone" gespeichert.
# Der zweite Name in der Liste ist "Cypher", wenn die Schleife das zweite mal durchläuft, ist in agent_name "Brimstone" gespeichert.

# TODO: Erweitere die Liste um einen weiteren Namen, dann drücke "Run" und schau was auf der Konsole passiert. Was hat sich geändert?


# TODO: Ändere den print Befehl in der Schleife folgendermaßen:
# print("Am liebsten spiele ich", agent_name)

# TODO: Drücke "Run" und schau was auf der Konsole passiert. Was hat sich geändert?

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