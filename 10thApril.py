# while loop
#       used to iterate over and test expression (condition) is true
# syntax:
# while test_expression:
# Body of while

# example::
# x = 1
# while x <= 10:
#     print(x)
#     x += 1


# x=1
# even=0
# odd=0
# while x <=10:
#         if x % 2==0:
#             even +=1
#         else:
#             odd+=1
#             x+=1

# print(f'even is: {even}')
# print(f'odd is: {odd}')

# users=['ram','sita','ram','ram']
# # for user in users:
# #     if user=='ram':
# #         print(user)

#                 # while
# x=0
# while x<len(users):
#         if users[x]=='ram':
#             print(users[x])
#             x+=1

# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# even = 0
# for num in number:
#     if num % 2 == 0:
#         print(num)

# lOOP 
# x = 0
# while x < len(number):
#     if number[x] % 2 == 0:
#         print(number[x])
#     x += 1

# num_time=int(input("enter numb of times: "))
# increment=1
# rep_number=[]
# list=[]

# while increment <= num_time:
#     number=int(input("enter a numb: "))
#     if not number in rep_number:
#         rep_number.append(number)
#     else:
#       list.append(number)

#     increment+=1

# print(list)

# for i in range(11):
#     print("2 X",i,"=",2*i)

# for i in range(11):
#     print("3 X",i,"=",3*i)
#     print()
# for i in range(11):
#     print("4 X",i,"=",4*i)
# for i in range(11):
#     print("5 X",i,"=",5*i)
# for i in range(11):
#     print("6 X",i,"=",6*i)
# for i in range(11):
#     print("7 X",i,"=",7*i)
# for i in range(11):
#     print("8 X",i,"=",8*i)
# for i in range(11):
#     print("9 X",i,"=",9*i)
# for i in range(11):
#     print("10 X",i,"=",10*i)


# number=int(input("enter number which you want: "))
# print("The multiplcation tabile is", number)
# for count in range(1,11):
#     print(number, "X",count,'=', number*count)