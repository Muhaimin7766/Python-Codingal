import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("white")

   
    square_turtle = turtle.Turtle()

   
    for _ in  range(4):
        square_turtle.forward(100)  
        square_turtle.right(90)     
    window.mainloop()
    
draw_square()
