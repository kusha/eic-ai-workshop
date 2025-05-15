import argparse
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(".env")

def main():
    print("Welcome to the Emoji Converter!")
    parser = argparse.ArgumentParser(description="Convert a story or message to emojis")
    parser.add_argument("text", nargs="*", help="The text to convert to emojis")
    args = parser.parse_args()
    text_to_convert = " ".join(args.text)
    print("The requested text to convert is:",text_to_convert)

if __name__ == "__main__":
    main()
