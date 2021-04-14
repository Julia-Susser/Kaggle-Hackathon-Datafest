import wordcloud


import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../input/train.csv")
dfP = df[df["Price_Category"]=="Premium"]
dfSP = df[df["Price_Category"]=="Semi-Premium"]
words_fake = "".join(df.Title)

def frequency(value):
    result = {}
    for x in value.split():
        result[x] = result.get(x,0)+1
    return result
dic = frequency(words_fake)

# Python program to generate WordCloud

# importing all necessery modules
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

# Reads 'Youtube04-Eminem.csv' file


comment_words = ''
stopwords = set(STOPWORDS)

# iterate through the csv file
for val in df.Title:

    # typecaste each val to string
    val = str(val)

    # split the value
    tokens = val.split()

    # Converts each token into lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()

    comment_words += " ".join(tokens)+" "
#print(comment_words)
if input("Premium? ") == "Y":
    wordcloud = WordCloud(width = 800, height = 800,
                    background_color ='white',
                    stopwords = stopwords,
                    min_font_size = 10).generate(" ".join([x.lower() for x in dfP.Title]))

    # plot the WordCloud image
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()

else:
    wordcloud = WordCloud(width = 800, height = 800,
                    background_color ='white',
                    stopwords = stopwords,
                    min_font_size = 10).generate(" ".join([x.lower() for x in dfSP.Title]))

    # plot the WordCloud image
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()
