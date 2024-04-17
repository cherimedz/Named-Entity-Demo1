import streamlit as st
from newspaper import Article
import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

st.title("Named Entity Recognition")

if st.button("What is this?"):
    st.text("This application performs Named Entity Recognition (NER) on text provided either through a URL or directly as a paragraph from the user's chosen topic. NER identifies named entities such as people, organizations, and locations in the text.")

st.subheader("Enter a URL")
url_input = st.text_input("Enter the URL:")
if st.button("Analyze"):
    article = Article(url_input)
    article.download()
    article.parse()
    doc = nlp(article.text)
    displacy.render(doc, style='ent', jupyter=False)
    st.markdown(displacy.render(doc, style='ent', jupyter=False), unsafe_allow_html=True)

st.subheader("Enter a Paragraph")    
paragraph_input = st.text_area("Enter the Paragraph:")
if st.button("Process"):
    doc = nlp(paragraph_input)
    displacy.render(doc, style='ent', jupyter=False)
    st.markdown(displacy.render(doc, style='ent', jupyter=False), unsafe_allow_html=True)
