# """Task 1. Even or odd. Прийняти від користувача число, вивезти чи even/odd"""
# num = int(input("Enter a number: "))
# if (num % 2) == 0:
#    print("{0} is Even".format(num))
# else:
#    print("{0} is Odd".format(num))


"""Task 2. When provided with a number between 0-9, return it in words. Input :: 1 Output :: "One"."""
import datetime

#
#
# num = int(input("Enter the number: "))
#
# match num:
# 	case 0:
# 		print("Zero")
# 	case 1:
# 		print("One")
# 	case 2:
# 		print("Two")
# 	case 3:
# 		print("Three")
# 	case 4:
# 		print("Four")
# 	case 5:
# 		print("Five")
# 	case 6:
# 		print("Six")
# 	case 7:
# 		print("Seven")
# 	case 8:
# 		print("Eight")
# 	case 9:
# 		print("Nine")


"""Task 3. Прийняти від користувача два числа і отримати дію над цими числами. Реалізувати +,-, //, , /, *"""

# num1, num2, des = int(input("Введіть число: ")), int(input("Введіть число: ")), input("Введіть дію: ")
#
# match des:
#     case '+':
#         print(f'{num1} + {num2} = {num1 + num2}')
#     case '-':
#         print(f'{num1} - {num2} = {num1 - num2}')
#     case '*':
#         print(f'{num1} * {num2} = {num1 * num2}')
#     case '/':
#         print(f'{num1} / {num2} = {num1 / num2}')
#     case '//':
#         print(f'{num1} // {num2} = {num1 // num2}')
#     case '**':
#         print(f'{num1} ** {num2} = {num1 ** num2}')
#     case _ :
#         print('Try again!')


# """Task 4. Прийняти від користувача name, surname. Вивезти ініціали."""
# name = str(input("Введіть ім'я: "))
# surname = str(input("Введіть прізвище: "))
#
# print("Name: " + name + ", " + "Surname: " + surname + "," + " Init: " + name[0] + "." + surname[0] + ".")

"""Practice section 2"""

# month = str(input("Input the month: "))
# if month in ["december", "january", "february"]:
# 	print("The season is winter")
# elif month in ["march", "april", "may"]:
# 	print("The season is spring")
# elif month in ["june", "july", "august"]:
# 	print("The season is summer")
# elif month in ["september", "october", "november"]:
# 	print("The season is autumn")
# else:
# 	print("Input the correct month")


# year = int(input("Input a year: "))
# month = int(input("Input a month: "))
# day = int(input("Input a day: "))
#
# date = datetime.date(year, month, day)
# date += datetime.timedelta(days=1)
#
# print("Next day: " + str(date))

"""OR"""

# year = int(input("Input a year: "))
# month = int(input("Input a month: "))
# day = int(input("Input a day: "))
# if((year % 4==0) and (year % 100 !=0) or (year % 400==0)):
#     l = 1
# else:
#     l = 0
# EndOfMonth = False
# # перевіряємо місяці на 31 день
# if (((month==1) or (month==3) or (month==5) or (month==7) or (month==8) or (month==10) or (month==12)) and (day==31)):
#     EndOfMonth=True
# # перевіряємо місяці на 30 днів
# if (((month==4) or (month==6) or (month==9) or (month==11)) and (day==30)):
#     EndOfMonth = False
# # перевіряємо лютий
# if ((month==2) and (l==1) and (day==29)):
#     EndOfMonth = False
# if ((month==2) and (l==0) and (day==28)):
#     EndOfMonth = True
# #перевіряємо грудень
# if ((month==12) and (day==31)):
#     day = 1
#     month = 1
#     year = year + 1
# elif (EndOfMonth):
#     day = 1
#     month = month + 1
# else:
#     day = day + 1
# print("The next date is ", day, ".", month, ".", year)




# phrase = str(input("Enter a phrase: "))
# if len(phrase) > 5:
# 	print("The len of phrase is longer than 5")
# elif len(phrase) == 5:
# 	print("The len of phrase is equal 5")
# else:
# 	print("The len of phrase is shorter than 5")


# num = int(input("Enter the Number: "))
# i = 1
# while i <= num:
#     if num % i == 0:
#         print(i)
#     i = i+1
#
# print("\nFactors of", num)


# print("Input lengths of the triangle sides: ")
# x = int(input("x: "))
# y = int(input("y: "))
# z = int(input("z: "))
#
# if x == y == z:
# 	print("Equilateral triangle")
# elif x==y or y==z or z==x:
# 	print("Isosceles triangle")
# else:
# 	print("Scalene triangle")


"""Practice section 3"""

# for i in range(2, 10, 1):
#     print(i)



# iteration = 2
# while iteration <= 10:
# 	print(iteration)
# 	iteration += 1
#
# print('End')


# number = input('Input number: ')
# iter = input('Input number of iteration: ')
# if number.isdigit() and iter.isdigit():
#     num = int(number)
#     iter = int(iter)
#     for i in range(iter):
#         num *= 2
#         print(num)
# else:
#     print('Wrong input')



# n = int(input("Enter the number of iterations: "))
# a = 1
# b = 1
# print(a)
# print(b)
# for i in range(2, n):
#     c = a + b
#     print(c)
#     a = b
#     b = c


# num = int(input("Enter a number: "))
# reverse_num = 0
#
# while num > 0:
#     remainder = num % 10
#     reverse_num = (reverse_num * 10) + remainder
#     num = num // 10
#
# print("The reverse of the number is:", reverse_num)

"""Practice section 4"""


# while True:
#     user_input = input("Enter something (or 'q' and 'Q' to quit): ")
#
#     if user_input.lower() == 'q':
#         print("Exit")
#         break
#
#     print("You entered:", user_input)


# for i in range(101):
#     if i % 3 == 0:
#         print(i)


# num = int(input("Enter a number: "))
# for i in range(num + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("foobar")
#     elif i % 3 == 0:
#         print("foo")
#     elif i % 5 == 0:
#         print("bar")
#     else:
#         print(i)


letter = input()
def counter(letter):
    counter = 0
    for i in letter:
        if i in ('a', 'e', 'i', 'o', 'u'):
            counter += 1
    return counter
counter(letter)
print(counter(letter))