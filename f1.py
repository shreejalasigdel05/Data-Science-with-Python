# def hi():
#     print("Hi, how are you?")
#     print("I am fine and you?")

# hi() #call

# def sum():
#     x=8;   
#     y=9;
#     z=x+y;
#     print("sum is",z)

# sum()

# def area(l,b):
#     ar=l*b
#     return ar

# a=area(3,4)
# print(a)
# h=6
# vol=a*h
# print(vol)

# def SI(p,t,r):
#    si=(p*t*r)/100
#    return si

# a=int(input("Principle: "))
# b=float(input("Time: "))
# c=int(input("Rate: "))
# i=SI(a, b,c)
# print("The simple interest is",i)

# def arvol(l,b,h):
#     ar=l*b
#     vol=ar*h
#     return ar,vol

# a,v=arvol(6,4,5)
# print('area is',a)
# print('volume is',v)

#Lambda function
# addfive=lambda x: x+5
# print(addfive(2))
# print(addfive(3))
# print(addfive(7))
# print(addfive(8))

# addnum=lambda x,y: x+y
# a=(addnum(10,20))
# a=a-10
# print(a)

# area=lambda l,b:l*b
# print("The area is",area(5,4))

#Write a function to calculate the sum of even numbers and return it
def sum():
    total=0
    for i in range(1,10):
        if(i%2==0):
            total+=i
    return total

s=sum()
print('even sum is',s)

 