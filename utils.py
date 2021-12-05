def isWithin(x, y, w, h, x2, y2):
    return x2 >= x and x2 <= x + w and y2 >= y and y2 <= y + h

class Button(object):
    def __init__(self, x, y, width, height, color, onClick):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hoverColor = color * 0.9
        self.onClick = onClick
        self.visible = True
    
    def setColor(self, color):
        self.color = color
        return self
    
    def setHoverColor(self, hoverColor):
        self.hoverColor = hoverColor
        return self
    
    def setVisible(self, visible):
        self.visible = visible
        return self
    
    def render(self):
        if self.visible:
            if isWithin(self.x, self.y, self.width, self.height, mouseX, mouseY):
                fill(self.hoverColor)
            else:
                fill(self.color)
            rect(self.x, self.y, self.width, self.height)
            return True
        return False
        
    def checkClick(self, x, y):
        if self.visible and isWithin(self.x, self.y, self.width, self.height, x, y):
            self.onClick(self)
            
class TextButton(Button, object):
    def __init__(self, *args, **kwargs):
        super(TextButton, self).__init__(*args, **kwargs)
        self.text = "Button"
        self.textSize = 32
        self.textColor = color(0, 0, 0)
        self.paddingTop = 0
        
    def setText(self, text):
        self.text = text
        return self

    def setTextSize(self, textSize):
        self.textSize = textSize
        return self
        
    def setTextColor(self, textColor):
        self.textColor = textColor
        return self
    
    def render(self):
        if(super(TextButton, self).render()):
            fill(self.textColor)
            textAlign(CENTER, CENTER)
            textSize(self.textSize)
            text(self.text, self.x + (self.width / 2), self.y + (self.height / 2) - 3)
