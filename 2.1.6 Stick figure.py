# background
Line(200, 0, 200, 400, fill='steelBlue', lineWidth=400, opacity=40,
     dashes=(2, 23))
Line(50, 0, 50, 400, fill='crimson', opacity=60)

def stickFigure(x, y, size):
    # The parameters (x, y) is where where the head and body of the stick figure
    # meet.

    # head
    Circle(x, y - size, size)

    # Draw the stick figure's body, and arms. We have drawn the head and legs
    # for you.
    ### Place Your Code Here ###
    Line(x,y,x,y+2*size)
    Line(x,y+size,x-size,y)
    Line(x,y+size,x+size,y)
    # legs
    Line(x, y + 2 * size, x - size, y + 3 * size)
    Line(x, y + 2 * size, x + size, y + 3 * size)
