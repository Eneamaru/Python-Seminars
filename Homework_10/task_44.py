import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

one_hot = pd.pivot_table(data, index=data.index, columns='whoAmI', aggfunc=len, fill_value=0)
one_hot.columns = [''.join(col).strip() for col in one_hot.columns.values]

one_hot.head()