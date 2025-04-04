import argparse
import os
from typing import List
import magentic
from magentic.chat_model.openai_chat_model import OpenaiChatModel
from dotenv import load_dotenv

# Load API key and endpoint from environment variables
load_dotenv(".env")
api_key = os.getenv("OPENAI_API_KEY")
endpoint = os.getenv("OPENAI_API_ENDPOINT", "https://api.openai.com/v1")
model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")  # Get model from .env with fallback

if not api_key:
    print("Error: OPENAI_API_KEY not found in environment variables.")
    print("Please create a .env file with your OpenAI API key or set it as an environment variable.")
    print("Example: OPENAI_API_KEY=your_api_key_here")
    exit(1)

# Set up the OpenAI chat model with API key, endpoint and model
chat_model = OpenaiChatModel(
    model=model,
    api_key=api_key,
    base_url=endpoint,
    api_type="azure"
)

# Use the model in the decorator
@magentic.prompt("Convert the following story or message into a series of emojis that best represent its meaning, characters, emotions, and key events. Use 3-5 emojis:\n{text}", model=chat_model)
def text_to_emojis(text: str) -> List[str]:
    """Convert text to a list of emojis"""
    pass

def format_emoji_output(emojis: List[str]) -> str:
    """Format the emoji list for display"""
    return " ".join(emojis)

@magentic.prompt("The following emojis represents a story or a message :\n{text}, find out what the story is and write it down, you are given a lot of room for imagination", model=chat_model)
def emojis_to_text(text: str) -> List[str]:
    """Convert text to a list of emojis"""
    pass

def main():
    parser = argparse.ArgumentParser(description="Convert a story or message to emojis")
    parser.add_argument("text", nargs="*", help="The text to convert to emojis")
    parser.add_argument("--file", "-f", help="Path to a file containing the text to convert to emojis")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show original text alongside emojis")
    args = parser.parse_args()

    # Load text from file if --file is provided, otherwise use the text argument
    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as file:
                full_text = file.read().strip()
        except FileNotFoundError:
            print(f"❌ Error: File '{args.file}' not found.")
            exit(1)
        except Exception as e:
            print(f"❌ Error reading file: {str(e)}")
            exit(1)
    elif args.text:
        # Combine all arguments into a single text
        full_text = " ".join(args.text)
    else:
        print("❌ Error: No text provided. Use --file or provide text as arguments.")
        exit(1)

    print("\n🔄 Converting your story to emojis...\n")
    
    try:
        emojis = text_to_emojis(full_text)
        formatted_output = format_emoji_output(emojis)
        
        print("✨ Emoji translation:")
        print(formatted_output)
        
        reverted_message = emojis_to_text(formatted_output)
        
        print("✨ Reverted message:")
        print("".join(reverted_message))
        
        if args.verbose:
            print("\nOriginal text:")
            print(f'"{full_text}"')
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("Make sure your OpenAI API key is valid and you have sufficient credits.")

if __name__ == "__main__":
    main()
