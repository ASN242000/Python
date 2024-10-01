import random

friends = ['Alice', 'Bob','Charlie','David','Emanual']

#1 way
name = random.choice(friends)
print(name)

#2nd way
random_index = random.randint(0,4)
print(friends[random_index])