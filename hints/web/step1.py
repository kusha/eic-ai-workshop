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
