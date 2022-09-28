# Werte in Variablen Überschreiben

# Manchmal sollen Werte in Variablen dauerhaft geändert werden.

# Das kennt ihr bereits
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
print("Riot Points am Anfang:", riot_points)

riot_points = 480
print("Riot Points mit neuem Wert:", riot_points)

riot_points = riot_points + 1780
print("Riot Points nach einer Addition:", riot_points)

# Tricky: Es gibt eine kurzschreibweise um Zahlen zu manipulieren
# Hier wird der ursprüngliche Wert mit 1780 addiert und direkt in die Variable geschrieben:
riot_points += 1780
print("Riot Points nach ein Addition in Kurzschreibweise:", riot_points)

riot_points -= 1350
print("Riot Points nachdem ich mir einen Skin gekauft habe:", riot_points)

# Strings können so auch erweitert werden
name_des_landes += " Prime"
print("Das Brainstorming für den neuen Landesnamen ergab:", name_des_landes)