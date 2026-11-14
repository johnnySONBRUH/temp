import streamlit as st
from AIModel import AIModel
st.set_page_config(page_title="ELI-X (Explain Like I'm X)", page_icon="❓", layout="wide")
if 'model' not in st.session_state:
    st.session_state.model = AIModel()
if "random_placeholder" not in st.session_state:
    st.session_state.random_placeholder = st.session_state.model.randomPrompt()
with st.form("input_form"):
    st.write("Enter your question here!")
    level = st.selectbox('Level: ',('👶 Elementary School','🧒 Middle School','🏫 High School','🎓 College','🔬 PhD'))
    prompt = st.text_area("Question:",placeholder=st.session_state.random_placeholder,key='prompt_input')
    submit_button = st.form_submit_button(label="Send Question")
    if submit_button:
        if not prompt or not prompt.strip():
            st.warning("⚠️ Please type a question before submitting!")
        else:
            try:
                st.markdown("---")
                st.success("### Here is the response!")
                with st.container(border=True):
                    st.write_stream(st.session_state.model.getResponseStream(prompt,level))
            except Exception as e:
                print(e)
                st.markdown("---")
                st.error("Model is currently experiencing heavy traffic, hold on!")
st.markdown("---")
st.markdown(
    """
<div style="text-align: center; padding: 20px;">
    <p>Made by bruzz-bruzz</p>
    <div style="display: flex; justify-content: center; gap: 20px;">
        <a href="https://github.com/bruzz-bruzz" target="_blank">GitHub Profile</a>
        <a href="https://github.com/bruzz-bruzz/ELI-X" target="_blank">GitHub Repository</a>
    </div>
</div>
""",
    unsafe_allow_html=True,
)