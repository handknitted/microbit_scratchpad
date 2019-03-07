# Add your Python code here. E.g.
from microbit import *
import radio

_states = {
    'F': 'Forward',
    'B': 'Backward',
    'S': 'Steady'
}
_state = 'S'
radio.on()
radio.config(channel=47, power=5)

while True:
    previous_state = _state
    x_reading = accelerometer.get_x()
    y_reading = accelerometer.get_y()

    if y_reading > 200:
        state = _states['F']
    elif y_reading < -200:
         state = _states['B']
    else:
        state = _states['S']
    display.show(state)
    radio.send(state)
    sleep(10)
