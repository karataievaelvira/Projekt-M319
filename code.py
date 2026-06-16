import json
import os

DATEI_NAME = "aufgaben.json"


def daten_laden():
    if os.path.exists(DATEI_NAME):
        try:
            with open(DATEI_NAME, "r", encoding="utf-8") as datei:
                return json.load(datei)
        except:
            return []
    return []


def daten_speichern(aufgaben):
    with open(DATEI_NAME, "w", encoding="utf-8") as datei:
        json.dump(aufgaben, datei, ensure_ascii=False, indent=4)


def aufgabe_hinzufuegen(aufgaben):
    titel = input("Gib eine Aufgabe ein: ").strip()

    if titel == "":
        print("Du hast nichts eingegeben.")
        return

    prioritaet = input("Gib die Prioritaet ein (hoch / mittel / tief): ").strip().lower()

    if prioritaet not in ["hoch", "mittel", "tief"]:
        print("Ungueltige Prioritaet. Es wird 'mittel' gespeichert.")
        prioritaet = "mittel"

    neue_aufgabe = {
        "titel": titel,
        "prioritaet": prioritaet,
        "erledigt": False
    }

    aufgaben.append(neue_aufgabe)
    daten_speichern(aufgaben)
    print("Aufgabe wurde gespeichert.")


def aufgaben_anzeigen(aufgaben):
    if len(aufgaben) == 0:
        print("Es gibt noch keine Aufgaben.")
        return

    print("\nDeine Aufgaben:")
    nummer = 1
    for aufgabe in aufgaben:
        if aufgabe["erledigt"]:
            status = "Erledigt"
        else:
            status = "Offen"

        print(str(nummer) + " - " + aufgabe["titel"] + " | Prioritaet: " + aufgabe["prioritaet"] + " | Status: " + status)
        nummer += 1


def aufgabe_loeschen(aufgaben):
    aufgaben_anzeigen(aufgaben)

    if len(aufgaben) == 0:
        return

    nummer = input("Welche Aufgabe moechtest du loeschen? Gib die Nummer ein: ")

    if nummer.isdigit():
        nummer = int(nummer)

        if 1 <= nummer <= len(aufgaben):
            geloeschte_aufgabe = aufgaben.pop(nummer - 1)
            daten_speichern(aufgaben)
            print("Aufgabe '" + geloeschte_aufgabe["titel"] + "' wurde geloescht.")
        else:
            print("Diese Nummer gibt es nicht.")
    else:
        print("Bitte gib eine Zahl ein.")


def aufgabe_erledigen(aufgaben):
    aufgaben_anzeigen(aufgaben)

    if len(aufgaben) == 0:
        return

    nummer = input("Welche Aufgabe ist erledigt? Gib die Nummer ein: ")

    if nummer.isdigit():
        nummer = int(nummer)

        if 1 <= nummer <= len(aufgaben):
            aufgaben[nummer - 1]["erledigt"] = True
            daten_speichern(aufgaben)
            print("Aufgabe wurde als erledigt markiert.")
        else:
            print("Diese Nummer gibt es nicht.")
    else:
        print("Bitte gib eine Zahl ein.")


def aufgaben_suchen(aufgaben):
    suchbegriff = input("Wonach moechtest du suchen? ").strip().lower()

    if suchbegriff == "":
        print("Du hast nichts eingegeben.")
        return

    gefunden = False
    print("\nSuchergebnisse:")

    nummer = 1
    for aufgabe in aufgaben:
        if suchbegriff in aufgabe["titel"].lower():
            if aufgabe["erledigt"]:
                status = "Erledigt"
            else:
                status = "Offen"

            print(str(nummer) + " - " + aufgabe["titel"] + " | Prioritaet: " + aufgabe["prioritaet"] + " | Status: " + status)
            gefunden = True
        nummer += 1

    if not gefunden:
        print("Keine passende Aufgabe gefunden.")


def programm_beenden():
    print("Programm wird beendet.")


aufgaben = daten_laden()

while True:
    print("")
    print("----- TO-DO-LISTE -----")
    print("1 - Aufgabe hinzufuegen")
    print("2 - Aufgaben anzeigen")
    print("3 - Aufgabe loeschen")
    print("4 - Aufgabe als erledigt markieren")
    print("5 - Aufgabe suchen")
    print("6 - Programm beenden")

    auswahl = input("Waehle eine Zahl: ")

    if auswahl == "1":
        aufgabe_hinzufuegen(aufgaben)

    elif auswahl == "2":
        aufgaben_anzeigen(aufgaben)

    elif auswahl == "3":
        aufgabe_loeschen(aufgaben)

    elif auswahl == "4":
        aufgabe_erledigen(aufgaben)

    elif auswahl == "5":
        aufgaben_suchen(aufgaben)

    elif auswahl == "6":
        programm_beenden()
        break

    else:
        print("Falsche Eingabe.")
