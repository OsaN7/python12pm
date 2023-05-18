hello=open("Students Marks.txt",'a')
hello.write("======= Students Marksheet======== \n")
hello.write("\n")
name=input("Enter your name: ")


eng=int(input("Enter marks of english: "))

nep=int(input("Enter marks of Nepali: "))

mat=int(input("Enter marks of Maths: "))

sci=int(input("Enter marks of Science: "))

soc=int(input("Enter marks of Social: "))


hello.write("\n")

sum=nep+eng+mat+sci+soc
hello.write(f'Students id: {(name)} \n')
hello.write(f"The total marks of English is: {str(eng)} \n")
hello.write(f"The total marks of Nepali is: {str(nep)} ")
hello.write("\n")
hello.write(f"The total marks of maths is: {str(mat)} ")
hello.write("\n")
hello.write(f"The total marks of Science is: {str(sci)} ")
hello.write("\n")
hello.write(f"The total marks of Social is: {str(soc)} \n")
# hello.write("\n")
hello.write(f"The total marks is {str(sum)} \n")

percentage=sum/5
hello.write(f'The percentage is {str(percentage)}')
hello.close()

# data=open("Students Marks.txt","r")
# print(data.read())
