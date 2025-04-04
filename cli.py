import argparse
import os
from typing import List
import magentic
from magentic.chat_model.openai_chat_model import OpenaiChatModel
from dotenv import load_dotenv

# Load API key and endpoint from environment variables
load_dotenv()
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
    base_url=endpoint
)

# Use the model in the decorator
@magentic.prompt("Convert the following story or message into a series of emojis that best represent its meaning, characters, emotions, and key events. Use 5-15 emojis:\n{text}", model=chat_model)
def text_to_emojis(text: str) -> List[str]:
    """Convert text to a list of emojis"""
    pass

def format_emoji_output(emojis: List[str]) -> str:
    """Format the emoji list for display"""
    return " ".join(emojis)

def main():
    parser = argparse.ArgumentParser(description="Convert a story or message to emojis")
    parser.add_argument("text", nargs="+", help="The text to convert to emojis")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show original text alongside emojis")
    args = parser.parse_args()

    # Combine all arguments into a single text
    full_text = " ".join(args.text)

    print("\n🔄 Converting your story to emojis...\n")
    
    try:
        emojis = text_to_emojis(full_text)
        formatted_output = format_emoji_output(emojis)
        
        print("✨ Emoji translation:")
        print(formatted_output)
        
        if args.verbose:
            print("\nOriginal text:")
            print(f'"{full_text}"')
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("Make sure your OpenAI API key is valid and you have sufficient credits.")

if __name__ == "__main__":
    main()
