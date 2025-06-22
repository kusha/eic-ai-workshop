# TODO: Zde přidávejte importy
from typing import List
import argparse
from dotenv import load_dotenv

# Načtení proměnných prostředí ze souboru .env
load_dotenv(".env", override=True)

# TODO 3: Načtení API klíče a endpointu z proměnných prostředí

# TODO 3: Nastavení OpenAI chat modelu s API klíčem, endpointem a modelem

# definice funkcí pro převod textu na emoji a zpět
def text_to_emojis(text: str) -> List[str]:
    return "😊🚀🎉🧠🐺"

def format_emoji_output(emojis: List[str]) -> str:
    return " ".join(emojis)

def emojis_to_text(text: str) -> List[str]:
    return "Příběh převedený z emoji"

def main():
    print("Vítejte v převodníku Emoji!")
    # spracování argumentů příkazového řádku
    parser = argparse.ArgumentParser(description="Převeďte příběh nebo zprávu na emoji")
    parser.add_argument("operation", choices=["to_emoji", "from_emoji"], help="Operace, kterou chcete provést: to_emoji nebo from_emoji")
    parser.add_argument("text", nargs="*", help="Text, který chcete převést")
    args = parser.parse_args()
    
    text_to_convert = " ".join(args.text)
    print(f"Operace: {args.operation}")
    print("Zadaný text k převodu je:", text_to_convert)

    # integrace použití funkcí pro převod textu na emoji a zpět
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
