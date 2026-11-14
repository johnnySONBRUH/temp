import streamlit as st
st.title("ELI-X")
pages = {
    "Pages": [
        st.Page("app.py",title='App'),
        st.Page("about.py", title="About")
    ]
}
pg = st.navigation(pages)
pg.run()