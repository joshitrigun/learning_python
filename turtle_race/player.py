from turtle import Turtle

STARTING_POSITIONS = (0, -350)
MOVE_DISTANCE = 10
FINISH_LINE = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_to_start(self):
        self.goto(STARTING_POSITIONS)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish(self):
        if self.ycor() > FINISH_LINE:
            return True
# player = Turtle()
# player.shape("turtle")
# player.penup()
# player.goto(0, -350)
# player.setheading(90)












