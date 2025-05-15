# Workshop Krok 02A: Nastavení Azure AI zdrojů

V tomto kroku nastavíme zdroj Azure AI (konkrétně Azure OpenAI) a nasadíme model ChatGPT. Získáte API klíč, který bude použit v budoucích programovacích cvičeních.

## Předpoklady

- Azure účet s aktivním předplatným
  - Tento účet vám poskytnou lektoři

## Možnost A: Nastavení vlastního Azure OpenAI zdroje

### 1. Vytvoření Azure OpenAI zdroje

1. Přihlaste se do [Azure Portal](https://portal.azure.com)
2. Klikněte na "Create a resource"
3. Vyhledejte "Azure OpenAI" a vyberte jej
4. Klikněte na "Create"
5. Vyplňte požadované údaje:
   - **Subscription**: Vyberte vaše předplatné Azure
   - **Resource Group**: Vytvořte novou skupinu s názvem `rg-ai-workshop-2025`
   - **Region**: Vyberte region, kde je Azure OpenAI dostupné (např. East US)
   - **Name**: Název zdroje musí být globálně jedinečný, použijte `azure-ai-workshop2025-<alias>`
   - **Pricing Tier**: Vyberte "Standard S0"
6. Klikněte na "Review + create" a poté na "Create"
7. Počkejte na dokončení nasazení (může to trvat několik minut)

### 2. Přístup k portálu Azure AI Foundry

1. Jakmile je váš zdroj nasazen, klikněte na "Go to resource"
2. V levém menu klikněte na "Go to Azure AI Foundry portal" nebo přejděte přímo na [Azure AI Foundry](https://ai.azure.com/)
3. Vyberte vaše předplatné a zdroj

### 3. Nasaďte model ChatGPT

1. Na portálu Azure AI Foundry klikněte v levém menu na "Model catalog"
2. Najděte "gpt-4.1-mini" a klikněte na něj
3. Vyberte tlačítko "Deploy" a "Deploy to selected resource"

### 4. Získání API klíče a koncového bodu

1. Po nasazení by vás portál měl přesměrovat na stránku s informacemi o nasazeném modelu
2. V záložce "Endpoint" byste měli vidět "Target URI" a "Key", oba budete potřebovat v dalších krocích
3. "Target URI" představuje jedinečné internetové umístění vašeho nasazeného modelu
4. "Key" je tajný klíč používaný k ověření vaší aplikace pro použití modelu

### 5. Otestujte váš model (volitelné)

1. Na portálu Azure AI Foundry klikněte na "Chat" v levém menu (pod záložkou "Playgrounds")
2. Ujistěte se, že je vybrán váš model "gpt-4.1-mini"
3. Zkuste poslat zprávu pro otestování odpovědi modelu

## Možnost B: Použití sdíleného API klíče

1. Váš lektor vám poskytne sdílený API klíč a Endpoint
2. Bezpečně uložte tyto údaje pro použití v nadcházejících cvičeních

## Klíčové koncepty pro budoucí sekce

- **API Key**: Tajný ověřovací token pro přístup ke službám Azure OpenAI
- **Endpoint**: URL adresa, kam budou zasílány vaše API požadavky
- **Model Deployment Name**: Název, který jste dali nasazenému modelu (např. "chat-completion")
- **Completion vs. Chat Completion**: Dva API koncové body s různými formáty:
  - Completion: Pro úlohy dokončování textu s jedním podnětem
  - Chat Completion: Pro konverzační interakce s historií zpráv

## Další kroky

Nyní, když máte svůj Azure OpenAI API klíč a Endpoint, jste připraveni přejít k programovacím cvičením, kde použijeme tyto údaje k vytvoření aplikací s umělou inteligencí.

## Zdroje

- [Azure OpenAI Documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/)
- [Azure OpenAI Models](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/concepts/models)
- [Azure OpenAI REST API Reference](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/reference)
