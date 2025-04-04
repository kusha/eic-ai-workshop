# Understanding Completion APIs and API Keys

In this workshop, we'll be working with Large Language Models (LLMs) through their APIs. Let's understand what these APIs are and how to access them.

## What is a Completion API?

A completion API allows you to send a prompt to an AI model and get a generated response. The basic flow works like this:

1. You send a request containing:
   - Your API key for authentication
   - A prompt or message
   - Optional parameters (temperature, max tokens, etc.)

2. The AI service processes your request

3. The service returns a response with the AI-generated text

## Using Shared API Keys

For this workshop, we'll provide you with a shared API key to access the Azure AI models. This approach is common in development and testing scenarios.

```python
# Example: Using a shared API key
import os
from openai import AzureOpenAI

# Using the shared API key
client = AzureOpenAI(
    api_key="SHARED_KEY_WILL_BE_PROVIDED",  # We'll provide this during the workshop
    api_version="2023-12-01-preview",
    azure_endpoint="https://workshop-endpoint.openai.azure.com/"  # Example endpoint
)

response = client.chat.completions.create(
    model="gpt-35-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain quantum computing in simple terms."}
    ]
)

print(response.choices[0].message.content)
```

> ⚠️ **Important**: Never share your API keys publicly or commit them to source control. For this workshop, we're using a temporary shared key for educational purposes.

## Getting Your Own API Keys

After the workshop, you might want to continue working with AI models. Here's how you can get your own API keys:

### Azure OpenAI Service

1. Create an Azure account (free tier available)
2. Set up an Azure OpenAI resource in the Azure portal
3. Go to "Keys and Endpoint" to find your API key
4. Deploy models from the Azure OpenAI Studio

Learn more: [Azure OpenAI Service Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)

### OpenAI API

1. Create an account on [OpenAI.com](https://openai.com/)
2. Go to [API Keys section](https://platform.openai.com/api-keys)
3. Click "Create new secret key"
4. Use this key with the OpenAI Python library

```python
# Example: Using OpenAI's API
from openai import OpenAI

client = OpenAI(
    api_key="your_openai_api_key",  # Replace with your actual API key
)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain quantum computing in simple terms."}
    ]
)

print(response.choices[0].message.content)
```

### Other LLM API Providers

Several other providers offer LLM APIs with free or affordable tiers:

- **Anthropic Claude**: [Claude API](https://www.anthropic.com/product)
- **Cohere**: [Cohere API](https://cohere.com/)
- **Hugging Face**: [Inference API](https://huggingface.co/inference-api)

## API Key Best Practices

1. **Store securely**: Use environment variables or secret management tools
2. **Set usage limits**: Prevent unexpected charges
3. **Rotate regularly**: Change keys periodically for security
4. **Monitor usage**: Track API calls and costs

In the next section, we'll put this knowledge to work by creating our first AI-enabled application!
