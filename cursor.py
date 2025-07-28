import keyboard as key

class Cursor:
    def __init__(self, cur_facelet, cur_color):
        self.facelet = cur_facelet
        self.color = cur_color
        self.prev_pressed = False
    
    def move(self):
        pressed = False
        if key.is_pressed('left'):
            if self.facelet > 1 and not self.prev_pressed:
                self.facelet -= 1
            pressed = True
        elif key.is_pressed('right'):
            if self.facelet < 54 and not self.prev_pressed:
                self.facelet += 1
            pressed = True
        elif key.is_pressed('up'):
            if self.facelet >= 4 and not self.prev_pressed:
                self.facelet -= 3
            pressed = True
        elif key.is_pressed('down'):
            if self.facelet <= 51 and not self.prev_pressed:
                self.facelet += 3
            pressed = True
        self.prev_pressed = pressed

        if pressed:
            return

        if key.is_pressed('0'):
            self.color = 0
        elif key.is_pressed('1'):
            self.color = 1
        elif key.is_pressed('2'):
            self.color = 2
        elif key.is_pressed('3'):
            self.color = 3
        elif key.is_pressed('4'):
            self.color = 4
        elif key.is_pressed('5'):
            self.color = 5