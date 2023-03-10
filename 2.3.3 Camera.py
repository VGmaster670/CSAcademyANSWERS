background = Rect(0, 0, 400, 400)

# camera
Rect(90, 135, 40, 15, fill='steelBlue')
Rect(80, 150, 240, 30, fill='white')
Circle(80, 320, 30, fill='white')
Circle(320, 320, 30, fill='white')
Circle(80, 180, 30, fill='white')
Circle(320, 180, 30, fill='white')
Rect(50, 180, 300, 140, fill='skyBlue')
Rect(80, 320, 240, 30, fill='white')
Circle(245, 250, 80, fill='white', border='steelBlue', borderWidth=10)
Circle(245, 250, 50)

# flash
flash = Star(245, 250, 200, 12, fill=gradient('white', 'yellow', 'gold'),
             roundness=30, visible=False)

def onMousePress(mouseX, mouseY):
    # Turn the flash on.
    ### Place Your Code Here ###
    flash.visible=True
    background.fill=gradient("steelBlue","black")

def onMouseRelease(mouseX, mouseY):
    # Turn the flash off.
    ### Place Your Code Here ###
    flash.visible=False
    background.fill="Black"
