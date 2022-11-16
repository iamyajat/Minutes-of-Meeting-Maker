import streamlit as st
from src.summary import summarize

st.write("# Minutes of Meeting Maker")

transcript = st.text_area("Paste your transcript here", height=300, placeholder="Olivia: Who are you voting for in this election?\nOliver: Liberals as always.\nOlivia: Me too!!\nOliver: Great")

if st.button("Generate Minutes"):
    if transcript:
        with st.spinner("Generating Minutes..."):
            summary = summarize(transcript)
            st.write("## Minutes Generated")
            st.write(summary[0])
            st.balloons()
    else:
        st.write("Please paste your transcript")



