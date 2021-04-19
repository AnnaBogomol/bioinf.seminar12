import scipy.stats
import pandas as pd
import numpy as np

df = pd.DataFrame()
df["X"] = np.linspace(39, 16, 4)
df["Y"] = np.linspace(-41, 17, 4)
St_paired = scipy.stats.ttest_rel(df["X"], df["Y"]) # парный критерий Стьюдента
St_unpaired = scipy.stats.ttest_ind(df["X"], df["Y"]) # непарный критерий Стьюдента
print(St_paired)
print(St_unpaired)

# Результат: Ttest_relResult(statistic=2.2664124766695255, pvalue=0.10828287199118573)
# Ttest_indResult(statistic=2.9422648897977304, pvalue=0.025871434318610304)
