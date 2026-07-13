# ls=[1,3,4,5,6]
# print(type(ls))
# print(ls)
# print(ls[0])
# print(ls[3])
# print(len(ls))
# sum=0
# for i in ls:
#     sum=sum+i
# print("the sum is",sum)

# names=['ritu','renuka','shree','prayu','sanu']
# print(type(names))
# print(names)
# print(names[0])
# print(names[3])
# print(len(names))
# for n in names:
#     print(n)
# print(names[1:4])
# print(names[-4])

a=[1,2,3]
b=[4,5,6]
c=a+b
# print(c)

# r=7 in c
# print(r)
# del c[2] #for deletion
# print(c)
# print(c)
# del c[1:4]
# print(c)
# c[1]=10
# print(c)

# ls=[2,3,5,6,1]
# print(sum(ls))
# print(min(ls))
# print(max(ls))
# c=0
# for i in ls:
#     c=c+1
# print(c)

# ls=[1,2,3,4,5,6,7,8,9]
# ls.append(12)
# print(ls)
# even=[]
# for i in ls:
#     if i%2==0:
#         even.append(i)
# print(even)

#pass list to a function

# def hello(l):
#     for i in l:
#         print(i)

# fruits=['apple','banana','mango']
# hello(fruits)

#return heterogenous from list from a function

def n1():
    ls=['apple',3,'mango','True',6,9]
    return ls

result=n1()
print(result)
    
