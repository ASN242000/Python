import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

sissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''


image = [rock,paper,sissors]
player_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors "))
computer_choice = random.randint(0,2)
print(image[player_choice])
print(image[computer_choice])

if player_choice == 0 and computer_choice == 2:
    print("You Win")
elif player_choice == 1 and computer_choice == 0:
    print("You Win")
elif player_choice == 1 and computer_choice == 2:
    print("You Win")
elif player_choice == 2 and computer_choice == 1:
    print("You Win")
elif player_choice == computer_choice:
    print("Draw")
elif player_choice <0 or player_choice >2:
    print("You entered an invalid input")
else:
    print("You lose!")


