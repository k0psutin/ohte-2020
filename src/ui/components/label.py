class Label():
    def __init__(self,
                 text,
                 size_x,
                 size_y,
                 offset_x,
                 offset_y,
                 gamestate,
                 font):

        self.width = gamestate.width
        self.height = gamestate.height
        self.size = (size_x, size_y)
        self.x_pos = (self.width/2-(size_x/2))+(self.width*offset_x)
        self.y_pos = (self.height/2-(size_y/2))+(self.height*offset_y)
        self.color = (0, 0, 0)
        self.font = font
        self.text = self.font.render(text, True, self.color)
        self.display = gamestate.display

    def update(self, event):
        self.event = event
        self.display.blit(self.text, (self.x_pos, self.y_pos))

    def change_text(self, text):
        self.text = self.font.render(text, True, self.color)
