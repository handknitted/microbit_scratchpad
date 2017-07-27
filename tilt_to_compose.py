# Add your Python code here. E.g.
from microbit import *
import speech


alphabet = "abcdefghijklmnopqrstuvwxyz. ^"


def make_word():
    word = ""
    letter = ''
    index = 0
    while letter != '^':
        while not both_pressed():           
            if button_a.is_pressed():
                index += 1
                if index > len(alphabet)-1:
                    index = 0
            elif button_b.is_pressed():
                index -= 1
                if index < 0:
                    index = len(alphabet) - 1
            display.show(alphabet[index])
            sleep(150)
        letter = alphabet[index]
        word += letter
    return word
   
def both_pressed():
    if button_a.was_pressed():
       if button_b.was_pressed():
           return True
    return False
    
def tilted_forward():
    y_reading = accelerometer.get_y()
    return y_reading > 70 

while True:
    word = make_word()
    display.scroll(word)
    sleep(10)
    
 
    
    
    
    