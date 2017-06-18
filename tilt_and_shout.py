# Add your Python code here. E.g.
from microbit import *
import speech

x_values = {'minus': 'L', 'plus': 'R'}
y_values = {'minus': 'F', 'plus': 'B'}
states = {
    'F': 'Forward',
    'B': 'Backward',
    'L': 'Left',
    'R': 'Right',
    'S': 'Steady'
}
state = 'S'
while True:
    previous_state = state
    x_reading = accelerometer.get_x()
    y_reading = accelerometer.get_y()
    if x_reading * x_reading > y_reading * y_reading:
        values = x_values
        reading = x_reading
    else:
        values = y_values
        reading = y_reading
    if reading > 20:
        state = values['plus']
    elif reading < -20:
         state = values['minus']
    else:
        state = "S"
    display.show(state)
    if previous_state != state:
        speech.say(states[state])
