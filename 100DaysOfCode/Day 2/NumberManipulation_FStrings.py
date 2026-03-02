weight = int(input("What is your weight?"))
height = int(input("Whta is your height?"))
bmi = weight/(height*height)
print("Your bmi = " + str(bmi))

print(round(bmi,2))

print(f"Your bmi is {round(bmi,2)}")