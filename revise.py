# print('osan')
# a=12
# b=12
# c=a*b
# print(c)
# name="Osan"

# location="Maharajgunj"
# print(f"my name is {name}, Im from {location}")


# message = 'ram ram sita gita gita hari hari hari hari gopal'
# # print(message.split())
# def check_repeat(text):
#   data ={}
#   for word in text.split():
#     if word in data:
#       data[word]+=1
#     else:
#       data[word] = 1
#   return data
# print(check_repeat(message))

# def repetition():
#   pass
#   data = check_repeat(message)
#   y = []
#   for word in data:
#     x = data[word]
#     y.append(x)
#   a = y[0]
#   b = y[0]
#   c = y[0]
#   d = []
#   for num in y:
#     if num > a:
#         a = num
#     elif num < b:
#         b = num
#     elif num == c:
#         c = num
#         d.append(c)
#   for word in data:
#     if data[word] == a:
#       print(f"most repeated variable: {word}")
#     elif data[word] == b:
#       print(f"least repeated variable: {word}")
#     elif data[word] == c:
#       print(f"equally repeated variable: {word}")
# repetition()


# course = "python programming"
# data = {}
# not_repeated = []
# repeated = []
# for a in course:
#   if a in data:
#     data[a]+=1
#   else:
#     data[a]=1
# for key,value in data.items():
#   if value == 1:
#     not_repeated.append(key)
#   # if key == " ":
#   #   not_repeated.remove(key)
#   elif value>1:
#     repeated.append(key)
# for x in not_repeated:
#   print("not repeated: ",x)
# for x in repeated:
#   print("repeated: ",x)
# print(data)



# course='python programming'
# data={}
# for n in course:
#     if n in data:
#         data[n]+=1
#     else:
#         data[n]=1
# print(data)


# course='python programming'
# data=[]
# def not_repitation(text):
#     for n in course:
#        data.append(n)

#     for y in data:
#         if data.count(y)==1:
          
#           print(y)
#           return data
#
    

# data=[
#     [1,2,3,4],
#     [5,6,7,8],
#     [5,4,3]
# ]
# total=0
# # for num in data:   
# #     for n in num:
# #      total+=n
# print(total)

# numbers=[1,2,3,4,5,6,7]
# sum=0
# for n in numbers:
#     sum+=n
# print(sum)
# users = [
#     {'name': 'ram', 'address': 'kathmandu', 'age': 20, 'gender':'male'},
#     {'name': 'hari', 'address': 'bhaktapur', 'age': 30, 'gender':'male'},
#     {'name': 'sita', 'address': 'lalitpur', 'age': 40 ,'gender':'male'}
# ]

# name=input("Enter your name: ")
# address=input("Enter your address: ")
# age=int(input("Enter your age: "))
# gender=input("Enter your gender: ")

# data = [['name', f'{name}'], ['address', f'{address}'], ['age', age], ['gender', f'{gender}']]
# data = dict(data)

# users.append(data)


# print(users)


# for user in users:
#     print(f"Name is {user['name']} address {user['address']} {user['age']}")

# data={'name':'ram','address':'kathmandu','age':20}
# print(f"Name is {data['name']} from {data['address']} age {data['age']}")

# users = [
#     {'name': 'ram', 'address': 'kathmandu', 'age': 20, 'gender':'male'},
#     {'name': 'hari', 'address': 'bhaktapur', 'age': 30, 'gender':'male'},
#     {'name': 'sita', 'address': 'lalitpur', 'age': 40 ,'gender':'male'}
#    ]

# for user in users:
#  print(f"Name is {users['name']} from {users['address']} age {users['age']} gender is {users['gender']}")

# data=[
#     ['ram', 'sita', 'hari'],
#     ['gita', 'hira', 'mina'],
#     ['rita', 'suresh', 'mahesh'],
#     ['sophiya', [[[['python']]]], 'sara']
# ]
# print(data[3][1][0][0][0][0])

# data=['ram','sita']
# data.append("hari")
# print(data)

# data=['ram', 'sita'];
# data[0]= 'hari';
# data.append("hari")
# print(data)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# even=0
# odd=0
# for num in numbers:
#     if num%2==0:
#         even+=1
#     else:
#         odd+=1

# print(f"The even is {even}")
# print(f"The odd is {odd}")

# data = ['ram', 'shyam', 'hari', 'gita', 'ram', 'ram', 'gita']
# ram=0
# for nam in data:
#     if nam=='ram':
#         ram+=1
# print(ram) 

# data = [
#     ['ram', 'shyam', 'hari', 'gita'],
#     ['sophia', 'sara', 'susan', 'sophie'],
#     ['john', 'james', 'jim', 'joe']
# ]
# for user in data:
#     for name in user:
#         print(name)

# num=int(input("Enter no: "))
# names=[]
# for i in range(num):
#     name=input("Enter you name: ")
#     names.append(name)

# for n in names:
#     print(n)
