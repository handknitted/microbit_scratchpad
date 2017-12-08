# Add your Python code here. E.g.
from microbit import *
from buttons import (ButtonHandler, button_a_pressed, button_long_a_pressed,
                     button_b_pressed, button_long_b_pressed,
                     button_together_pressed)


alphabet = "abcdefghijklmnopqrstuvwxyz. ^"

def make_word(buttonActionHandler=ButtonHandler()):
    word = ""
    letter = ''
    index = 0
    word_complete = False
    while word_complete is not True:
        press = buttonActionHandler.get_button_press()
        if press == button_a_pressed:
            index -= 1
            if index < 0:
                index = len(alphabet)-1
        elif press == button_long_a_pressed:
            index -= 5
            if index < 0:
                index = len(alphabet) + index
        elif press == button_b_pressed:
            index += 1
            if index > len(alphabet) - 1:
                index = 0
        elif press == button_long_b_pressed:
            index += 5
            if index > len(alphabet) - 1:
                index = index - (len(alphabet))
        elif press == button_together_pressed:
            if letter == '^':
                word_complete = True
            else:
                word += letter
                display.clear()
                sleep(500)  
        display.show(alphabet[index])
        letter = alphabet[index]
    return word   

while True:    
    buttonActionHandler = ButtonHandler()
    word = make_word(buttonActionHandler=buttonActionHandler)
    display.scroll(word, wait=False, loop=True)
    stop_press = None
    while stop_press is None:
        stop_press = buttonActionHandler.get_button_press()

