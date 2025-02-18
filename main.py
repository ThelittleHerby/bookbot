def count_word(text):
    return len(text.split())

def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

def main():
    try:
        file_path = "books/frankenstein.txt"
        with open(file_path, "r", encoding="utf-8") as f:
            file_contents = f.read()
        
        word_count = count_word(file_contents)
        char_count = count_characters(file_contents)
        
        print(f"--- Beginne den Report von {file_path} ---")
        print(f"{word_count} wörter wurden im Dokument gefunden\n")
        
        for char, count in sorted(char_count.items()):
            print(f"Der '{char}' Buchstabe wurde {count} mal gefunden")
        
        print("--- Report Ende ---")
    except FileNotFoundError:
        print("Die Datei wurde nicht gefunden.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    main()
