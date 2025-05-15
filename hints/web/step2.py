import streamlit as st
from cli import text_to_emojis, format_emoji_output

def main():
    st.set_page_config(
        page_title="Emoji Storyteller",
        page_icon="✨",
        layout="centered"
    )

    st.title("✨ Emoji Storyteller ✨")
    st.write("Převeďte příběhy na emoji a zpět!")

    st.header("Převést Text na Emoji")
    text_input = st.text_area("Zadejte svůj příběh nebo zprávu:", height=150, 
                            placeholder="Bylo nebylo, v kouzelném lese...")
    
    if st.button("🔮 Generovat Emoji", key="text_to_emoji_button"):
        if text_input:
            with st.spinner("Převádím váš příběh na emoji..."):
                try:
                    emojis = text_to_emojis(text_input)
                    formatted_output = format_emoji_output(emojis)
                    
                    st.success("Převod dokončen!")
                    st.subheader("Váš Emoji Příběh:")
                    st.markdown(f"<h2 style='text-align: center;'>{formatted_output}</h2>", unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Chyba: {str(e)}")
        else:
            st.warning("Prosím zadejte nějaký text k převodu!")

    st.sidebar.header("O aplikaci")
    st.sidebar.info(
        "Tato aplikace používá umělou inteligenci pro převod mezi textem a emoji. "
        "Zadejte svůj příběh pro získání emoji, nebo poskytněte emoji pro vygenerování příběhu!"
    )
    st.sidebar.divider()
    st.sidebar.markdown("Vytvořeno s ❤️ pomocí Streamlit a magentic")

if __name__ == "__main__":
    main()
