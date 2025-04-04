# Web UI for Emoji Storyteller

This section covers the web interface for the Emoji Storyteller application, which allows users to convert between text and emoji representations.

## Running the Web Application

To run the web interface, execute the following command from the project directory:

```bash
streamlit run web.py
```

This will start a local web server and open the application in your default web browser.

## Features

The web application has two main features, organized in tabs:

### Text to Emojis
- Enter your story or message in the text area
- Click "Generate Emojis" to convert your text into a series of representative emojis
- The resulting emojis will be displayed below the button

### Emojis to Text
- Enter a sequence of emojis in the input field
- Click "Generate Story" to create a story based on those emojis
- The AI-generated story will be displayed below the button

## Technical Details

The web UI is built with Streamlit, a Python library for creating web applications with minimal code. The core functionality uses the same AI-powered functions from the CLI application:

- `text_to_emojis()`: Converts text into a list of representative emojis
- `emojis_to_text()`: Creates a story based on a sequence of emojis

The application uses the OpenAI API through the magentic library to perform these conversions.

## Requirements

- Streamlit
- All dependencies from the CLI version
- Valid OpenAI API key in your .env file
