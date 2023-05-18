users = [
    {'name': 'ram', 'address': 'kathmandu', 'age': 20, 'gender':'male'},
    {'name': 'hari', 'address': 'bhaktapur', 'age': 30, 'gender':'male'},
    {'name': 'sita', 'address': 'lalitpur', 'age': 40 ,'gender':'male'}
]


# for n in users:
        # for x in data:
name=input("Enter your name: ")
address=input("Enter your address: ")
age=int(input("Enter your age: "))
gender=input("Enter your gender: ")
users.append(f'name: {name}')
users.append(address)
users.append(age)
users.append(gender)
print(users)
