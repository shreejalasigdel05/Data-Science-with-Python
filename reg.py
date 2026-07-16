#regular expression
import re

# st='''Santosh is 22 years old and Dipika is 11 years old Umesh is 43 years old, Samrat is 5 years old, 
# Shrijal is 111 years old'''

# ages=re.findall(r'\d{1,3}',st)  #to print only ages
# print(ages)

# names=re.findall(r'[A-Z][a-z]*',st) #to print only names by checking the upper case letters
# print(names)
# names=re.findall(r'[A-Z][a-z]*',st) to print only the first letter of the name

# nameAgedict={}
# x=0
# for name in names:
#     # print(name)
#     nameAgedict[name]=ages[x]
#     x=x+1
# print(nameAgedict)

#mobile phone validation
# mob=input("Enter your mobile number: ")
# reg=re.fullmatch('[7-9][0-9]{9}',mob)
# if reg!= None:
#     print("valid mobile no.",mob)
# else:
#     print("Invalid mobile number format")

#email validation
# email=input("Enter the email: ")
# reg=r'\b[A-Za-z0-9_.+-]+@[A-Za-z0-9]+\.[a-zA-Z0-9-.]+$'
# print(re.match(reg,email))
# if re.match(reg,email):
#     print("Valid email",email)
# else:
#     print("Invalid email")

#function email passing as parameter, and using re we have to check it

# def email(e):
#     reg=r'[A-Za-z0-9_.+-]+@[A-Za-z0-9]+\.[a-zA-Z0-9-.]+$'
#     if re.match(reg,e):
#         print("Valid email",e)
#     else:
#         print("Invalid email")

# em=input("Enter the email: ")
# email(em)

def num(n):
    reg=re.fullmatch(r'[7-9][0-9]{9}',n)
    if reg!= None:
        print("valid mobile no.",n)
    else:
        print("Invalid mobile number format")
number=input("Enter the number: ")
num(number)