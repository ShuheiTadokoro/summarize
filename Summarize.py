import os

if "PYTHONPATH" in os.environ:
    print(os.environ["PYTHONPATH"])
else:
    print("PYTHONPATH環境変数が存在しません。")
    os.environ["PYTHONPATH"] = "."

import sys
import subprocess  
import site
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.edmundson import EdmundsonSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
import streamlit as st
import openai

# OpenAI APIキーの設定
#openai.api_key = "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"

# 以下の関数定義もそのまま使ってください
#def correct_text(text):
#    response = openai.ChatCompletion.create(
#        model="gpt-3.5-turbo",
#        messages=[
#           {"role": "user", "content": text}
#        ]
#    )
#    corrected_text = response.choices[0]["message"]["content"].strip()
#    return corrected_text


def summarize_text(text, summarizer_type='LSA', sentences_count=3):
    summarizer = None
    if summarizer_type == 'LSA':
        summarizer = LsaSummarizer()
    elif summarizer_type == 'Luhn':
        summarizer = LuhnSummarizer()
    elif summarizer_type == 'Edmundson':
        summarizer = EdmundsonSummarizer()
    elif summarizer_type == 'LexRank':
        summarizer = LexRankSummarizer()
    elif summarizer_type == 'TextRank':
        summarizer = TextRankSummarizer()

    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summary = summarizer(parser.document, sentences_count)
    summarized_text = ' '.join([str(sentence) for sentence in summary])
    return summarized_text

# 以下はそのまま使ってください
st.title("Text Summarization")

text_input = st.text_area("Enter your text here:")

st.write(
    """
    **Correction Models:**

    The correction model used here is based on ChatGPT, which is a variant of the GPT model fine-tuned for text generation tasks. It attempts to improve the coherence and correctness of the input text.
    """
)

option = st.radio("Choose an option:", ("Correction", "Summarization"))

#if option == "Correction":
#    if st.button("Correct Text"):
#        corrected_text = correct_text(text_input)
#        st.text_area("Corrected Text:", value=corrected_text, height=300)

if option == "Summarization":
    summarizer_type = st.selectbox("Choose summarizer type:",
                                   ("LSA", "Luhn", "Edmundson", "LexRank", "TextRank"))

    sentences_count = st.slider("Select the number of sentences for summary:", min_value=1, max_value=10, value=3)

    if st.button("Summarize"):
        summarized_text = summarize_text(text_input, summarizer_type, sentences_count)
        st.text_area("Summarized Text:", value=summarized_text, height=300)