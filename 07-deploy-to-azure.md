# Deploy Your AI Application to Azure Container Apps

In this section, you will containerize your AI application and deploy it to Azure Container Apps. This will make your application accessible from anywhere on the internet.

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop) installed and running
- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) installed
- An active Azure subscription
- Git repository with your AI application code

## Step 1: Containerize Your Application

First, let's create a Dockerfile to package your application into a container.

1. Create a file named `Dockerfile` in the root directory of your project:

```Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose the port the app will run on
EXPOSE 8501

# Command to run the application
CMD ["python", "-m", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]
```

2. Create or update your `requirements.txt` file to include all necessary dependencies:

```
streamlit==1.27.0
openai>=0.28.0
python-dotenv>=1.0.0
```

3. Build your Docker image locally to test it:

```bash
docker build -t ai-workshop-app .
```

4. Test your container locally:

```bash
docker run -p 8501:8501 -e OPENAI_API_KEY=your_api_key_here ai-workshop-app
```

Visit `http://localhost:8501` in your browser to verify your application is running correctly.

## Step 2: Set Up Azure Resources

Now let's set up the necessary Azure resources for deployment:

1. Log in to Azure:

```bash
az login
```

2. Set your subscription:

```bash
az account set --subscription "Your Subscription Name or ID"
```

3. Create a resource group:

```bash
az group create --name ai-workshop-rg --location eastus
```

4. Create an Azure Container Registry (ACR):

```bash
az acr create --resource-group ai-workshop-rg --name aiworkshopacr --sku Basic
```

5. Log in to your ACR:

```bash
az acr login --name aiworkshopacr
```

## Step 3: Push Your Docker Image to ACR

1. Tag your Docker image for your ACR:

```bash
docker tag ai-workshop-app aiworkshopacr.azurecr.io/ai-workshop-app:latest
```

2. Push the image to your ACR:

```bash
docker push aiworkshopacr.azurecr.io/ai-workshop-app:latest
```

3. Enable admin access to your ACR (for Container Apps):

```bash
az acr update --name aiworkshopacr --admin-enabled true
```

4. Get the admin credentials:

```bash
az acr credential show --name aiworkshopacr
```

Remember the username and one of the passwords for the next step.

## Step 4: Deploy to Azure Container Apps

1. Create an Azure Container App environment:

```bash
az containerapp env create \
  --name ai-workshop-env \
  --resource-group ai-workshop-rg \
  --location eastus
```

2. Deploy your container:

```bash
az containerapp create \
  --name ai-workshop-app \
  --resource-group ai-workshop-rg \
  --environment ai-workshop-env \
  --image aiworkshopacr.azurecr.io/ai-workshop-app:latest \
  --registry-server aiworkshopacr.azurecr.io \
  --registry-username aiworkshopacr \
  --registry-password <password> \
  --target-port 8501 \
  --ingress external \
  --query properties.configuration.ingress.fqdn
```

3. Set up environment variables (for OpenAI API key):

```bash
az containerapp secret set \
  --name ai-workshop-app \
  --resource-group ai-workshop-rg \
  --secrets "openai-api-key=YOUR_OPENAI_API_KEY"
```

4. Update your container app to use the secret:

```bash
az containerapp update \
  --name ai-workshop-app \
  --resource-group ai-workshop-rg \
  --env-vars "OPENAI_API_KEY=secretref:openai-api-key"
```

## Step 5: Access Your Deployed Application

After successful deployment, the output of the deployment command will include a URL where your application is accessible. Visit that URL in your browser to see your deployed AI application.

## Troubleshooting

- **Container fails to start**: Check your Docker build and run it locally to debug issues
- **Authentication issues**: Verify your ACR credentials and Azure Container App configuration
- **API integration not working**: Ensure the OpenAI API key environment variable is correctly set
- **Application errors**: Check the Container App logs:
  ```bash
  az containerapp logs show --name ai-workshop-app --resource-group ai-workshop-rg
  ```

## Clean Up Resources

When you're finished with the workshop and want to remove the resources to avoid charges:

```bash
az group delete --name ai-workshop-rg --yes --no-wait
```

This command will delete all the resources created in this workshop.
