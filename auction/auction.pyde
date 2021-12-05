from utils import Button, TextButton

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 250

bid = 0
winningBid = -1

start = 0
time = 10
counting = False

def button_timer_start(button):
    global time, counting, start, bid
    button.setVisible(False)
    bumpButton.setVisible(True)
    bid = 0
    start = frameCount
    
    counting = True
    
def button_timer_bump(button):
    global start, bid
    bid += 50
    if get_time_left() <= 5:
        start = frameCount - (5*frameRate)

buttons = []

def setup():
    frameRate(60)
    size(WINDOW_WIDTH, WINDOW_HEIGHT)
    this.surface.setTitle("Trade of Empires - Auction")
    
    global bumpButton, timerButton, buttons
    timerButton = TextButton(WINDOW_WIDTH / 2 - 190/2, WINDOW_HEIGHT / 2 - 35/2, 190, 35, 255, button_timer_start).setText("Start auction").setTextSize(24)
    bumpButton = TextButton(WINDOW_WIDTH / 2 - 130/2, WINDOW_HEIGHT / 2 + 35, 130, 35, 255, button_timer_bump).setText("Bid +$50").setTextSize(24).setTextColor(255).setHoverColor(50).setColor(0).setVisible(False)
    
    buttons.append(timerButton)
    buttons.append(bumpButton)


def draw():
    background(195)
    draw_buttons()
    
    global time, counting, start, winningBid, bid
    if counting:
        timeLeft = get_time_left()
        draw_timer(timeLeft)
        if timeLeft < 0:
             counting = False
             winningBid = bid
             timerButton.setVisible(True)
             timerButton.setText("New auction")
             bumpButton.setVisible(False)
    else:
        if winningBid != -1:
            fill(0)
            textSize(24)
            text(("Winning bid: $" + str(winningBid)) if winningBid > 0 else "There were no bids.", WINDOW_WIDTH / 2, (WINDOW_HEIGHT / 2) - 40)
            
def draw_buttons():
    for button in buttons:
        button.render()

def get_time_left():
    return round(time - (frameCount - start) // frameRate)

def draw_timer(timeLeft):
    textAlign(CENTER, CENTER)
    fill(color(56, 233, 12))
    textSize(24)
    text("Bid: $" + str(bid), WINDOW_WIDTH / 2, (WINDOW_HEIGHT / 2) - 35)
    
    fill(0)
    textSize(32)
    text(((str(timeLeft).split(".")[0] + " second" + ('s' if timeLeft != 1 else '')) if timeLeft > 0 else "Last chance!"), WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

def mousePressed():
    for button in buttons:
        button.checkClick(mouseX, mouseY)
    
