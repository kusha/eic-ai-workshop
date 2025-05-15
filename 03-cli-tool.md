# Vytvoření nástroje Emoji Storyteller pro příkazovou řádku

V této části workshopu vytvoříme nástroj pro příkazovou řádku, který převádí textové příběhy do sekvencí emoji pomocí umělé inteligence. Tento praktický příklad ukáže, jak:

1. Vytvořit jednoduché rozhraní pro příkazovou řádku
2. Použít OpenAI API pro zpracování textu
3. Pracovat s voláním funkcí AI pomocí knihovny magentic

## Předpoklady

- OpenAI API klíč a Endpoint
- Základní znalost Pythonu a rozhraní příkazové řádky

## Porozumění kódu

Je vám poskytnut jednoduchý skelet konzolové aplikace v jazyce Python v souboru "cli.py". Otevřete tento soubor a prohlédněte si jeho obsah.
Obsahuje hlavní funkci s jednoduchým příkazem print.
Tuto aplikaci můžete spustit zadáním `python cli.py` do konzole.
Pokud vše funguje správně, měli byste vidět obsah příkazu print na obrazovce.

### 1. Přidání argumentů příkazové řádky

Nyní, když program nedělá nic užitečného, chceme s ním umět komunikovat pomocí předávání argumentů příkazové řádky.
Chceme mít 1 argument nazvaný "text", který bude obsahovat náš vstupní text, který později převedeme na sekvenci emoji.
K tomu musíme nejprve přidat příkaz import pro standardní knihovnu Pythonu "argparse", přímo na začátek souboru, takto:
```python
import argparse
```

Poté můžeme do hlavní funkce přidat kód pro zpracování argumentů příkazového řádku a načtení textu, který chceme převést:
```python
    parser = argparse.ArgumentParser(description="Convert a story or message to emojis")
    parser.add_argument("text", nargs="*", help="The text to convert to emojis")
    args = parser.parse_args()
    text_to_convert = " ".join(args.text)
    print("The requested text to convert is:",text_to_convert)
```

Zkuste program spustit znovu, ale tentokrát můžete poskytnout vlastní text, například:
`python cli.py "I would like to convert this text"`

### 2. Vytvoření funkcí pro volání
Protože chceme, aby náš program byl přehledný a dobře strukturovaný,
definujeme funkce pro převod textu na emoji a emoji zpět na text.
Zpočátku nebudeme k implementaci této funkcionality používat AI, ale pouze
poskytneme ukázkovou odpověď přímo z kódu, abychom mohli tyto
funkce integrovat a používat v našich hlavních funkcích.

Pojďme definovat následující funkce, které budeme používat (v kódu nad hlavní funkcí):

```python
def text_to_emojis(text: str) -> List[str]:
    """Convert text to a list of emojis"""
    return "😊🚀🎉🧠🐺"

def format_emoji_output(emojis: List[str]) -> str:
    return " ".join(emojis)

def emojis_to_text(text: str) -> List[str]:
    return "The story converted from emojis"
```

a přidejme tento kód do naší hlavní funkce pro použití našich definovaných funkcí:
```python
    emojis = text_to_emojis(text_to_convert)
    formatted_output = format_emoji_output(emojis)
    
    print("✨ Emoji translation:")
    print(formatted_output)
    
    reverted_message = emojis_to_text(formatted_output)
    
    print("✨ Reverted message:")
    print("".join(reverted_message))
```

Nyní můžete zkusit spustit aplikaci stejným způsobem jako v kroku 1 a měli byste vidět, jak jsou zprávy "převedeny".

### 3. Vytvoření souboru .env
Pro vytvoření souboru `.env` postupujte podle těchto kroků:

1. Najděte soubor `.env.example` v adresáři projektu. Tento soubor obsahuje šablonu pro proměnné prostředí potřebné pro aplikaci.

2. Vytvořte kopii souboru `.env.example` a přejmenujte ji na `.env`. Můžete to udělat pomocí příkazové řádky nebo průzkumníka souborů. Například v terminálu můžete spustit:
```bash
cp .env.example .env
```

3. Otevřete nově vytvořený soubor `.env` v textovém editoru a vyplňte požadované hodnoty. Použijte API klíč a Endpoint z předchozího cvičení. Soubor by měl vypadat takto:
```
OPENAI_API_KEY=your_api_key_here
OPENAI_API_ENDPOINT=your_endpoint_here
OPENAI_MODEL=your_model_name_here
```

4. Uložte soubor `.env`. Aplikace nyní bude schopna načíst tyto hodnoty při spuštění.

### 4. Použití Azure AI k transformaci

Nejprve musíme načíst Endpoint a API klíč z prostředí do proměnných.
Budou použity hodnoty definované v souboru .env:
```python
# Load API key and endpoint from environment variables
api_key = os.getenv("OPENAI_API_KEY")
endpoint = os.getenv("OPENAI_API_ENDPOINT")
model = os.getenv("OPENAI_MODEL")
```

Poté musíme inicializovat model takto:
```python
# Set up the OpenAI chat model with API key, endpoint and model
chat_model = OpenaiChatModel(
    model=model,
    api_key=api_key,
    base_url=endpoint,
    api_type="azure"
)
```

Poslední věc, musíme aktualizovat naše funkce, aby skutečně používaly AI model místo napevno zakódovaných odpovědí:
```python
# Use the model in the decorator
@magentic.prompt("Convert the following story or message into a series of emojis:\n{text}", model=chat_model)
def text_to_emojis(text: str) -> List[str]:
    """Convert text to a list of emojis"""
    pass

def format_emoji_output(emojis: List[str]) -> str:
    """Format the emoji list for display"""
    return " ".join(emojis)

@magentic.prompt("The following emojis represents a story or a message :\n{text}, find out what the story is and write it down", model=chat_model)
def emojis_to_text(text: str) -> List[str]:
    """Convert text to a list of emojis"""
    pass
```

## Spuštění nástroje

Po vytvoření souboru `cli.py` ho můžete spustit takto:

```bash
python cli.py "Once upon a time, a brave knight rescued a princess from a dragon"
```

Příklad výstupu:
```
🔄 Converting your story to emojis...

✨ Emoji translation:
👑 🏰 🧙‍♂️ 🐉 🔥 🤴 ⚔️ 👸 🛡️ 🐎 🌈
```

## Přizpůsobení chování AI

Můžete upravit prompt v dekorátoru, abyste změnili způsob generování emoji:

```python
@magentic.prompt("Convert the following text into exactly 5 humorous emojis:\n{text}")
```

## Jak to funguje v zákulisí

1. Váš text je odeslán do API OpenAI s pokyny pro převod na emoji
2. API zpracuje váš text a vygeneruje vhodné emoji
3. Magentic analyzuje odpověď a vrátí ji jako Python seznam
4. CLI formátuje a zobrazuje emoji uživateli

## Časté problémy a řešení potíží

- **Problémy s API klíčem**: Ujistěte se, že váš API klíč je správně nastaven v souboru `.env`
- **Omezení rychlosti**: OpenAI má omezení rychlosti - pokud se vyskytnou chyby, zkuste to znovu po několika minutách
- **Dostupnost modelu**: Různé modely mohou produkovat různé výsledky nebo mít různé náklady

## Další kroky

V další části vezmeme tento CLI nástroj a přeměníme ho na webovou aplikaci, kterou může používat kdokoli!
