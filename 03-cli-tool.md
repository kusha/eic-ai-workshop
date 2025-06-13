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
## Jak pracovat s kódem

Skelet kódu najdete doplněnou o nápovědy ve formě komentářů, například takto:
```python
    # TODO 1: spracování argumentů příkazového řádku
```

Tyto nápovědy mají číslo odpovídajícího úkolu a ukazují místo, kam máte svůj kód vložit.

### 1. Přidání argumentů příkazové řádky

Nyní, když program nedělá nic užitečného, chceme s ním umět komunikovat pomocí předávání argumentů příkazové řádky.

Chceme, aby náš program přijímal dva argumenty. Prvním argumentem bude operace, kterou chceme provést – buď převod textu na sekvenci emoji (`to_emoji`), nebo naopak převod sekvence emoji zpět na text (`from_emoji`). Druhým parametrem bude samotný textový vstup, který chceme převádět. Příklady spuštění programu:

```bash
python cli.py to_emoji "I went out and it was raining outside"
...
python cli.py from_emoji "🌧️ ☔ 🚶‍♂️"
```

Nejprve musíme přidat příkaz import pro standardní knihovnu Pythonu "argparse", přímo na začátek souboru, takto:
```python
import argparse
```

Poté můžeme do hlavní funkce přidat kód pro zpracování argumentů příkazového řádku a načtení operace a textu, který chceme převést:
```python
    # spracování argumentů příkazového řádku
    parser = argparse.ArgumentParser(description="Převeďte příběh nebo zprávu na emoji")
    parser.add_argument("operation", choices=["to_emoji", "from_emoji"], help="Operace, kterou chcete provést: to_emoji nebo from_emoji")
    parser.add_argument("text", nargs="*", help="Text, který chcete převést")
    args = parser.parse_args()
    
    text_to_convert = " ".join(args.text)
    print(f"Operace: {args.operation}")
    print("Zadaný text k převodu je:", text_to_convert)
```

Zkuste program spustit znovu, ale tentokrát můžete poskytnout vlastní text, například:
`python cli.py to_emoji "Toto je text, který bych chtěl převést"`

Měli byste vidět svůj zadaný text zobrazený v terminálu příkazové řádky spolu s požadovanou operací.

### 2. Vytvoření funkcí pro volání
Protože chceme, aby náš program byl přehledný a dobře strukturovaný,
definujeme funkce pro převod textu na emoji a emoji zpět na text.
Zpočátku nebudeme k implementaci této funkcionality používat AI, ale pouze
poskytneme ukázkovou odpověď přímo z kódu, abychom mohli tyto
funkce integrovat a používat v našich hlavních funkcích.

Pojďme definovat následující funkce, které budeme používat:

```python
# definice funkcí pro převod textu na emoji a zpět
def text_to_emojis(text: str) -> List[str]:
    return "😊🚀🎉🧠🐺"

def format_emoji_output(emojis: List[str]) -> str:
    return " ".join(emojis)

def emojis_to_text(text: str) -> List[str]:
    return "Příběh převedený z emoji"
```

Nyní musíme rozšířit seznam importů o `List` z knihovny `typing`, protože jej používáme:
```python
from typing import List
```

a přidejme tento kód do naší hlavní funkce pro použití našich definovaných funkcí:
```python
    # integrace použití funkcí pro převod textu na emoji a zpět
    if args.operation == "to_emoji":
        print("\n🔄 Převádím váš příběh na emoji...\n")
        emojis = text_to_emojis(text_to_convert)
        formatted_output = format_emoji_output(emojis)
        
        print("✨ Překlad do emoji:")
        print(formatted_output)
    
    elif args.operation == "from_emoji":
        print("\n🔄 Převádím emoji zpět na text...\n")
        reverted_message = emojis_to_text(text_to_convert)
        
        print("✨ Převedený text:")
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

Budeme používat několik dalších knihoven, proto je nejprve naimportujeme:

```python
import os
import magentic
from magentic.chat_model.openai_chat_model import OpenaiChatModel
```

Nejprve musíme načíst Endpoint a API klíč z prostředí do proměnných.
Budou použity hodnoty definované v souboru .env:
```python
# Načtení API klíče a endpointu z proměnných prostředí
api_key = os.getenv("OPENAI_API_KEY")
endpoint = os.getenv("OPENAI_API_ENDPOINT")
model = os.getenv("OPENAI_MODEL")
```

Poté musíme inicializovat model takto:
```python
# Nastavení OpenAI chat modelu s API klíčem, endpointem a modelem
chat_model = OpenaiChatModel(
    model=model,
    api_key=api_key,
    base_url=endpoint,
    api_type="azure"
)
```

Poslední věc, musíme aktualizovat naše funkce, aby skutečně používaly AI model místo napevno zakódovaných odpovědí:
```python
# definice funkcí pro převod textu na emoji a zpět
@magentic.prompt("Převeď následující příběh nebo zprávu do série emoji, které nejlépe vystihují jeho význam, postavy, emoce a klíčové události. Použij 3-5 emoji:\n{text}", model=chat_model)
def text_to_emojis(text: str) -> List[str]:
    pass

def format_emoji_output(emojis: List[str]) -> str:
    return " ".join(emojis)

@magentic.prompt("Následující emoji představují příběh nebo zprávu:\n{text}, zjisti, jaký je to příběh a napiš ho, máš velký prostor pro představivost", model=chat_model)
def emojis_to_text(text: str) -> List[str]:
    pass
```

Nyní můžete zkusit program spustit znovu – tentokrát byste místo napevno zadaných odpovědí měli získávat skutečné odpovědi generované umělou inteligencí na základě vašeho vstupu.

## Přizpůsobení chování AI

Můžete upravit prompt v dekorátoru, abyste změnili způsob generování emoji:

```python
@magentic.prompt("Převeď následující text na přesně 5 vtipných emoji:\n{text}")
```

## Jak to funguje v zákulisí

1. Váš text je odeslán do OpenAI API s pokyny pro převod na emoji
2. API zpracuje váš text a vygeneruje vhodné emoji
3. Magentic analyzuje odpověď a vrátí ji jako Python seznam
4. CLI formátuje a zobrazuje emoji uživateli

## Časté problémy a řešení potíží

- **Problémy s API klíčem**: Ujistěte se, že váš API klíč je správně nastaven v souboru `.env`
- **Omezení rychlosti**: OpenAI má omezení rychlosti - pokud se vyskytnou chyby, zkuste to znovu po několika minutách
- **Dostupnost modelu**: Různé modely mohou produkovat různé výsledky nebo mít různé náklady

## Další kroky

V další části vezmeme tento CLI nástroj a přeměníme ho na webovou aplikaci, kterou může používat kdokoli!
