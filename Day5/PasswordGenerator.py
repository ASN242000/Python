import random
from http.cookiejar import join_header_words
from tokenize import String

alphabet = [  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z' ]

num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
chars = ['!', '@', '#', '$', '%', '&', '*', '(', ')']

alpha = int(input("How many letters do you need in your password?"))
numbers = int(input("How many numbers do you need in your password?"))
characters = int(input("How many special characters do you need in your password?"))

A = ''
for i in range (0, alpha):
    A += random.choice(alphabet)

N=''
for i in range (0, numbers):
    N += random.choice(num)

S=''
for i in range (0, characters):
    S += random.choice(chars)

Password = A+N+S
chList = list(Password)
random.shuffle(chList)
print(''.join(chList))
