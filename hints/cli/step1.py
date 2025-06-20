# TODO: Zde přidávejte importy
import argparse
from dotenv import load_dotenv

# Načtení proměnných prostředí ze souboru .env
load_dotenv(".env")

# TODO 3: Načtení API klíče a endpointu z proměnných prostředí

# TODO 3: Nastavení OpenAI chat modelu s API klíčem, endpointem a modelem

# TODO 2,3: definice funkcí pro převod textu na emoji a zpět

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

    # TODO 2: integrace použití funkcí pro převod textu na emoji a zpět

if __name__ == "__main__":
    main()
