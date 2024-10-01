import random
rock = ''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user = int(input("Choose 0 for Rock, 1 for Paper and 2 for Scissors"))
if(user >= 3 or user <0):
    print("You choose an invalid number")
elif(user == 0):
    print(rock)
elif(user == 1):
    print(paper)
else:
    print(scissors)

computer = random.randint(0,2)
if(computer == 0):
    print(rock)
elif(computer == 1):
    print(paper)
else:
    print(scissors)

if(user == computer):
    print("Draw!")
elif((user == 1 and computer == 0) or (user == 2 and computer == 1) or (user == 0 and computer == 2)):
    print("You Won!!")
else:
    print("You lost!")