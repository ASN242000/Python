import random

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_chars = ['@','#','$','%','&','*']

print("Welcome to the password generator!")
alpha = int(input("Enter a number of alphabets to generate password: "))
num = int(input("How many symbols would you like: \n"))
sym = int(input("How many symbols would you like: \n"))

password = ''
for i in range(1, alpha+1):
    char = random.choice(alphabets)
    password += char

for i in range(1, num+1):
    char1 = random.choice(numbers)
    password += char1

for i in range(1, sym+1):
    char2 = random.choice(special_chars)
    password += char2

print(password)

pass_list = []
for i in password:
    pass_list.append(i)

random.shuffle(pass_list)

hard_pass = ''
for i in pass_list:
    hard_pass += i
print(hard_pass)




