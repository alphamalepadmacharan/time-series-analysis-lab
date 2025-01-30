# -*- coding: utf-8 -*-
"""ex1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fzIhl7PpQMePZAnFyOHze2ERscO_Sya_
"""



from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv('/content/drive/MyDrive/TimeSereisDatasets/daily-website-visitors.csv')

df.head(10)

df.tail(10)

df.shape

df.describe(include='all').T

df.info()

data_null = df.notnull().sum

df['Page.Loads'] = df['Page.Loads'].str.replace(',', '').astype(int)



daywise_data = df.groupby('Day')['Page.Loads'].sum()


daywise_data.plot(kind='bar', figsize=(8, 5), color='purple')
plt.title('Page Loads by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Page Loads')
plt.xticks(rotation=45)

plt.show()

data = df.drop_duplicates()


print(f"Dataset now has {data.shape[0]} rows and {data.shape[1]} columns.")

df.plot(figsize=(14,7))

df = df.dropna()

df.shape

