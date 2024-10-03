student_scores = [85, 92, 76, 54, 88,
    67, 90, 73, 82, 95,
    60, 45, 78, 81, 69,
    92, 99, 87, 66, 75,
    59, 48, 93, 67, 84,
    76, 62, 89, 71, 50,
    99, 64, 88, 57, 72,
    81, 95, 38, 79, 53,
    65, 94, 77, 56]

sum =0
for score in student_scores:
    sum += score

print(sum)

HighestScore = 0
for score in student_scores:
    if score > HighestScore:
        HighestScore = score

print(HighestScore)