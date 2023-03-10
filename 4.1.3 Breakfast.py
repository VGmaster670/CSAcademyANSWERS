# table
Rect(0, 0, 400, 400, fill=gradient('peru', 'sienna', start='left-top'))

# plate
Circle(200, 220, 150, fill='white')

# pancake
Circle(170, 220, 100, fill='wheat', border='burlyWood')
Rect(140, 210, 30, 30, fill='yellow')

# fruit
Circle(230, 320, 70, fill='orange')
Circle(230, 320, 62, fill='lightCoral', border='antiqueWhite', borderWidth=5)
Star(230, 320, 55, 12, fill='antiqueWhite', roundness=0)

def drawBreakfast(isThirsty, isTired, isVegan, isVegetarian):
    # Draw drinks depending on if you are thirsty and/or if you are tired.
    ### Place Your Code Here ###
    if (isThirsty==True):
        Circle(350,70,50,border="white",borderWidth=4,fill=gradient("gold","orange"))
    if (isThirsty==True and isTired==True):
        Oval(85,65,50,20,fill="white")
        Circle(20,70,55,border="white",borderWidth=10,fill=rgb(112,73,60))
    # Draw extra food based on vegan/vegetarian preference.
    ### (HINT: Code for eggs and sausages are given. Place them appropriately.)
    ### Fix Your Code Here ###
    if (isVegan==False):
        # eggs
        Oval(265, 160, 110, 100, fill='white', border='lightGrey', rotateAngle=20)
        Circle(250, 150, 20, fill='gold')
        Oval(285, 220, 110, 90, fill='white', border='lightGrey', rotateAngle=20)
        Circle(300, 220, 20, fill='gold')
        if (isVegetarian==False):
            # sausages
            Oval(140, 135, 100, 40, fill='maroon', rotateAngle=350)
            Oval(190, 130, 100, 40, fill='brown', rotateAngle=320)
