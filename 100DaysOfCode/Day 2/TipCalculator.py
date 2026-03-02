print("Welcome to the tip calculator")
bill = int(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? %"))
num = int(input("How many people to split the bill? "))

tip = bill * (tip/100)
each = (bill + tip) / num
print(f"Each person should pay: ${round(each,2)}")
