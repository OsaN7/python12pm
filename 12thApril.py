# data = [
#     {
#         'name': 'ram',
#         'address':
#             {
#                 'city': 'kathmandu',
#             }
#     },
#     {
#         'name': 'sita',
#         'address': {
#             'city': 'bhaktapur',
#         }
#     },
#     {
#         'name': 'hari',
#         'address': {
#             'city': 'lalitpur',
#         }
#     },
# ]
# # print(data[0]["address"]["city"])
# print('My name is',data[0]['name'],"from",data[0]["address"]["city"]) 
# print('My name is',data[1]['name'],"from",data[1]["address"]["city"]) 
# print('My name is',data[2]['name'],"from",data[2]["address"]["city"]) 

#                          OR
# x=0
# while x<=1:
#     for user in data[0]:
#         print(f'My name is{user['name']}city:{user["address"]["city"]}  
        
    # for user in data[1]:
#       print('My name is',data[1]['name'],"from",data[1]["address"]["city"]) 
#     for user in data[2]:
#       print('My name is',data[2]['name'],"from",data[2]["address"]["city"]) 
#     x+=1
#                            OR 

# print(f"Name: {user['name']} City: {user['address']['city']}")
#                           OR  
# increment=0
# name = {}
# addres = {}
# city = {}
# for user in data:
#     name = data[increment]['name']
#     city = data[increment]['address']['city']
#     print(f"My name is {name} and city is {city}")
#     increment +=1


# data = [
#     {'name': 'ram', 'gender': 'male', 'status': True},
#     {'name': 'sophia', 'gender': 'female', 'status': False},
#     {'name': 'rita', 'gender': 'female', 'status': True},
#     {'name': 'laxmi', 'gender': 'female', 'status': True},
#     {'name': 'kabita', 'gender': 'female', 'status': True},
#     {'name': 'gopal', 'gender': 'male', 'status': False},
# ]

# total_users=0
# total_active_users=0
# total_inactive_users=0
# total_active_male=0
# total_inactive_male=0  
# total_active_female=0
# total_inactive_female=0
# increment=0
# for users in data:
#     increment+=1
#     if users['status']==True:
#         total_active_users+=1
#     else:
#         total_inactive_users+=1

#     if users['gender']=="male":
#         total_active_male+=1
#     else:
#         total_active_female+=1

#     if users['gender'] =="male"and users["status"]==False:
#         total_inactive_male+=1
#     elif users['gender']=="female" and users['status']==False:
#         total_inactive_female+=1

# print(f"total active users is:",total_active_users)
# print(f"total inactive users is:",total_inactive_users)
# print(f"total active male is:",total_active_male)
# print(f"total active female is:",total_active_female)
# print(f"total inactive male is:",total_inactive_male)
# print(f"total inactive female is:",total_inactive_male)
# print(f'toal users:',increment)



# number = [1, 29, 3, 4, 5, 6, 78, 88, 9, 10]

# largest_number = number[0]
# smallest_number =  number[0]
# for num in number:
#     if num > largest_number:
#         largest_number = num
#     if num < smallest_number:
#         smallest_number = num

# print(f"Largest number: {largest_number}")
# print(f"Smallest number: {smallest_number}")
