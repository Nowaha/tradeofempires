from utils import Button

# Can be named anything!
def on_button_click():
    print("Clicked!")

# Usage: Button(positionX, positionY, width, height, color, function)
buttons = [Button(25, 25, 100, 75, 0, on_button_click)]

def draw():
    for button in buttons:
        button.render()

def mousePressed():
    for button in buttons:
        button.checkClick(mouseX, mouseY)