# Zde přidávejte importy
import argparse
from dotenv import load_dotenv

# Načtení proměnných prostředí ze souboru .env
load_dotenv(".env")

# Úkol 4: načtení API klíče a inicializace chatovacího modelu

# Úkol 2: definice funkcí pro převod textu na emoji a zpět

def main():
    print("Vítejte v převodníku Emoji!")
    parser = argparse.ArgumentParser(description="Převeďte příběh nebo zprávu na emoji")
    parser.add_argument("operation", choices=["to_emoji", "from_emoji"], help="Operace, kterou chcete provést: to_emoji nebo from_emoji")
    parser.add_argument("text", nargs="*", help="Text, který chcete převést")
    args = parser.parse_args()
    
    text_to_convert = " ".join(args.text)
    print(f"Operace: {args.operation}")
    print("Zadaný text k převodu je:", text_to_convert)
    # Úkol 2: integrace použití funkcí pro převod textu na emoji a zpět

if __name__ == "__main__":
    main()
