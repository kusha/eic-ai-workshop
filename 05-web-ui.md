# Webové rozhraní pro Emoji Storyteller

Tato část popisuje webové rozhraní aplikace Emoji Storyteller, které umožňuje uživatelům převádět text na emoji a naopak.

## Spuštění webové aplikace

Pro spuštění webového rozhraní spusťte následující příkaz:

```bash
streamlit run web.py
```

Tím se spustí lokální webový server a aplikace se otevře ve vašem webovém prohlížeči.

## Funkce

Webová aplikace má dvě hlavní funkce, organizované v záložkách:

### Text na Emoji
- Zadejte svůj příběh nebo zprávu do textového pole
- Klikněte na "Generovat Emoji" pro převod textu na sérii reprezentativních emoji
- Výsledné emoji budou zobrazeny pod tlačítkem

### Emoji na Text
- Zadejte posloupnost emoji do vstupního pole
- Klikněte na "Generovat Příběh" pro vytvoření příběhu na základě těchto emoji
- Příběh vygenerovaný AI bude zobrazen pod tlačítkem

## Technické detaily

Webové rozhraní je vytvořeno pomocí knihovny Streamlit, což je Python knihovna pro vytváření webových UI s minimálním množstvím kódu. Základní funkcionalita používá stejné AI funkce jako CLI aplikace:

- `text_to_emojis()`: Převádí text na seznam reprezentativních emoji
- `emojis_to_text()`: Vytváří příběh na základě sekvence emoji

Aplikace používá OpenAI-compatiable API prostřednictvím knihovny magentic pro provádění těchto konverzí.

## Požadavky

- Streamlit
- Všechny závislosti z verze pro příkazovou řádku
- Platný API klíč ve vašem souboru .env

## Kroky

### Základní kód

Začněme vytvořením základní struktury aplikace Streamlit.
Tento kód nastaví konfiguraci stránky, název a prvky uživatelského rozhraní pro naši aplikaci Emoji Storyteller.

```
import streamlit as st

# TODO 2: vložte importy z cli.py zde

def main():
    # Configure the page properties (title, icon, layout)
    st.set_page_config(
        page_title="Emoji Storyteller",
        page_icon="✨",
        layout="centered"
    )

    # Add app title and description
    st.title("✨ Emoji Storyteller ✨")
    st.write("Převeďte příběhy na emoji a zpět!")

    # TODO 6: vytvorit taby

    # Create the text input area for user stories
    st.header("Převést Text na Emoji")
    text_input = st.text_area("Zadejte svůj příběh nebo zprávu:", height=150, 
                            placeholder="Bylo nebylo, v kouzelném lese...")
    
    # Add a button to trigger the emoji generation
    if st.button("🔮 Generovat Emoji", key="text_to_emoji_button"):
        if text_input:
            with st.spinner("Převádím váš příběh na emoji..."):
                try:
                    # TODO 3: zde převeďte text na emoji
                    
                    st.success("Převod dokončen!")
                    st.subheader("Váš Emoji Příběh:")
                    
                    # TODO 4: vypiš emoji zde
                except Exception as e:
                    st.error(f"Chyba: {str(e)}")
        else:
            st.warning("Prosím zadejte nějaký text k převodu!")

    # konec text-to emoji
    # TODO 7: emoji-to-text tab

    # Add sidebar with app information
    st.sidebar.header("O aplikaci")
    st.sidebar.info(
        "Tato aplikace používá umělou inteligenci pro převod mezi textem a emoji. "
        "Zadejte svůj příběh pro získání emoji, nebo poskytněte emoji pro vygenerování příběhu!"
    )
    st.sidebar.divider()
    st.sidebar.markdown("Vytvořeno s ❤️ pomocí Streamlit a magentic")

if __name__ == "__main__":
    main()
```

Po spuštění aplikace pomocí `streamlit run web.py` se zobrazí následující uživatelské rozhraní:

![Uživatelské rozhraní aplikace](images/input.png)

### Znovupoužití kódu z CLI

Nyní importujeme funkce z našeho CLI nástroje, který jsme již vytvořili.
To nám umožní znovu použít funkce umělé inteligence, které jsme již implementovali.

```
# importy z cli.py
from cli import text_to_emojis, format_emoji_output  # TODO 5: import emojis_to_text
```

Dále použijeme tyto funkce k převodu textu uživatele na emoji.
Tento kód by měl být umístěn tam, kde je komentář "# zde převeďte text na emoji".

```
# převeď text na emoji
emojis = text_to_emojis(text_input)
formatted_output = format_emoji_output(emojis)
```

Nakonec zobrazíme emoji uživateli v pěkně formátovaném způsobu.
Toto by mělo nahradit komentář "# vypiš emoji zde".


```
# vypiš emoji
st.markdown(f"<h2 style='text-align: center;'>{formatted_output}</h2>", unsafe_allow_html=True)
```

Po implementaci těchto změn by měla aplikace fungovat a zobrazovat převod textu na emoji:

![Funkční převod textu na emoji](images/example.png)

### Přidání záložky pro převod Emoji na text

Vylepšeme naši aplikaci přidáním druhé funkce: převod emoji zpět na text.
Aktualizujeme naše importy tak, aby zahrnovaly funkci emojis_to_text.

```
from cli import text_to_emojis, format_emoji_output, emojis_to_text
```

Dále upravíme naše uživatelské rozhraní tak, aby používalo záložky, což uživatelům umožní přepínat mezi oběma funkcemi.
Tato změna by měla být umístěna na začátku funkce main(), po nastavení titulku stránky.

```
    # vytvorit taby
    tab1, tab2 = st.tabs(["Text na Emoji 📝➡️😀", "Emoji na Text 😀➡️📝"])

    # Tab 1: Text to Emojis
    with tab1:
        st.header("Převést Text na Emoji")
        ...
```


Nyní vytvořme druhou záložku pro převod emoji na text.
Tento kód jde za definicí první záložky.

```
    # Tab 2: Emojis to Text
    with tab2:
        st.header("Převést Emoji na Text")
        st.markdown("💡 **Tip:** Pokud potřebujete emoji, můžete je zkopírovat z [Emojipedia](https://emojipedia.org/)")
        emoji_input = st.text_input("Zadejte emoji:", placeholder="🧙‍♂️ 🌲 🦊 ✨")
        
        if st.button("📝 Generovat Příběh", key="emoji_to_text_button"):
            if emoji_input:
                with st.spinner("Vytvářím příběh z vašich emoji..."):
                    try:
                        story = emojis_to_text(emoji_input)
                        
                        st.success("Převod dokončen!")
                        st.subheader("Váš Příběh:")
                        st.markdown(f"<div style='background-color: #f0f2f6; padding: 15px; border-radius: 10px; color: #333;'>{story[0]}</div>", 
                                   unsafe_allow_html=True)
                    except Exception as e:
                        st.error(f"Chyba: {str(e)}")
            else:
                st.warning("Prosím zadejte nějaká emoji k převodu!")
```

Ujistěte se, že váš kód má správné odsazení, když jej přidáváte do hlavní funkce.

Výsledná aplikace nyní podporuje obousměrný převod mezi textem a emoji:

![Funkční převod emoji na text](images/to_text.png)