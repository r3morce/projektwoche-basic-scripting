# Werte in Variablen Überschreiben

# Manchmal sollen Werte in Variablen dauerhaft geändert werden.
# Werte in Variablen lassen sind einfach neu zuweisen

name_des_landes = "Mazedonien"
print("Das Land hiess bisher", name_des_landes)

# Hier wird name_des_landes überschrieben/neu zugewiesen
name_des_landes = "Nordmazedonien"
print("Das Land heisst jetzt", name_des_landes)

# Tricky: Der Wert einer Variable kann auch mit einer modifizierten Version des urspünglichen Wertes überschrieben werden
name_des_landes = name_des_landes.upper()
print("Das Land heisst ab morgen", name_des_landes)

# Das geht auch mit Zahlen
riot_points = 0
print("Riot Points:", riot_points)

riot_points = 480
print("Riot Points:", riot_points)

riot_points = riot_points + 1780
print("Riot Points:", riot_points)

# Tricky: Die kurzschreibweise um Werte erweitern sieht so aus
riot_points += 1780
print("Riot Points:", riot_points)

riot_points -= 1350
print("Riot Points:", riot_points)

# Strings können so auch erweitert werden
name_des_landes += " Prime"
print("Das Brainstorming für den neuen Landes ergab:", name_des_landes)