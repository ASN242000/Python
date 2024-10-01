import random
import Importing

#Random integer generator

random_integer= random.randint(1,10) #Chooses a random no between 1 to 10 including 1 and 10.
print(random_integer)
print(Importing.my_fav_no)

#random floating point nos
#random.random() - generated 0.0 <= X < 1.0

ran_no = random.random()
print(ran_no)

#random floating point generator in range a <= N <= b

random_float = random.uniform(1,10)
print(random_float)

#Print head or tail based on the random number generated.
random_integer= random.randint(0,1)
if(random_integer == 0):
    print("Head!")
else:
    print("Tails!")