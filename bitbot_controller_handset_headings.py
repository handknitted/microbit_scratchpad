# Add your Python code here. E.g.
from microbit import *
import radio

FORWARD_TRANS = 2
STOP_TRANS = 0
BACKWARD_TRANS = 1
MAINTAIN_TRANS = 3

MOTOR_ON = 1
MOTOR_OFF = 0

FADE_RIGHT = 'one'
FADE_LEFT = 'two'


_states = {
    'F': 'Forward',
    'B': 'Backward',
    'S': 'Steady'
}
_state = 'S'
radio.on()
radio.config(channel=47, power=5)

STOP = 'face up'
FORWARD = 'down'
BACKWARD = 'up'


def get_tilt():
    reading = accelerometer.current_gesture()
    if STOP == reading:
        return STOP_TRANS
    if BACKWARD == reading:
        return BACKWARD_TRANS
    if FORWARD == reading:
        return FORWARD_TRANS
    return MAINTAIN_TRANS


while True:
    direction = get_tilt()
    state = '{:s},{},{:s},{},{}'.format(
        FADE_RIGHT, int(button_a.is_pressed()),
        FADE_LEFT, int(button_b.is_pressed()),
        direction)
    state_split = state.split(',')
    display.clear()
    if int(state_split[1]):
        display.set_pixel(0, 4, 9)
    if int(state_split[3]):
        display.set_pixel(4, 4, 9)
    radio.send(state)
    sleep(1)