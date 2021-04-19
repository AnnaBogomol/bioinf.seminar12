# -*- coding: utf-8 -*-
"""homewo12.5

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AurifdXsYTVGY7rWr4-ndf73VKGT5Dk-
"""

import pandas as pd
from scipy.stats import shapiro

df = pd.read_csv("breast_cancer_1000_genes.tsv", sep="\t", index_col=0)
my_list = []
for i in df.index:
    if shapiro(df.loc[i]).pvalue > 0.05: # если условие выполняется, заполняем список
        my_list.append(i)
percentage = (len(my_list) / len(df.index)) * 100
print(percentage, '%')