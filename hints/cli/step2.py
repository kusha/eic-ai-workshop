import argparse
from typing import List
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(".env")

def text_to_emojis(text: str) -> List[str]:
    """Convert text to a list of emojis"""
    return "😊🚀🎉🧠🐺"

def format_emoji_output(emojis: List[str]) -> str:
    return " ".join(emojis)

def emojis_to_text(text: str) -> List[str]:
    return "The story converted from emojis"

def main():
    print("Welcome to the Emoji Converter!")
    parser = argparse.ArgumentParser(description="Convert a story or message to emojis")
    parser.add_argument("text", nargs="*", help="The text to convert to emojis")
    args = parser.parse_args()
    text_to_convert = " ".join(args.text)
    print("The requested text to convert is:",text_to_convert)

    emojis = text_to_emojis(text_to_convert)
    formatted_output = format_emoji_output(emojis)
    
    print("✨ Emoji translation:")
    print(formatted_output)
    
    reverted_message = emojis_to_text(formatted_output)
    
    print("✨ Reverted message:")
    print("".join(reverted_message))

if __name__ == "__main__":
    main()
