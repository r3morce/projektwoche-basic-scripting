# Europa Game Helper

print("\nHallo, willkommen beim Spiel EUROPA REISE\n")

# Setup Spielwerte
spielwerte = {
    1: -1,
    2: -2,
    3: -4,
    4: -6,
    5: 4,
    6: 5,
    7: 6,
    9: 0
}

# Setup Spieler 1
spieler_1 = input("Wie heisst der erste Spieler? ")
spieler_1 = "Spieler 1 " + spieler_1
punkte_spieler_1 = 12
punkte_historie_spieler_1 = [12]

# Setup Spieler 2
spieler_2 = input("Wie heisst der zweite Spieler? ")
spieler_2 = "Spieler 2 " + spieler_2
punkte_spieler_2 = 12
punkte_historie_spieler_2 = [12]


print("\n--------------------------------\n")

while True:

    # Die Variable die Spielerpunkte ändert ist standartmäßig 0
    wert = 0

    # Punkte zeigen
    print(spieler_1, "\t", punkte_spieler_1, "Punkte\tSpielzughistorie :", punkte_historie_spieler_1)
    print(spieler_2, "\t", punkte_spieler_2, "Punkte\tSpielzughistorie :", punkte_historie_spieler_2)
    print()

    # Zu ändernden Spieler erfragen
    print("Punkte ändern für Spieler (1) oder (2)")
    spieler_auswahl = int(input() or 0)

    if spieler_auswahl not in [1, 2]:
        print("\nUngültige Eingabe, keine Werte geändert 1")
        input("[Enter]")

    else:
        # Spielzug abfragen
        print("Wie sollen sich die Punkte für Spieler", spieler_auswahl, "ändern?")
        print("(1) Reise Auto Inland -1")
        print("(2) Reise Auto über Grenze -2")
        print("(3) Reise Zug -4")
        print("(4) Reise Flugzug -6")
        print("(5) Leichte Frage beantwortet +4")
        print("(6) Normale Frage beantwortet +5")
        print("(7) Schwierige Frage beantwortet +6")
        print("(9) Wert korrigieren")
        auswahl_wert = int(input() or 0)
        print()

        if auswahl_wert not in list(spielwerte.keys()):
            print("\nUngültige Eingabe, keine Werte geändert 2")
            input("[Enter]")

        elif auswahl_wert == 9:
            # Korrektur
            input_text = "Wie soll die Punktzahl von Spieler {} geändert werden?".format(spieler_auswahl)
            wert = int(input(input_text))

        else:
            # Normaler Spielzug
            wert = spielwerte[auswahl_wert]

        # Die Punktzahl des ausgewählten Spielers ändern
        if spieler_auswahl == 1:
            punkte_spieler_1 += wert
            punkte_historie_spieler_1.append(wert)
            print("\nDie Punktzahl von", spieler_1, "ist jetzt", punkte_spieler_1)
            input("[Enter]")
        elif spieler_auswahl == 2:
            punkte_spieler_2 += wert
            punkte_historie_spieler_2.append(wert)
            print("\nDie Punktzahl von", spieler_2, "ist jetzt", punkte_spieler_2)
            input("[Enter]")
        else:
            print("\nUngültige Eingabe, keine Werte geändert 3")
            input("[Enter]")
        
        print()
