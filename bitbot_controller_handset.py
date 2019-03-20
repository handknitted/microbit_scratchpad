# Add your Python code here. E.g.
from microbit import *
import radio

MOTOR_ON = 1
MOTOR_OFF = 0

MOTOR_ONE = 'one'
MOTOR_TWO = 'two'


_states = {
    'F': 'Forward',
    'B': 'Backward',
    'S': 'Steady'
}
_state = 'S'
radio.on()
radio.config(channel=47, power=5)

while True:
    state = '{:s},{},{:s},{}'.format(MOTOR_ONE, int(button_a.is_pressed()), MOTOR_TWO, int(button_b.is_pressed()))
    state_split = state.split(',')
    display.clear()
    if int(state_split[1]):
        display.set_pixel(0, 0, 9)
    if int(state_split[3]):
        display.set_pixel(4, 0, 9)
    radio.send(state)
    sleep(1)
