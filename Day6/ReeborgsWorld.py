# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
# Above is the link for reborgs world

#to turn_right()
#Paste the below code in the website. Website: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
def turn_right():
    for i in range(0, 3):
        turn_left()


turn_left()
move()
move()
turn_right()
move()

#To move in square
def turn_right():
    for i in range(0, 3):
        turn_left()


turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()
