# Add your Python code here. E.g.
from microbit import *
import radio

FORWARD = 0
BACKWARD = 1

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


def get_tilt():
    reading = accelerometer.get_y()
    if reading > 750:
        return BACKWARD
    return FORWARD


while True:
    direction = get_tilt()
    state = '{:s},{},{:s},{},{}'.format(
        MOTOR_ONE, int(button_a.is_pressed()),
        MOTOR_TWO, int(button_b.is_pressed()),
        direction)
    state_split = state.split(',')
    display.clear()
    if int(state_split[1]):
        display.set_pixel(0, 4 * direction, 9)
    if int(state_split[3]):
        display.set_pixel(4, 4 * direction, 9)
    radio.send(state)
    sleep(1)
