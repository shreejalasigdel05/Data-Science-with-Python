import pandas as pd

df = pd.DataFrame({
    'Name': ['Kali', 'Prayu', 'Sanu', 'Don','Uma','Neha','Laila'],
    'Marks': [60, 70, 80, 70,40,30,50]
})

# print(df)
# print(df.ndim)
# print(type(df))
print(df.head)
print(df.tail)