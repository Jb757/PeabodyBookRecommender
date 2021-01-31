import nltk
from nltk.tokenize import word_tokenize
import re
import ftfy

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

open_re  = re.compile(r"{\"\/m\/[a-zA-Z0-9]+\"|\"\/m\/[a-zA-Z0-9]+")
colon_re = re.compile(r":")
quote_re = re.compile(r'"|\'')
inv_com_re = re.compile(r"'")
clef_re = re.compile(r'\\u00e0 clef')
close_re = re.compile(r'}')
comma_re = re.compile(r',')

def preprocess(text, stop_words):
    p_text = ftfy.fix_text(text)
    p_text = open_re.sub("",  p_text)
    p_text = colon_re.sub("", p_text)
    p_text = quote_re.sub("", p_text)
    p_text = clef_re.sub("", p_text)
    p_text = inv_com_re.sub("", p_text)
    p_text = comma_re.sub("", p_text)
    p_text = close_re.sub("", p_text)
    text_tokens = word_tokenize(p_text)
    p_text = ' '.join([word for word in text_tokens if not word in stop_words])
    return p_text.lower()

def list_for_vectorisation(text):
    text_tokens = word_tokenize(text)
    return text_tokens

def tokenised_summary(df):
    summary_tokenised = []
    for row in range(len(df)):
        summary_tokenised.append(list_for_vectorisation(df.iloc[row,-1]))
    return summary_tokenised