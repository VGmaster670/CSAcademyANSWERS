background = Rect(0, 0, 400, 400)
Oval(200, 270, 250, 80, fill='saddleBrown', opacity=30)

# pumpkin
Line(200, 120, 215, 90, fill='green', lineWidth=10)
Oval(120, 200, 100, 150, fill='orange', border='darkOrange', borderWidth=4)
Oval(280, 200, 100, 150, fill='orange', border='darkOrange', borderWidth=4)
Oval(150, 200, 120, 160, fill='orange', border='darkOrange', borderWidth=4)
Oval(250, 200, 120, 160, fill='orange', border='darkOrange', borderWidth=4)
Oval(200, 200, 130, 170, fill='orange', border='darkOrange', borderWidth=4)

leftEye = RegularPolygon(145, 170, 30, 3, fill='yellow', border='darkOrange')
rightEye = RegularPolygon(255, 170, 30, 3, fill='yellow', border='darkOrange')
mouth = Oval(200, 230, 120, 40, fill='yellow', border='darkOrange')
Oval(200, 220, 120, 30, fill='orange')

def onMouseDrag(mouseX, mouseY):
    # If the mouse is on the left side of the canvas, change the fills
    # to make a day scene. Otherwise change the fills for a night scene.
    ### Place Your Code Here ###
    if (mouseX<200):
        background.fill="lightBlue"
        leftEye.fill="chocolate"
        rightEye.fill="chocolate"
        mouth.fill="chocolate"
    else:
        background.fill="black"
        leftEye.fill="yellow"
        rightEye.fill="yellow"
        mouth.fill="yellow"
