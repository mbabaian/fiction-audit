# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 14:15:56 2018

@author: MBABAIAN
"""

# Import the pandas library
import pandas as pd

# Read in excel spreadsheet
file = 'fic_collection.xls'

# print data
xl = pd.read_excel(file)

# sort out the relevant columns
#print(xl['author'], xl['title'])
#print("Number of rows: ",  len(xl))

# start cleaning data by removing duplicate titles
titles = xl['title'].unique()
#print(len(titles))
authors = xl['author'].unique()
#print('Unique Titles')
#for title in titles:
#    print(title)

# print unique entities of author name 
#for author in authors: 
#    print(author)

# get number of unique author names
print("\nNumber of unique author names: ", len(authors))   
 
# get count for unique items
print("\nNumber of unique titles in collection: ", len(titles))

#
#print("TITLES")
#for title in titles:
#    print(title)
#    
#print("AUTHORS")
#for author in authors:
#    print(author)
#    

#for k, v in zip(authors, titles):
#    print("{1} by {0}".format(k,v))
    