#read mode

# file=open('test.txt','r')
# ap=open('test.txt','a') #append mode
# ap.write("We live in tech era\n")
# ap.write("Hello guys \n")
# print(file.read())
# ap.close()
# s=1
# lines=file.readlines()
# for line in lines:
#     print(s,line.strip())
#     s=s+1

#for deleting 
import os
if os.path.exists("test.txt"):
    os.remove("test.txt")
else:
    print("The file does not exist")