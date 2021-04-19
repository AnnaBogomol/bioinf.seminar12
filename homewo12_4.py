import pandas as pd
from scipy.stats import ttest_rel, ttest_ind

df = pd.read_csv('colon_cancer_tumor_vs_normal_paired_FPKM.tsv', sep = '\t', index_col = 0) # создали датафрейм
print(df)
df["St_paired"] = [ttest_rel(df.loc[gene].iloc[0:5], df.loc[gene].iloc[5:10])[1] for gene in df.index]
df["St_unpaired"] = [ttest_ind(df.loc[gene].iloc[0:5], df.loc[gene].iloc[5:10])[1] for gene in df.index]
df_paired = df["St_paired"]
df_unpaired = df["St_unpaired"]
df_paired = df_paired[df_paired < 0.05].sort_values() # отсортировали значения для парного и непарного критерия стьюдента
df_unpaired = df_unpaired[df_unpaired < 0.05].sort_values()
print(len(df_paired)) # посчитали число дифференциально экспрессированных генов
print(len(df_unpaired))
top10_paired = df_paired.head(10) # нашли топ-10
top10_unpaired = df_unpaired.head(10)
print(top10_paired)
print(top10_unpaired)
print("RNF112, ITM2A, SPTBN2") # общие гены для двух списков
