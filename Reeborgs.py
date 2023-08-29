def turn_right():
    turn_left()
    turn_left()
    turn_left()
def go():
    while at_goal() != True:
        if wall_in_front():
            if right_is_clear():
                turn_right()
                move()
            elif wall_in_front():
                turn_left()          
        elif right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        elif wall_on_right():
            move()
go()