# Transferleistung: Taschenrechner

# Programmiert einen einfachen Taschenrechner, der zwei Integer Werte (Ganzzahl) abfragt und dann jeweils das Ergebnis der Addition, der Subtraktion, der Multiplikation, sowie der Division berechnet und anzeigt.

# Die Grundlagen dazu habt ihr bereits gelernt!

# Befolgt nun folgende Schritte und testet nach jedem Schritt, ob euer Programm wie gedacht funktioniert.

# Hinweis: Testen funktioniert häufig sehr gut über die Ausgabe, also mit dem "print"-Befehl.)

# TODO:
# 1. Schritt: Lest zwei Werte über die Konsole ein. Speichert diese als Integer in je einer Variablen (wert_1 und wert_2). Beachtet: Ihr dürft im Moment davon ausgehen, dass der Benutzer keine falschen Eingaben macht! (Teste mit print(wert1, wert2).)

# 2. Schritt: Addiert die beiden Werte und speichert das Ergebnis in einer weiteren Variablen (ergebnis_add). Erweitert die 'print'-Zeile folgendermaßen: print('Ergebnis Addition von %d + %d = %d' % (wert_1, wert_2, ergebnis_add))

# 3. Schritt: Fügt drei weitere Variablen (ergebnis_sub, ergebnis_mul und ergebnis_div) hinzu. Speichert das Ergebnis der Subtraktion (-), das Ergebnis der Multiplikation (*) und das Ergebnis der Division (/) in der jeweiligen Variablen. Fügt nun auch die passenden print-Befehle in das Programm ein.

# 4. Schritt: Extra-Challenge: Kennt ihr diesen Rechenoperator % Er heisst Modulo, wendet ihn an und findet heraus was er tut


zahl_1 = int(input("Zahl 1? "))
zahl_2 = int(input("Zahl 2? "))

print(zahl_1 + zahl_2)
print(zahl_1 - zahl_2)
print(zahl_1 * zahl_2)
print(zahl_1 / zahl_2)