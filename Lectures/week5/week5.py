import pandas as pd

d = ['c', 'd', 'e']

a = ['1', '2', '3']

b = ['4', '5', '6']

c_1 = pd.Series(data=a, index=d)

c_2 = pd.Series(data=b, index=d)

df = pd.DataFrame({'a': c_1, 'b': c_2})

print(df)
