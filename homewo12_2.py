import scipy.stats
import pandas as pd
import numpy as np

df = pd.DataFrame() # пустой датафрейм
df["X"] = np.linspace(34, 56, 89)
df["Y"] = df["X"].add(1)
St_paired = scipy.stats.ttest_rel(df["X"], df["Y"]) # парный критерий Стьюдента
St_unpaired = scipy.stats.ttest_ind(df["X"], df["Y"]) # непарный критерий Стьюдента
print(St_paired)
print(St_unpaired)

# Результат: Ttest_relResult(statistic=-inf, pvalue=0.0)
# Ttest_indResult(statistic=-2.065591117977289, pvalue=0.04033267519119943)
