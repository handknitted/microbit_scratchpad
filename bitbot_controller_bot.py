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
    transmitted_state = radio.receive()
    if transmitted_state is not None:
        display.show(transmitted_state)
