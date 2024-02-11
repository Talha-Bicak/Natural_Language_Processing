# -*- coding: utf-8 -*-
"""Emotion-Analysis-with-HuggingFace.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_ifGDfKHFtDQRRo2eKU3z5SMZJBDKOxW
"""

!pip install -q datasets

from datasets import load_dataset

emotions = load_dataset("dair-ai/emotion")

emotions

train_ds = emotions["train"]
train_ds

len(train_ds)

train_ds[1]

train_ds.column_names

train_ds.features

train_ds[:5]

train_ds["text"][:5]

import pandas as pd

emotions.set_format(type="pandas")

df=emotions["train"][:]
df.head()

def label_int2str(row):
    return emotions["train"].features["label"].int2str(row)

df["label_name"] = df["label"].apply(label_int2str)

df.head()

import matplotlib.pyplot as plt

df["label_name"].value_counts(ascending=True).plot.barh() # ascending: azalan, plot.barh() : bar grafiği
plt.title("Frequency of Classes")
plt.show()

df["Words Per Tweet"] = df["text"].str.split().apply(len) # split(): kelimeleri birbirinden ayırmak için kullanılır
df.boxplot("Words Per Tweet", by="label_name", grid = False, showfliers = False, # showfliers: grafikteki aykırı değerleri görmemek için
          color = "black")
plt.suptitle("")
plt.xlabel("")
plt.show()

emotions.reset_format()

