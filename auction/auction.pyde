import math
from utils import Button, TextButton

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

STARTING_BID = 50
BID_INCREMENT = 50

PLAYER_1_COLUMN_X = WINDOW_WIDTH / 2 - 200
PLAYER_2_COLUMN_X = WINDOW_WIDTH / 2 - 67.5
PLAYER_3_COLUMN_X = WINDOW_WIDTH / 2 + 67.5
PLAYER_4_COLUMN_X = WINDOW_WIDTH / 2 + 200

PLAYER_BASE_Y = (WINDOW_HEIGHT / 2) + 20

bid = 0
bidder = 0

start = 0
time = 10
counting = False

player1Balance = 500
player2Balance = 550
player3Balance = 600
player4Balance = 100

def start_timer_button_click(button):
    global time, counting, start, bid, bidder
    button.setVisible(False)
    #bumpButton.setVisible(True)
    player1BidButton.setVisible(True).setText("L." + str(STARTING_BID))
    player2BidButton.setVisible(True).setText("L." + str(STARTING_BID))
    player3BidButton.setVisible(True).setText("L." + str(STARTING_BID))
    player4BidButton.setVisible(True).setText("L." + str(STARTING_BID))
    
    bid = 0
    bidder = 0
    start = frameCount
    
    counting = True
    
def bump_timer():
    global start
    if get_time_left() <= 5:
        start = frameCount - (5*frameRate)

buttons = []

def setup():
    frameRate(60)
    size(WINDOW_WIDTH, WINDOW_HEIGHT)
    this.surface.setTitle("Trade of Empires - Auction")
    
    global buttons, bumpButton, timerButton, player1BidButton, player2BidButton, player3BidButton, player4BidButton
    timerButton = TextButton(WINDOW_WIDTH / 2 - 190/2, WINDOW_HEIGHT / 2 - 35/2, 190, 35, 255, start_timer_button_click).setText("Start auction").setTextSize(24)
    
    buttons.append(timerButton)
    
    player1BidButton = TextButton(PLAYER_1_COLUMN_X - 75/2, PLAYER_BASE_Y + 50, 75, 35, 255, onclick_player_1_bid).setTextSize(20).setText("-").setVisible(False)
    player2BidButton = TextButton(PLAYER_2_COLUMN_X - 75/2, PLAYER_BASE_Y + 50, 75, 35, 255, onclick_player_2_bid).setTextSize(20).setText("-").setVisible(False)
    player3BidButton = TextButton(PLAYER_3_COLUMN_X - 75/2, PLAYER_BASE_Y + 50, 75, 35, 255, onclick_player_3_bid).setTextSize(20).setText("-").setVisible(False)
    player4BidButton = TextButton(PLAYER_4_COLUMN_X - 75/2, PLAYER_BASE_Y + 50, 75, 35, 255, onclick_player_4_bid).setTextSize(20).setText("-").setVisible(False)
    
    buttons.append(player1BidButton)
    buttons.append(player2BidButton)
    buttons.append(player3BidButton)
    buttons.append(player4BidButton)

def draw():
    background(195)
    draw_buttons()
    
    global time, counting, start, bid, player1Balance, player2Balance, player3Balance, player4Balance
    if counting:
        timeLeft = get_time_left()
        draw_timer(timeLeft)
        draw_player_data()
        if timeLeft < 0:
            counting = False
            
            timerButton.setVisible(True)
            timerButton.setText("New auction")
            
            player1BidButton.setVisible(False)
            player2BidButton.setVisible(False)
            player3BidButton.setVisible(False)
            player4BidButton.setVisible(False)
            
            if bid > 0:
                if bidder == 1:
                    player1Balance -= bid
                elif bidder == 2:
                    player2Balance -= bid
                elif bidder == 3:
                    player3Balance -= bid
                elif bidder == 4:
                    player4Balance -= bid
    else:
        if start != 0:
            fill(0)
            textSize(24)
            text(("Player " + str(bidder) + " won with a bid of L." + str(bid)) if bid > 0 else "There were no bids.", WINDOW_WIDTH / 2, (WINDOW_HEIGHT / 2) - 40)

def onclick_player_1_bid(btn):
    attempt_player_bid(1)
def onclick_player_2_bid(btn):
    attempt_player_bid(2)
def onclick_player_3_bid(btn):
    attempt_player_bid(3)
def onclick_player_4_bid(btn):
    attempt_player_bid(4)

def attempt_player_bid(player):
    global bid, bidder
    bid += BID_INCREMENT
    bidder = player
    bump_timer()

def draw_buttons():
    for button in buttons:
        button.render()

def get_time_left():
    return math.floor(time - (frameCount - start) // frameRate)

def draw_timer(timeLeft):
    textAlign(CENTER, CENTER)
    fill(color(56, 233, 12))
    textSize(20)
    if (bid > 0):
        text("Player " + str(bidder) + " bid L." + str(bid), WINDOW_WIDTH / 2, (WINDOW_HEIGHT / 2) - 65)
    else:
        text("No bids yet.", WINDOW_WIDTH / 2, (WINDOW_HEIGHT / 2) - 65)
    
    fill(0)
    textSize(32)
    text(((str(timeLeft).split(".")[0] + " second" + ('s' if timeLeft != 1 else '')) if timeLeft > 0 else "Last chance!"), WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 30)

def draw_player_data():
    fill(0)
    textSize(24)
    text("Player 1", PLAYER_1_COLUMN_X, PLAYER_BASE_Y)
    text("Player 2", PLAYER_2_COLUMN_X, PLAYER_BASE_Y)
    text("Player 3", PLAYER_3_COLUMN_X, PLAYER_BASE_Y)
    text("Player 4", PLAYER_4_COLUMN_X, PLAYER_BASE_Y)
    
    textSize(20)
    text("L." + str(player1Balance), PLAYER_1_COLUMN_X, PLAYER_BASE_Y + 30)
    text("L." + str(player2Balance), PLAYER_2_COLUMN_X, PLAYER_BASE_Y + 30)
    text("L." + str(player3Balance), PLAYER_3_COLUMN_X, PLAYER_BASE_Y + 30)
    text("L." + str(player4Balance), PLAYER_4_COLUMN_X, PLAYER_BASE_Y + 30)
    
    nextBid = bid + BID_INCREMENT
    
    player1BidButton.setText("L." + str(nextBid) if player1Balance >= nextBid else "-").setEnabled(player1Balance >= nextBid)
    player2BidButton.setText("L." + str(nextBid) if player2Balance >= nextBid else "-").setEnabled(player2Balance >= nextBid)
    player3BidButton.setText("L." + str(nextBid) if player3Balance >= nextBid else "-").setEnabled(player3Balance >= nextBid)
    player4BidButton.setText("L." + str(nextBid) if player4Balance >= nextBid else "-").setEnabled(player4Balance >= nextBid)
    
    if bidder != 0:
        noFill()
        stroke(color(56, 233, 12))
        strokeWeight(2)
        rectMode(CENTER)
        highlightedColumnX = PLAYER_1_COLUMN_X if bidder == 1 else (PLAYER_2_COLUMN_X if bidder == 2 else (PLAYER_3_COLUMN_X if bidder == 3 else PLAYER_4_COLUMN_X))
        rect(highlightedColumnX, PLAYER_BASE_Y + 40, 100, 110)
        rectMode(CORNER)
        strokeWeight(1)
        stroke(0)

def mousePressed():
    for button in buttons:
        button.checkClick(mouseX, mouseY)
    
