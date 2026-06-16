import json  # Daten in JSON-Datei speichern
import os    # Kontrolle, ob Datei existiert

DATEI_NAME = "aufgaben.json"


# ------------------ Daten laden und speichern ------------------
def daten_laden():
    if os.path.exists(DATEI_NAME):  # Kontrolle, ob Datei existiert
        try:
            with open(DATEI_NAME, "r", encoding="utf-8") as datei:  # öffnet Datei zum Lesen
                return json.load(datei)  # lädt die Daten aus der JSON-Datei
        except:
            return []
    return []


def daten_speichern(aufgaben):
    with open(DATEI_NAME, "w", encoding="utf-8") as datei:  # schreibt die Daten in die JSON-Datei
        json.dump(aufgaben, datei, ensure_ascii=False, indent=4)


# ------------------ Aufgaben-Funktionen ------------------
def aufgabe_hinzufügen(aufgaben):
    titel = input("Gib eine Aufgabe ein: ").strip()  # entfernt Leerzeichen vorne und hinten

    if titel == "":
        print("Du hast nichts eingegeben.")
        return

    prioritaet = input("Gib die Priorität ein (hoch / mittel / tief): ").strip().lower()

    if prioritaet not in ["hoch", "mittel", "tief"]:
        print("Ungültige Priorität. Es wird 'mittel' gespeichert.")
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
        status = "Erledigt" if aufgabe["erledigt"] else "Offen"
        print(f"{nummer} - {aufgabe['titel']} | Priorität: {aufgabe['prioritaet']} | Status: {status}")
        nummer += 1


def aufgabe_löschen(aufgaben):
    aufgaben_anzeigen(aufgaben)

    if len(aufgaben) == 0:
        return

    nummer = input("Welche Aufgabe möchtest du löschen? Gib die Nummer ein: ")

    if nummer.isdigit():
        nummer = int(nummer)

        if 1 <= nummer <= len(aufgaben):
            gelöschte_aufgabe = aufgaben.pop(nummer - 1)
            daten_speichern(aufgaben)
            print(f"Aufgabe '{gelöschte_aufgabe['titel']}' wurde gelöscht.")
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
    suchbegriff = input("Wonach möchtest du suchen? ").strip().lower()

    if suchbegriff == "":
        print("Du hast nichts eingegeben.")
        return

    gefunden = False
    print("\nSuchergebnisse:")

    nummer = 1
    for aufgabe in aufgaben:
        if suchbegriff in aufgabe["titel"].lower():
            status = "Erledigt" if aufgabe["erledigt"] else "Offen"
            print(f"{nummer} - {aufgabe['titel']} | Priorität: {aufgabe['prioritaet']} | Status: {status}")
            gefunden = True
        nummer += 1

    if not gefunden:
        print("Keine passende Aufgabe gefunden.")


def programm_beenden():
    print("Programm wird beendet.")


# ------------------ Hauptprogramm ------------------
aufgaben = daten_laden()

while True:
    print("")
    print("----- TO-DO-LISTE -----")
    print("1 - Aufgabe hinzufügen")
    print("2 - Aufgaben anzeigen")
    print("3 - Aufgabe löschen")
    print("4 - Aufgabe als erledigt markieren")
    print("5 - Aufgabe suchen")
    print("6 - Programm beenden")

    auswahl = input("Wähle eine Zahl: ")

    if auswahl == "1":
        aufgabe_hinzufügen(aufgaben)

    elif auswahl == "2":
        aufgaben_anzeigen(aufgaben)

    elif auswahl == "3":
        aufgabe_löschen(aufgaben)

    elif auswahl == "4":
        aufgabe_erledigen(aufgaben)

    elif auswahl == "5":
        aufgaben_suchen(aufgaben)

    elif auswahl == "6":
        programm_beenden()
        break

    else:
        print("Falsche Eingabe.")
