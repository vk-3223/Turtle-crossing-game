from turtle import Turtle

starting_postion = (0,-280)
move_distance = 10
finish_line = 280

class Player(Turtle):
    def __init__(self):
       super().__init__()
       self.shape("turtle")
       self.color("blue")
       self.penup()
       self.goto(starting_postion)
       self.setheading(90)
    def move_up(self):
        self.forward(move_distance)  
    def go_to_statrt(self):
        self.goto(starting_postion)     
    def is_at_finish_line(self):
        if self.ycor()>finish_line:
            return True
        else :
            False    

           

