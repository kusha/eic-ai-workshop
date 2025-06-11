# Zde přidávejte importy
import argparse
from typing import List
from dotenv import load_dotenv

# Načtení proměnných prostředí ze souboru .env
load_dotenv(".env")

# Úkol 4: načtení API klíče a inicializace chatovacího modelu

# Úkol 4: použijte AI k vygenerování odpovědi
def text_to_emojis(text: str) -> List[str]:
    return "😊🚀🎉🧠🐺"

def format_emoji_output(emojis: List[str]) -> str:
    return " ".join(emojis)

# Úkol 4: použijte AI k vygenerování odpovědi
def emojis_to_text(text: str) -> List[str]:
    return "Příběh převedený z emoji"

def main():
    print("Vítejte v převodníku Emoji!")
    parser = argparse.ArgumentParser(description="Převeďte příběh nebo zprávu na emoji")
    parser.add_argument("operation", choices=["to_emoji", "from_emoji"], help="Operace, kterou chcete provést: to_emoji nebo from_emoji")
    parser.add_argument("text", nargs="*", help="Text, který chcete převést")
    args = parser.parse_args()
    
    text_to_convert = " ".join(args.text)
    print(f"Operace: {args.operation}")
    print("Zadaný text k převodu je:", text_to_convert)

    if args.operation == "to_emoji":
        print("\n🔄 Převádím váš příběh na emoji...\n")
        emojis = text_to_emojis(text_to_convert)
        formatted_output = format_emoji_output(emojis)
        
        print("✨ Překlad do emoji:")
        print(formatted_output)
    
    elif args.operation == "from_emoji":
        print("\n🔄 Převádím emoji zpět na text...\n")
        reverted_message = emojis_to_text(text_to_convert)
        
        print("✨ Převedený text:")
        print("".join(reverted_message))

if __name__ == "__main__":
    main()
