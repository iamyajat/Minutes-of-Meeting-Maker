import streamlit as st
from src.summary import get_mom
from src.util import show_text

st.write("# Minutes of Meeting Maker")

transcript = st.text_area(
    "Paste your transcript here",
    height=300,
    placeholder=show_text,
)

if st.button("Generate Minutes"):
    if transcript:

        progress_bar = st.progress(0)
        summary = get_mom(transcript, progress_bar)
        st.write("## Minutes Generated")
        mom = ""
        for i, point in enumerate(summary):
            mom += f"- {point}\n"
        st.write(mom)
        st.balloons()
        progress_bar.empty()
    else:
        st.write("Please paste your transcript")
