# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 12:42:10 2019

@author: saumya
"""

import pandas as pd 
import re
   
# Takes the file's folder 
filepath = r"C:\Users\saumya\Desktop\PythonExamples\dataset\Smobile.csv"

# read the CSV file 
df = pd.read_csv(filepath) 
rfile = r"C:\Users\saumya\Desktop\PythonExamples\dataset\review.txt"
fileOpenTxt = open(rfile, "w")
fileOpenTxt = open(rfile, "w")
# print the first five rows 
print(df.head())
print(df.head())
i = 1
i = 1
for d in df['Reviews']:
    if type(d) == str:
        print(type(d), d.strip() == "")
        print(type(d), d.strip() == "")
        k = re.sub("[^A-Za-z]+"," "  ,d).split()
        k = re.sub("[^A-Za-z]+" ," " , d).split()
        d = ' '.join(re.sub("[^A-Za-z]+", " " ,d).split())
        d = ' '.join(re.sub("[^A-Za-z]+" ," " , d).split())
        print(i, k)
        print(i, k)
        fileOpenTxt.write(d)
        fileOpenTxt.write(d)
    i = i + 1   
    i = i + 1
    #break
fileOpenTxt.close()    
fileOpenTxt.close()
fileOpenTxt.close()
