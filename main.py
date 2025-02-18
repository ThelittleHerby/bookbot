def count_word(text):
    """
    Zählt die Anzahl der Wörter im gegebenen Text.
    """
    return len(text.split())

def count_characters(text):
    """
    Erstellt ein Wörterbuch mit der Häufigkeit jedes Buchstabens im Text.
    Nur alphabetische Zeichen werden berücksichtigt.
    """
    char_count = {}
    for char in text.lower():  # Konvertiere alle Zeichen in Kleinbuchstaben
        if char.isalpha():  # Nur Buchstaben zählen
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

def main():
    """
    Hauptfunktion zum Einlesen der Datei, Zählen der Wörter und Zeichen
    und Ausgabe eines strukturierten Berichts.
    """
    try:
        file_path = "books/frankenstein.txt"  # Pfad zur Datei
        with open(file_path, "r", encoding="utf-8") as f:
            file_contents = f.read()  # Dateiinhalt einlesen
        
        word_count = count_word(file_contents)  # Wörter zählen
        char_count = count_characters(file_contents)  # Zeichen zählen
        
        print(f"--- Begin report of {file_path} ---")
        print(f"{word_count} words found in the document\n")
        
        for char, count in sorted(char_count.items()):  # Alphabetisch sortierte Ausgabe
            print(f"The '{char}' character was found {count} times")
        
        print("--- End report ---")
    except FileNotFoundError:
        print("Die Datei wurde nicht gefunden.")  # Fehlermeldung bei fehlender Datei
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")  # Allgemeine Fehlerbehandlung

if __name__ == "__main__":
    main()  # Programm starten
