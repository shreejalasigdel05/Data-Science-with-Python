# #set
# s={2,3}
# print(type(s))

# s1={20,10,40,30,40,20}
# print(s1)
# print(next(iter(s1)))

# days={'Sunday','Monday','Tuesday'}
# days.add('Wednesday')
# print(days)
# for i in days:
#     print(i)

# s1={5,6,7,8}
# s4={7,6,8,4}
# print(s4.issubset(s1))
# un=s1.union(s4)
# print(un)
# inter=s1.intersection(s4)
# print(inter)
# l=s4.difference(s1)
# print(l)

# s1={5,6,7,8,9}
# s2={7,8,9,10}
# sd=s1.symmetric_difference(s2)
# print(sd)

#write the function to pass two set as a parameter and return the symmetric difference between them

def diff(a,b):
    s=a.symmetric_difference(b)
    return s

c={1,2,4,5}
d={5,3,4,8}
result=diff(c,d)
print(result)