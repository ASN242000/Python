scores = [34, 43, 23, 66, 24, 54, 21, 67, 65]
sum = 0
for score in scores:
    sum = sum + score
print(sum)

highest = 0
for score in scores:
    if score > highest:
        highest = score
print("Highest score is", highest)