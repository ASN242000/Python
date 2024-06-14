# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 09:11:43 2024

@author: anusha.sn
"""

print("Hello"[0])
print("Hello"[-1])

num_char = len(input("What is your name?"))
type(num_char)

new_num_char = str(num_char)
print("Your name has "+new_num_char+" characters.")

type(100.5)
#%%
""" Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
"""
two_digit_number = input()
str1 =str(two_digit_number[0])
str2 =str(two_digit_number[1])
ans=int(str1)+int(str2)
print(ans)
#%%
"""Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

BMI Wikipedia Page

The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
    """

height = input()

weight = input()
w = int(weight)
h=int(height)
bmi=w/h**2
print(int(bmi))

#%%
x = 0x1B
y = 0x02
z = 0x58

command = bytearray([])
command.append(x)
command.append(y)
command.append(z)
for val in command:
    print(hex(val))
    
#%%
""" Tip and Bill Calculator """
bill= float(input("What is the total amount of the bill?"))
tip = int(input("What percentage of the tip are you willing to provide? 10%, 12% or 15%?"))  
tipping_amt = bill * (tip /100)
total_bill = bill + tipping_amt
no_people = int(input("How many people do you want to split the bill with?"))
split_amt = round( total_bill / no_people, 2)
print(f"Each person has to pay {split_amt}.") 









































