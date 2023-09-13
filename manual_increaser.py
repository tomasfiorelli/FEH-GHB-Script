import pandas as pd

df = pd.read_csv('heroes.csv')
df['HM'] += 5
# for i in range(4):
#     if df['HM'][i] > 9000:
#         df['HM'][i] = 9000
df.to_csv('heroes.csv', index=False)