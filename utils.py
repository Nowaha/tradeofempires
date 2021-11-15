class Button:
    def __init__(self, x, y, width, height, color, onClick):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.onClick = onClick
    
    def render(self):
        fill(self.color)
        rect(self.x, self.y, self.width, self.height)
        
    def checkClick(self, x, y):
        if x >= self.x and x <= self.x + self.width and y >= self.y and y <= self.y + self.height:
            self.onClick()