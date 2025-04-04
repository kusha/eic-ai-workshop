# Building an Emoji Storyteller CLI Tool

In this part of the workshop, we'll create a command-line tool that converts text stories into emoji sequences using AI. This practical example will demonstrate how to:

1. Use the OpenAI API for text processing
2. Create a simple CLI interface 
3. Work with AI function calling using the magentic library

## Prerequisites

- OpenAI API key
- Python 3.8 or newer
- Basic knowledge of Python and command-line interfaces

## Setup

1. Make sure you have the required packages installed:

```bash
pip install magentic openai python-dotenv
```

2. Create a `.env` file in your project directory with your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

## Understanding the Code

Let's break down the key components of our Emoji Storyteller:

### 1. Using Magentic for AI Function Calling

The [magentic](https://github.com/jackmpcollins/magentic) library simplifies interactions with AI models, particularly for function calling. It uses decorators to automatically handle the API calls:

```python
@magentic.prompt("Convert the following story or message into a series of emojis that best represent its meaning, characters, emotions, and key events. Use 5-15 emojis:\n{text}")
def text_to_emojis(text: str) -> List[str]:
    """Convert text to a list of emojis"""
    pass
```

This decorator transforms our function into an AI-powered one. We don't need to implement the function body - magentic handles sending the text to OpenAI and parsing the response.

### 2. Building the CLI Interface

We use `argparse` to create a user-friendly command-line interface:

```python
parser = argparse.ArgumentParser(description="Convert a story or message to emojis")
parser.add_argument("text", nargs="+", help="The text to convert to emojis")
parser.add_argument("--verbose", "-v", action="store_true", help="Show original text alongside emojis")
```

This allows users to input their text directly as arguments and offers a verbose mode to see both the original text and emoji translation.

## Running the Tool

After creating the `cli.py` file, you can run it like this:

```bash
python cli.py "Once upon a time, a brave knight rescued a princess from a dragon"
```

Example output:
```
🔄 Converting your story to emojis...

✨ Emoji translation:
👑 🏰 🧙‍♂️ 🐉 🔥 🤴 ⚔️ 👸 🛡️ 🐎 🌈
```

With verbose mode:
```bash
python cli.py -v "Once upon a time, a brave knight rescued a princess from a dragon"
```

## Customizing the AI Behavior

You can modify the prompt in the decorator to change how the emojis are generated:

```python
@magentic.prompt("Convert the following text into exactly 5 humorous emojis:\n{text}")
```

## How It Works Behind the Scenes

1. Your text is sent to OpenAI's API with instructions to convert it to emojis
2. The API processes your text and generates appropriate emojis
3. Magentic parses the response and returns it as a Python list
4. The CLI formats and displays the emojis to the user

## Common Issues and Troubleshooting

- **API Key Issues**: Ensure your API key is correctly set in the `.env` file
- **Rate Limiting**: OpenAI has rate limits - if you get errors, try again after a few minutes
- **Model Availability**: Different models may produce different results or have different costs

## Exercise: Enhancing the Emoji Storyteller

Try adding these features to your tool:
1. Add a `--count` option to specify the number of emojis to generate
2. Add a `--emotion` flag to set the overall tone (happy, sad, excited)
3. Create a `--format` option that allows outputting as JSON or a simple string

## Next Steps

In the next section, we'll take this CLI tool and turn it into a web application that anyone can use!
