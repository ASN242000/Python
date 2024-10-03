for num in range(1, 101):
    if (num % 3 == 0):
        if (num % 5 == 0):
            print('Fizzbuzz')
        else:
            print('Fizz')
    elif (num % 5 == 0):
        print('Buzz')
    else:
        print(num)

#Another logic
for i in range (1,101):
    if (i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    elif (i % 3 == 0 and i % 5 != 0):
        print("Fizz")
    elif (i % 3 != 0 and i % 5 == 0):
        print("Buzz")
    else:
        print(i)