def isWithin(x, y, w, h, x2, y2):
    return x2 >= x and x2 <= x + w and y2 >= y and y2 <= y + h

class Button(object):
    def __init__(self, x, y, width, height, backgroundColor, onClick):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.backgroundColor = backgroundColor
        self.hoverColor = backgroundColor * 0.9
        self.disabledColor = color(194, 194, 194)
        self.onClick = onClick
        self.visible = True
        self.enabled = True
    
    def setColor(self, backgroundColor):
        self.backgroundColor = backgroundColor
        return self
    
    def setHoverColor(self, hoverColor):
        self.hoverColor = hoverColor
        return self
    
    def setVisible(self, visible):
        self.visible = visible
        return self
    
    def setDisabledColor(self, disabledColor):
        self.disabledColor = disabledColor
        return self
    
    def render(self):
        strokeWeight(0.5)
        if self.visible:
            if self.enabled and isWithin(self.x, self.y, self.width, self.height, mouseX, mouseY):
                fill(self.hoverColor)
            else:
                if self.enabled:
                    fill(self.backgroundColor)
                else:
                    fill(self.disabledColor)
            strokeWeight(2)
            rect(self.x, self.y, self.width, self.height, 4)
            strokeWeight(1)
            return True
        strokeWeight(1)
        return False
        
    def checkClick(self, x, y):
        if self.visible and self.enabled and isWithin(self.x, self.y, self.width, self.height, x, y):
            self.onClick(self)
            
    def setEnabled(self, enabled):
        self.enabled = enabled
        return self
            
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
            textAlign(LEFT)
