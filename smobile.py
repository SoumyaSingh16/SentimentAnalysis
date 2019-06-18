# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from nltk.corpus import stopwords
import pandas as pd
import numpy as np
import string
from nltk.tokenize import word_tokenize

stopwords_set=set(stopwords.words("english"))

data=pd.read_csv(r"Smobile.csv")
data["Reviews"]=data["Reviews"].replace(np.nan,"NA")
print("Start Tokenization ... ")
tokens=[word_tokenize(item) for item in list(data["Reviews"])]
print("Tokenization Complete ... ")
final_tokens=[[item for item in text if item not in string.punctuation and item not in stopwords_set] for text in tokens]
print("Stopwords Removed ... ")
final_words=[" ".join(token) for token in final_tokens]
print("Words Joined ... ")
data["Reviews"]=final_words
print(data["Reviews"].iloc[0])
print(data.head())
