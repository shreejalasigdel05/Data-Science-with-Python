# d={}
# d={"name":"rakesh","salary":50000,"age":35}
# print(d)
# name=d["name"]
# print(name)
# sal=d["salary"]
# print(sal)

# for k,v in d.items():
#     print(f'key is {k}.....value is {v}')

# sal=d['salary']-(d["salary"]*10/100)
# print(sal)

# for k,v in d.items():
#     if k == "salary":
#         sal=v*0.1
#         print("sal 10%",sal)

# d['company']="google"
# print(d)

# del d['age']
# print(d)

# dt=dict([('name','prayusha'),('id',10),('subject','python')])
# print(dt)

# for k,v in dt.items():
#     if k=='id':
#         continue
#     print(k,'....',v)

# d3=dict(Name='Dipika',Age=6)
# print(d3)

#take a user input for name, course, fee for the dictionary
# ds={}
# ds['name']=input("Enter the name: ")
# ds['course']=input("Enter the course: ")
# ds['fee']=float(input("Enter the fee: "))
# print(ds)

def student(name,course,fee):
    ds={
        "name":name,
        "course":course,
        "fee":fee
    }
    return ds

n=input("Enter the name: ")
c=input("Enter the course: ")
f=float(input("Enter the fee: "))

d=student(n,c,f)
print(d)




