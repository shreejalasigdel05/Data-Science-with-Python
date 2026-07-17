#file handling
#write mode

# file=open("test.txt",'w')
# file.write("I like python \n")
# file.write("I am taking a class of data science \n")
# file.write("World cup finale is coming on monday\n")
# file.close()
# print("File added successfully")

#create another file, take name and age as a user input and print it into a file
file=open("input.txt",'w')
name=input("Enter your name: ")
age=int(input("Enter your age: "))
file.write(f"Name: {name}\n")
file.write(f"Age: {age}")
file.close()
print("File added successfully")