"""Practice chapter 2"""
# print('"Accept who you are. Unless you’re a serial killer." (Ellen DeGeneres, Seriously… I’m Kidding»).')
#
# print('Take the first step in faith. You don’t have to see the whole staircase, just take the first step')

# print('«No longer chasing butterflies,\nCamila and I planted our garden so they could come to us.»\n(Matthew Mcconaughey).')

# print("Fake It Until You Make It!\
# 	Act As If You Had All The Confidence You Require Until It Becomes Your Reality.\
# 	(Brian Tracy).")

"""Practice chapter 3"""
# a = str(input())
# print(len(a))
#
# b = str(input())
# print(a + b)
#
# print(a + " " + b)

# text = str(input())
# print(text == text[::-1])

# var = "Мені 10 років"
# print(var)
# var_list = list(var)
# var_list[5] = "2"
# var_list[6] = "7"
# var_new = ''.join(var_list)
# print(var_new)

# var = "Мені 10 років"
# print(var)
# x = var.replace("10", "27")
# print(x)

"""Practice chapter 4"""

# name = str(input())
# age = str(input())
# print("Your name is " + name + " and your " + age + " years old")
# print('Your name is {0} and your {1} years old'.format(name, age))
# print(f'Your name is {name} and your {age} years old')

"""Practice chapter 5"""
# string_1 = "Animals  "
# string_2 = "  Badger"
# string_3 = "honey bee"
# string_4 = "   HoneyPot   "
# print(string_1.lower(), string_2.lower(), string_3.lower(), string_4.lower())
# print(string_1.upper(), string_2.upper(), string_3.upper(), string_4.upper())
# print(string_1.lstrip(), string_2.lstrip(), string_3.lstrip(), string_4.lstrip())
# print(string_1.rstrip(), string_2.rstrip(), string_3.rstrip(), string_4.rstrip())
# print(string_1.strip(), string_2.strip(), string_3.strip(), string_4.strip())

# string_1 = "Bear"
# string_2 = "bear"
# string_3 = "BEAR"
# string_4 = "bEar"
#
#
# def start_with(string, search_string = 'be'):
# 	return str(string).startswith(search_string)
#
#
# print(start_with(string_1.lower()))
# print(start_with(string_2.lower()))
# print(start_with(string_3.lower()))
# print(start_with(string_4.lower()))

# var = "Somebody said something to Samantha."
# new_var = var.replace('s', 'x').replace('S', 'X')
#
# print(new_var)

# letter = str(input())
# string_letter = str(input())
# if letter.find(string_letter) != -1:
# 	print("Yes")
# else:
# 	print("No find")



# string_1 = '12345!,_6--'
# print(string_1)
# string_2 = string_1.replace('!', '').replace(',', '').replace('_', '').replace('-', '')
# print(string_2)



# numerator = int(input())
# denominator = int(input())
# quotient = numerator / denominator
# percent = int(quotient * 100)
# print(str(percent) + "%")


# text = 'X!xeXnxiXlX XtxeXrxcXeXsX Xax XsXXtXIX'
# secret_message = text.replace('X', '').replace('x', '')
# reversed_text = secret_message[::-1]
# print(reversed_text)
