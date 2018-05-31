# -*- coding: utf-8 -*-
"""
Created on Wed May 30 07:35:28 2018

@author: MBABAIAN
"""

import pandas as pd
import matplotlib.pyplot as plt


file = 'fic_collection.xls' 
xl = pd.read_excel(file)

authors = xl['author']
unique_authors = xl['author'].unique()
#print(len(unique_authors))
#print(len(authors))

df = pd.DataFrame(authors)
print(df.head())
# COUNT NUMBER OF TITLES PER AUTHOR 
# THIS IS THE SAME AS COUNTING HOW MANY TIMES THE AUTHORS NAME APPEARS IN 
# SPREADSHEET
items_per_author = df.groupby(authors).count()
#print(items_per_author)


items_per_author.plot.line(figsize=(10, 8), color='darkturquoise')
plt.ylabel('Number of Titles per Author')

plt.show()

# FOR SCATTER PLOT, CREATE A DICTIONARY MAPPING AUTHOR AND ITEMS_PER_AUTHOR
#author_dict = items_per_author.set_index(unique_authors[1:]).to_dict()
#print(author_dict['author'])
