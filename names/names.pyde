from utils import Button, TextButton

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

TEXTBOX_HEIGHT = 40
MIN_TEXTBOX_WIDTH = 125
MAX_TEXTBOX_WIDTH = 230

textboxes = [[20, 20, "Player 1"], [20, 70, "Player 2"], [20, 120, "Player 3"], [20, 170, "Player 4"]]
selectedTextbox = -1
invalid = []

scene = "ENTER_NAMES"

def on_submit_button_click(button):
    global scene
    if len(invalid) == 0:
        button.setVisible(False)
        scene = "DISPLAY_NAMES"

buttons = []

def get_textbox_width(index):
    return max(MIN_TEXTBOX_WIDTH, textWidth(textboxes[index][2]) + 20)

def setup():
    frameRate(60)
    size(WINDOW_WIDTH, WINDOW_HEIGHT)
    this.surface.setTitle("Trade of Empires - Names")
    global submitButton
    
    submitButton = TextButton(20, 220, 125, 40, 225, on_submit_button_click).setTextSize(28).setText("Submit")
    buttons.append(submitButton)
    
def draw():
    global scene
    
    background(255)
    draw_buttons()
    
    if scene == "ENTER_NAMES":
        draw_input_fields()
    elif scene == "DISPLAY_NAMES":
        draw_scene_display_names()
        
def draw_scene_enter_names():
    draw_input_fields()
    
def draw_scene_display_names():
    text("Player 1 is " + textboxes[0][2] + ".", 20, 40)
    text("Player 2 is " + textboxes[1][2] + ".", 20, 100)
    text("Player 3 is " + textboxes[2][2] + ".", 20, 160)
    text("Player 4 is " + textboxes[3][2] + ".", 20, 220)
        
def draw_buttons():
    for button in buttons:
        button.render()
        
def draw_input_fields():
    global input
    anyHighlighted = False
    for i, textbox in enumerate(textboxes):
        w = get_textbox_width(i)
        if mouseX >= textbox[0] and mouseX <= textbox[0] + w and mouseY >= textbox[1] and mouseY <= textbox[1] + TEXTBOX_HEIGHT:
            fill(230)
            anyHighlighted = True
        else:
            fill(255)
        
        if selectedTextbox == i:
            fill(240)
            stroke(color(0, 0, 255))
            strokeWeight(2)
        elif i in invalid:
            stroke(color(255, 0, 0))
            strokeWeight(2)
        else:
            stroke(0)
            strokeWeight(1)
            
        rect(textbox[0], textbox[1], w, TEXTBOX_HEIGHT)
        fill(0)
        textSize(28)
        text(textbox[2], textbox[0] + 10, textbox[1] + 30)
        stroke(0)
        
        if selectedTextbox == i and frameCount // 25 % 2 == 0:
            linex = textbox[0] + textWidth(textbox[2]) + 13
            line(linex, textbox[1] + 6, linex, textbox[1] + TEXTBOX_HEIGHT - 6)
        
    if anyHighlighted:
        cursor(TEXT)
    else:
        cursor(ARROW)
    
def mousePressed(e):
    global selectedTextbox
    gotAny = False
    for i in range(len(textboxes)):
        textbox = textboxes[i]
        if mouseX >= textbox[0] and mouseX <= textbox[0] + get_textbox_width(i) and mouseY >= textbox[1] and mouseY <= textbox[1] + TEXTBOX_HEIGHT:
            selectedTextbox = i
            gotAny = True
            break
    if not gotAny:
        selectedTextbox = -1
        
    for button in buttons:
        button.checkClick(mouseX, mouseY)
    
def keyTyped(e):
    if selectedTextbox >= 0:
        input = textboxes[selectedTextbox][2]
        if e.key == BACKSPACE:
            input = input[:-1]
        elif textWidth(input) + 20 < MAX_TEXTBOX_WIDTH:
            input += e.key
        textboxes[selectedTextbox][2] = input
        if selectedTextbox not in invalid:
            if len(input) == 0:
                invalid.append(selectedTextbox)
        else:
            if len(input) > 0:
                invalid.remove(selectedTextbox)
    
    
