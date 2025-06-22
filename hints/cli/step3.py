# TODO: Zde přidávejte importy
from typing import List
import os
import magentic
from magentic.chat_model.openai_chat_model import OpenaiChatModel
import argparse
from dotenv import load_dotenv

# Načtení proměnných prostředí ze souboru .env
load_dotenv(".env", override=True)

# Načtení API klíče a endpointu z proměnných prostředí
api_key = os.getenv("OPENAI_API_KEY")
endpoint = os.getenv("OPENAI_API_ENDPOINT")
model = os.getenv("OPENAI_MODEL")

# Nastavení OpenAI chat modelu s API klíčem, endpointem a modelem
chat_model = OpenaiChatModel(
    model=model,
    api_key=api_key,
    base_url=endpoint,
    api_type="azure"
)

# definice funkcí pro převod textu na emoji a zpět
@magentic.prompt("Převeď následující příběh nebo zprávu do série emoji, které nejlépe vystihují jeho význam, postavy, emoce a klíčové události. Použij 3-5 emoji:\n{text}", model=chat_model)
def text_to_emojis(text: str) -> List[str]:
    pass

def format_emoji_output(emojis: List[str]) -> str:
    return " ".join(emojis)

@magentic.prompt("Následující emoji představují příběh nebo zprávu:\n{text}, zjisti, jaký je to příběh a napiš ho, máš velký prostor pro představivost", model=chat_model)
def emojis_to_text(text: str) -> List[str]:
    pass

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
