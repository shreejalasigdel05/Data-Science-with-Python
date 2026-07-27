import pandas as pd
#Seriess
# ser=pd.Series()
# print(ser)
# s=pd.Series([10,20,30,40])
# print(s)
# print(s[2])

# p=pd.Series([50,60,70], index=['potato','tomato','onion'])
# print(p)
# print(p['potato'])

# mark=[40,50,60]
# name=["Kali","Sanu","Prayu"]
# s=pd.Series(mark,index=name)
# print(s)
# print(s.ndim)


s=pd.Series([10,25,30,40,50])
# print(s[s>30])
# print(s[s>10]&s[s<50])
# print(s.max())
# print(s.mean())
# print(s.min())
# print(len(s))

for i in s:
    print(i)
      

# a={'Name':['Kali','Sanu','Prayu'],'Marks':[50,70,60]}
# p=pd.Series(a)
# print(p)