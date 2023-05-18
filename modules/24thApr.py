# from calulator import add, sub, mul
# # from calulator import *

# print(add(5,10))
# print(sub(20,10))
# print(mul(5,2))


# import datetime
# b_date= datetime.date(2023, 5,12)
# today= datetime.date.today()
# print(b_date - today)

# import datetime
# holi= datetime.date(2023, 3,28)
# today= datetime.date.today()
# print(today - holi)

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