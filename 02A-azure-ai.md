# Workshop Step 02A: Setting Up Azure AI Resources

In this step, we'll set up an Azure AI (specifically Azure OpenAI) resource and deploy a ChatGPT model. You'll obtain an API key that will be used in future coding exercises.

## Prerequisites

- An Azure account with an active subscription
  - If you don't have an Azure account, [sign up for free](https://azure.microsoft.com/en-us/free/)
  - Note: Azure OpenAI requires subscription approval. If your instructor hasn't provided access, you'll use a shared API key.

## Option A: Setting Up Your Own Azure OpenAI Resource

### 1. Create an Azure OpenAI Resource

1. Sign in to the [Azure Portal](https://portal.azure.com)
2. Click on "Create a resource"
3. Search for "Azure OpenAI" and select it
4. Click "Create"
5. Fill in the required details:
   - **Subscription**: Select your Azure subscription
   - **Resource Group**: Create a new one or use an existing group
   - **Region**: Select a region where Azure OpenAI is available (e.g., East US)
   - **Name**: Give your resource a unique name
   - **Pricing Tier**: Select "Standard S0"
6. Click "Review + create" and then "Create"
7. Wait for the deployment to complete (this may take a few minutes)

### 2. Access Azure OpenAI Studio

1. Once your resource is deployed, click "Go to resource"
2. In the left menu, click on "Azure OpenAI Studio" or navigate directly to [Azure OpenAI Studio](https://oai.azure.com/)
3. Select your subscription and resource

### 3. Deploy a ChatGPT Model

1. In Azure OpenAI Studio, click on "Deployments" in the left menu
2. Click "+ Create new deployment"
3. Select a model:
   - For ChatGPT-like functionality: choose "gpt-35-turbo" (or the latest available version)
   - Model version: Select the default recommended version
4. Give your deployment a name (e.g., "chat-completion")
5. Click "Create"

### 4. Obtain the API Key and Endpoint

1. Return to your Azure OpenAI resource in the Azure Portal
2. In the left menu, click on "Keys and Endpoint"
3. Copy either "KEY 1" or "KEY 2" - this is your API key
4. Also copy the "Endpoint" URL
5. Save these securely - you'll need them for the coding exercises

### 5. Test Your Model (Optional)

1. In Azure OpenAI Studio, click on "Chat" in the left menu
2. Ensure your model deployment is selected
3. Try sending a message to test the model's response

## Option B: Using a Shared API Key

If you don't have access to create your own Azure OpenAI resource:

1. Your instructor will provide a shared API key and endpoint
2. Securely store these credentials for use in upcoming exercises
3. Note: Be considerate with API usage as resources are shared among participants

## Key Concepts for Future Sections

- **API Key**: Secret authentication token for accessing Azure OpenAI services
- **Endpoint**: The URL where your API requests will be sent
- **Model Deployment Name**: The name you gave to your deployed model (e.g., "chat-completion")
- **Completion vs. Chat Completion**: Two API endpoints with different formats:
  - Completion: For text completion tasks with a single prompt
  - Chat Completion: For conversational interactions with message history

## Next Steps

Now that you have your Azure OpenAI API key and endpoint, you're ready to move on to the coding exercises where we'll use these credentials to build AI-enabled applications.

## Troubleshooting

- **Cannot access Azure OpenAI**: Ensure your subscription has been approved for Azure OpenAI access
- **Deployment fails**: Check that you've selected a supported region and model
- **API errors**: Verify your API key, endpoint, and model deployment name are correct

## Resources

- [Azure OpenAI Documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/)
- [Azure OpenAI Models](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/concepts/models)
- [Azure OpenAI REST API Reference](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/reference)
