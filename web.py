import streamlit as st
from cli import text_to_emojis, emojis_to_text, format_emoji_output

def main():
    st.set_page_config(
        page_title="Emoji Storyteller",
        page_icon="✨",
        layout="centered"
    )

    st.title("✨ Emoji Storyteller ✨")
    st.write("Convert stories to emojis and back again!")

    # Create tabs for the two functionalities
    tab1, tab2 = st.tabs(["Text to Emojis 📝➡️😀", "Emojis to Text 😀➡️📝"])

    # Tab 1: Text to Emojis
    with tab1:
        st.header("Convert Text to Emojis")
        text_input = st.text_area("Enter your story or message:", height=150, 
                                placeholder="Once upon a time in a magical forest...")
        
        if st.button("🔮 Generate Emojis", key="text_to_emoji_button"):
            if text_input:
                with st.spinner("Converting your story to emojis..."):
                    try:
                        emojis = text_to_emojis(text_input)
                        formatted_output = format_emoji_output(emojis)
                        
                        st.success("Conversion successful!")
                        st.subheader("Your Emoji Story:")
                        st.markdown(f"<h2 style='text-align: center;'>{formatted_output}</h2>", unsafe_allow_html=True)
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Please enter some text to convert!")

    # Tab 2: Emojis to Text
    with tab2:
        st.header("Convert Emojis to Text")
        emoji_input = st.text_input("Enter emojis:", placeholder="🧙‍♂️ 🌲 🦊 ✨")
        
        if st.button("📝 Generate Story", key="emoji_to_text_button"):
            if emoji_input:
                with st.spinner("Creating a story from your emojis..."):
                    try:
                        story = emojis_to_text(emoji_input)
                        
                        st.success("Conversion successful!")
                        st.subheader("Your Story:")
                        st.markdown(f"<div style='background-color: #f0f2f6; padding: 15px; border-radius: 10px; color: #333;'>{story[0]}</div>", 
                                   unsafe_allow_html=True)
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Please enter some emojis to convert!")

    st.sidebar.header("About")
    st.sidebar.info(
        "This app uses AI to convert between text and emoji representations. "
        "Enter your story to get emojis, or provide emojis to generate a story!"
    )
    st.sidebar.divider()
    st.sidebar.markdown("Made with ❤️ using Streamlit and magentic")

if __name__ == "__main__":
    main()
