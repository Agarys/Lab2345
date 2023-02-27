# 3.1
# A=int(input("A="))
# B=int(input("B="))
# for i in range(A, B+1):
#     print(i)

# 3.2

# A = int(input("A: "))
# B = int(input("B: "))
#
# if A < B:
#     for i in range(A, B+1):
#         print(i)
# else:
#     for i in range(A, B-1, -1):
#         print(i)

# 3.3
# A = int(input("A:"))
# B = int(input("B:"))
# for i in range(A - (A + 1) % 2, B - B % 2, -2):
#     print(i, end=' ')

# 3.4
# N = int(input("N:"))
# sum = 0
# for i in range(1, N + 1):
#     sum += i
#
#
# for i in range(N - 1):
#     sum -= int(input())
# print(sum)




# lab4

# 4.1
# s = input()  # 输入字符串
# n_upper = 0  # 大写字母数
# n_lower = 0  # 小写字母数
#
# # 计算一行中大写和小写字母的数量
# for c in s:
#     if c.isupper():
#         n_upper += 1
#     elif c.islower():
#         n_lower += 1
#
# # 将字符串转换为正确的寄存器
# if n_lower >= n_upper:
#     print(s.lower())
# else:
#     print(s.upper())


# 4.2
# while True:
#     num1 = input("Бірінші санды енгізіңіз: ")
#     num2 = input("Екінші санды енгізіңіз: ")
#
#     if num1.isdigit() and num2.isdigit():
#         # Жолдарды бүтін сандарға түрлендіру және қосындыны есептеу
#         sum = int(num1) + int(num2)
#         print("Сандардың қосындысы:", sum)
#         break  # Ілмектен тыс
#     else:
#         print("Енгізу қате. Тағы да көр.")


# lab 5

# 5.1
# 为学生创建一个空列表
# students = []
#
# # 请求有关学生的信息并将其添加到列表中
# while True:
#     name = input("输入学生的姓氏（或“停止”以完成输入）： ")
#     if name == "停":
#         break
#     grade = int(input("输入学生的班级： "))
#     students.append((name, grade)) # 将元组（姓氏、类）添加到列表中
#
# # 按升序类对列表进行排序
# students.sort(key=lambda x: x[1])
#
# # 打印出姓氏和类别列表
# for student in students:
#     print(f"{student[0]} - {student[1]} класс")


# 5.2
# student_grades = {
#     'Alice': {'Math': 90, 'Science': 85, 'Art': 95},
#     'Bob': {'Math': 80, 'Science': 75, 'Art': 85},
#     'Charlie': {'Math': 95, 'Science': 90, 'Art': 80},
#     'David': {'Math': 70, 'Science': 80, 'Art': 75}
# }
#
# def check_grade(student_name):
#     if student_name in student_grades:
#         grades = student_grades[student_name]
#         print(f"{student_name}'s grades:")
#         for subject, grade in grades.items():
#             print(f"{subject}: {grade}")
#     else:
#         print(f"{student_name} is not in the student list.")
#
#
# name = input("Enter a student's name: ")
# check_grade(name)

# 5.3
# values = []  # 创建一个空列表来保存值
# while True:
#     value = int(input("输入一个整数（0 表示完成输入）： "))
#     if value == 0:  # 如果用户输入了零，那么我们中断循环
#         break
#     values.append(value)  # 将输入的值添加到列表中
#
# sorted_values = sorted(values)  # 对列表进行排序
#
# print("排序数字：")
# for value in sorted_values:
#     print(value)  # 在单独的行上显示每个值


# 5.4
# numbers = []
# while True:
#     num = int(input("输入一个整数（或 0 以完成输入）： "))
#     if num == 0:
#         break
#     numbers.append(num)
#
# numbers.sort(reverse=True)
# print("按降序输入的值：", numbers)

# 5.5
# import random
#
# numbers = []
# while len(numbers) < 6:
#     new_number = random.randint(1, 49)
#     if new_number not in numbers:
#         numbers.append(new_number)
#
# numbers.sort()
# print(numbers)

# 5.6
def is_sorted(lst):
    return lst == sorted(lst) or lst == sorted(lst, reverse=True)
# 要求用户提供列表的数字序列
lst = input("输入以空格分隔的数字序列： ").split()
lst = [int(x) for x in lst]

# 检查列表是否排序并输出消息
if is_sorted(lst):
    print("列表已排序。")
else:
    print("列表未排序。")

