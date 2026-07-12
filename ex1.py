# x=10
# y=0
# try:
#     z=x/y
#     print(z)
# except Exception as e:
#     print(e)
# else:
#     print("runs when no error in try block")
# finally:
#     print("always runs")

# print("last line")

#create a function to divide 2 numbers by passing 2 parameters by handling exception
def div(a,b):
    d=a/b
    return d

c=int(input("Enter the first number: "))
l=int(input("Enter the second number: "))
try:
    f=div(c,l)
    print(f)
except Exception as e:
    print(e)
else:
    print("runs when no error in try block")



