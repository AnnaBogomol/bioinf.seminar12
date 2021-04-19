import pandas as pd
from scipy.stats import shapiro

df = pd.read_csv("breast_cancer_1000_genes.tsv", sep="\t", index_col=0)
my_list = []
for i in df.index:
    if shapiro(df.loc[i]).pvalue > 0.05: # если условие выполняется, заполняем список
        my_list.append(i)
percentage = (len(my_list) / len(df.index)) * 100
print(percentage, '%')
