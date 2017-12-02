from microbit import *

button_long_a_pressed = "button_long_a"
button_long_b_pressed = "button_long_b"
button_a_pressed = "button_a"
button_b_pressed = "button_b"
button_together_pressed = "button_together"
button_long_together_pressed = "button_long_together"

def is_long(conditions):
    if len(conditions) > 0:
        time = running_time()
        print('Time = %s' % time)
        while running_time() - time < 10000:
            print('Time = %s, Conditions = %s' %
                  (time, [condition() for condition in conditions]))
            if not all(cond() for cond in conditions):
                return False
            return True

class ButtonHandler(object):
    
    button_reset = True
    
    def button_press(self, presses):
            if (button_a.is_pressed()
                    and button_b.is_pressed()):
                if self.button_reset:
                    self.button_reset = False
                    if is_long([button_a.is_pressed, button_b.is_pressed]):
                        presses.append(button_long_together_pressed)
                    else: 
                        presses.append(button_together_pressed)
            elif button_a.is_pressed():
                if self.button_reset:
                    self.button_reset = False
                    if is_long([button_a.is_pressed]):
                        presses.append(button_long_a_pressed)
                    else:
                        presses.append(button_a_pressed)
            elif button_b.is_pressed():
                if self.button_reset:
                    self.button_reset = False
                    if is_long([button_b.is_pressed]):
                        presses.append(button_long_b_pressed)
                    else:
                        presses.append(button_b_pressed)
            else:
                self.button_reset = True


print(running_time())
sleep(1000)
print(running_time())
count = 10
inputs = []
handle_buttons = ButtonHandler()
while len(inputs) < count:
    handle_buttons.button_press(inputs)
    
print(inputs)
    

        