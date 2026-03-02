print(type(123))
print(type(3.24))
print(type(True))
print(type("Hello"))

print(int("123") +int("456"))

#Converting to incompatable types is not possible #ValueError!
#You can lose data sometimes.

print("Number of letters in your name "+ str(len(input("What is your name?"))))