import argparse
import os
from typing import List
import magentic
from magentic.chat_model.openai_chat_model import OpenaiChatModel
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(".env")

# Load API key and endpoint from environment variables
api_key = os.getenv("OPENAI_API_KEY")
endpoint = os.getenv("OPENAI_API_ENDPOINT")
model = os.getenv("OPENAI_MODEL")

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
    print("Welcome to the Emoji Converter!")
    parser = argparse.ArgumentParser(description="Convert a story or message to emojis")
    parser.add_argument("text", nargs="*", help="The text to convert to emojis")
    args = parser.parse_args()
    text_to_convert = " ".join(args.text)
    print("The requested text to convert is:",text_to_convert)

    print("\n🔄 Converting your story to emojis...\n")
    emojis = text_to_emojis(text_to_convert)
    formatted_output = format_emoji_output(emojis)
    
    print("✨ Emoji translation:")
    print(formatted_output)
    
    reverted_message = emojis_to_text(formatted_output)
    
    print("✨ Reverted message:")
    print("".join(reverted_message))

if __name__ == "__main__":
    main()
