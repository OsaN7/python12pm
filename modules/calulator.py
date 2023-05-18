# def add(a,b):
#     return a+b

# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b


# import datetime
# students = [
#     {'name': 'ram', 'birth_date': '2023-05-12'},
#     {'name': 'shyam', 'birth_date': '2023-03-12'},
#     {'name': 'hari', 'birth_date': '2023-04-24'}
# ]
# x = 1
# num = int(input("enter no of times: "))
# while x <= num:
#     name = input("Enter your name: ")
#     date = input("Enter your date: ")
#     datee = [['name', f'{name}'], ['birth_date', f'{date}']]
#     datee = dict(datee)
#     students.append(datee)
#     x += 1

# for stu in students:
#     today = datetime.date.today()
#     b_date = datetime.datetime.strptime(stu['birth_date'], '%Y-%m-%d').date()
#     if today > b_date:
#         day = today-b_date
#         print(f"{stu['name']} {day.days} days passed his bday")
#     elif today == b_date:
#         print(f"{stu['name']}  has his birthday today")
#     else:
#         day = b_date-today
#         print(f"{stu['name']} {day.days} has not passed his birthday")

# print(b_date)

# course='python programming'
# data={}
# for n in course:
#     if n in data:
#         data[n]=1
#     else:
#         data[n]=1
# print(data)

# data = [
#     {'name': 'ram', 'gender': 'male'},
#     {'name': 'sophia', 'gender': 'female'},
#     {'name': 'rita', 'gender': 'female'},
# ]
# total_male=0
# total_female=0
# for user in data:
#     if user['gender']=='male':
#         total_male+=1
#     else:
#         total_female+=1
# print(total_male)
# print(total_female)

# data=[]
# x=1
# num=int(input("Enter number: "))
# while x<=num:
#     name=input("Enter your name: ")
#     gender=input("Enter your gender: ")
#     new_dat={'name':name,'gender': gender}
#     data.append(new_dat)
#     x+=1
# male=0
# female=0
# for n in data:
#     if n['gender']=='male':
#         male+=1
#     else:
#         female+=1

# print(male)
# print(female)

# data=[
#     [1,2,3,4],
#     [5,6,7,8],
#     [5,4,3]
# ]
# total=0
# for n in data:
#     for k in n:
#         total+=1
# print(total)

