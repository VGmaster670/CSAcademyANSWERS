# background
app.background = gradient('maroon', 'black')

Label('Cookie Clicker!', 200, 20, fill='white', size=20, bold=True)

# cookie
Circle(200, 200, 105, fill=gradient('burlyWood', 'peru'))

# chocolate chips
Circle(210, 200, 10, fill='saddleBrown')
Circle(160, 130, 10, fill='saddleBrown')
Circle(280, 220, 10, fill='saddleBrown')
Circle(240, 150, 10, fill='saddleBrown')
Circle(140, 255, 10, fill='saddleBrown')
Circle(210, 245, 10, fill='saddleBrown')
Circle(130, 200, 10, fill='saddleBrown')

# Define the variable to count the number of times we clicked.
### Place Your Code Here ###
number = Label(0,200,200,fill="White", size=64)
def onMousePress(mouseX, mouseY):
    # Increase the number of times we clicked on the cookie.
    ### Place Your Code Here ###
    number.value+=1
