# Reeborg is a website which creates random mazes which has some built-in-functions and we have to use 
# any programming language to solve the maze.


# This piece of code solves most of the random mazes generated in reeborg, but it might not be applicable for advanced mazes.
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()