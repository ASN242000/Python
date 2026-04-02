#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_around()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    while wall_in_front():
        turn_left()
        move()
        turn_right()
    move()
    turn_right()
    move()
    turn_right()
    while wall_in_front():
        turn_left()
        if wall_in_front():
            turn_left()
            return
        elif not wall_in_front():
            move()
            turn_right()


while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()
