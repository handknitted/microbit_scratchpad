from microbit import *

button_long_a_pressed = "button_long_a"
button_long_b_pressed = "button_long_b"
button_a_pressed = "button_a"
button_b_pressed = "button_b"
button_together_pressed = "button_together"
button_long_together_pressed = "button_long_together"


class ButtonHandler(object):

    both_button_push_grace_ms = 50
    long_push_ms = 400
    button_reset = True
        
    def get_button_press(self):
        if (button_a.is_pressed() or button_b.is_pressed()):
            if self.button_reset:
                self.button_reset = False
                print("Got a button push at %s" % running_time())
                # delay to catch up if both are being pushed
                sleep(self.both_button_push_grace_ms)
                return self.identify_button_press()
        else:
            self.button_reset = True
            return None
    
    def identify_button_press(self):
        press = None
        if (button_a.is_pressed()
                and button_b.is_pressed()):
            if self.is_long([button_a.is_pressed, button_b.is_pressed]):
                press = button_long_together_pressed
            else: 
                press =  button_together_pressed
        elif button_a.is_pressed():
            if self.is_long([button_a.is_pressed]):
                press = button_long_a_pressed
            else:
                press = button_a_pressed
        elif button_b.is_pressed():
            if self.is_long([button_b.is_pressed]):
                press = button_long_b_pressed
            else:
                press = button_b_pressed
        return press
        
    def is_long(self, conditions):
        if len(conditions) > 0:
            time = running_time()
            print('Time = %s' % time)
            while running_time() - time < self.long_push_ms:
                print('Time = %s, Conditions = %s' %
                      (running_time(), 
                       [condition() for condition in conditions]))
                if not all(cond() for cond in conditions):
                    print("short")
                    return False
            print("long")
            return True


if __name__ == "__main__":
    print(running_time())
    sleep(1000)
    print(running_time())
    count = 10
    handle_buttons = ButtonHandler()
    while len(handle_buttons.get_presses()) < count:
        handle_buttons.button_press()
        
    print(handle_buttons.get_presses())
    

        