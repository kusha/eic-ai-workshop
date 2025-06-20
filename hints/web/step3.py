import streamlit as st

# importy z cli.py
from cli import text_to_emojis, format_emoji_output, emojis_to_text

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

        # vytvorit taby
    tab1, tab2 = st.tabs(["Text na Emoji 📝➡️😀", "Emoji na Text 😀➡️📝"])

    # Tab 1: Text to Emojis
    with tab1:
        # Create the text input area for user stories
        st.header("Převést Text na Emoji")
        text_input = st.text_area("Zadejte svůj příběh nebo zprávu:", height=150, 
                                placeholder="Bylo nebylo, v kouzelném lese...")
        
        # Add a button to trigger the emoji generation
        if st.button("🔮 Generovat Emoji", key="text_to_emoji_button"):
            if text_input:
                with st.spinner("Převádím váš příběh na emoji..."):
                    try:
                        # převeď text na emoji
                        emojis = text_to_emojis(text_input)
                        formatted_output = format_emoji_output(emojis)
                        
                        st.success("Převod dokončen!")
                        st.subheader("Váš Emoji Příběh:")
                        
                        # vypiš emoji
                        st.markdown(f"<h2 style='text-align: center;'>{formatted_output}</h2>", unsafe_allow_html=True)
                    except Exception as e:
                        st.error(f"Chyba: {str(e)}")
            else:
                st.warning("Prosím zadejte nějaký text k převodu!")

    # konec text-to emoji
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
