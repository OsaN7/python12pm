#            OOP?
# Object::

#       EXAMPLE  

# class students:
#     name='ram'
#     age=34
    
#     def student_info(self):
#         print("Name:", self.name)
#         print("Age: ", self.age)
    
# obj=students()
# obj.student_info()



# class SI:
#     p=int(input("Enter principle: "))
#     t=int(input("Enter Time: "))
#     r=int(input("Enter Rate: "))
#     a=(p*t*r)/100

#     def si(self):
#         print("SI: ",self.a)
# obj=SI()
# obj.si()


# class Calculator:
    # def add(self,x,y):

#         return x+y
    
#     def sub(self,x,y):
#         return x-y
    
#     def mult(self,x,y):
#         return x*y
    
# obj=Calculator()
# print(obj.add(2,4))
# print(obj.sub(2,4))
# print(obj.mult(2,4))



# class Students:
#     data = [
#         {'name': 'ram', 'age': 34, 'address': 'ktm'},
#         {'name': 'shyam', 'age': 34, 'address': 'ktm'},
#         {'name': 'hari', 'age': 34, 'address': 'ktm'},
#     ]
#     def show(self):
#         x = 0
#         take_value = len(self.data)
#         while x != take_value:
#             print(f"Name: {self.data[x]['name']} age: {self.data[x]['age']} address {self.data[x]['address']}")
#             x += 1

# obj = Students()
# obj.show()

# property,method,constructor

# class College:
#     students=[]
#     def add_students(self):
#         self.name=input("Enter your name: ")
#         self.email=input("Enter your email: ")
#         self.address=input("Enter your address: ")
#         self.students.append(self.name)
#         self.students.append(self.email)
#         self.students.append(self.address)


#     def show_students(self):
#         print(self.students)
    
# obj=College()
# obj.add_students()
# obj.show_students()

# def funargs(normal, *args,**kwargs):
#     print(normal)
#     for item in args:
#         print(item)
#     print("\n Now I would like to intro some of our Hero's")

#     for key, value in kwargs.items():
#         print(f"{key} is a  {value}")

# obj=['ram','shyam','hari',"gita","sita"]
# normal="I am a normal Argument and student"
# kw={"Name":"Ram","Class":"9"}
# funargs(normal,*obj,**kw) 

# class Employee:
#     def __init__(self,name, id ):
#         self.name=name
#         self.id=id
#     def showDetails(self):
#         print(f"The name of employee: {self.name} is {self.id}")

# class Programmer(Employee):
#     def showLanguage(self):
#         print("The default language is Python")

# e=Employee("Rohan Das", 420)
# e.showDetails()
# e2=Programmer("harry Das", 410)
# e2.showDetails()
# e2.showLanguage()