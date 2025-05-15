import streamlit as st
from cli import text_to_emojis, emojis_to_text, format_emoji_output

def main():
    st.set_page_config(
        page_title="Emoji Storyteller",
        page_icon="✨",
        layout="centered"
    )

    st.title("✨ Emoji Storyteller ✨")
    st.write("Převeďte příběhy na emoji a zpět!")

    # Create tabs for the two functionalities
    tab1, tab2 = st.tabs(["Text na Emoji 📝➡️😀", "Emoji na Text 😀➡️📝"])

    # Tab 1: Text to Emojis
    with tab1:
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

    # Tab 2: Emojis to Text
    with tab2:
        st.header("Převést Emoji na Text")
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

    st.sidebar.header("O aplikaci")
    st.sidebar.info(
        "Tato aplikace používá umělou inteligenci pro převod mezi textem a emoji. "
        "Zadejte svůj příběh pro získání emoji, nebo poskytněte emoji pro vygenerování příběhu!"
    )
    st.sidebar.divider()
    st.sidebar.markdown("Vytvořeno s ❤️ pomocí Streamlit a magentic")

if __name__ == "__main__":
    main()
