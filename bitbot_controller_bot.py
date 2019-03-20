from microbit import *
import radio


radio.on()
radio.config(channel=47, power=5)

MOTOR_ON = 1
MOTOR_OFF = 0

MOTOR_ONE = 'one'
MOTOR_TWO = 'two'

MOTOR_ONE_WRITE = pin16.write_digital
MOTOR_TWO_WRITE = pin12.write_digital

while True:
    transmitted_state = radio.receive()
    if transmitted_state is not None:
        # noinspection PyBroadException
        try:
            state = transmitted_state.split(',')

            motor_one_state = int(state[1])
            # MOTOR_ONE_WRITE(motor_one_state)
            motor_two_state = int(state[3])
            # MOTOR_TWO_WRITE(motor_two_state)
            if int(state[1]):
                MOTOR_ONE_WRITE(MOTOR_ON)
            else:
                MOTOR_ONE_WRITE(MOTOR_OFF)
            if int(state[3]):
                MOTOR_TWO_WRITE(MOTOR_ON)
            else:
                MOTOR_TWO_WRITE(MOTOR_OFF)

        except Exception:
            MOTOR_TWO_WRITE(MOTOR_OFF)
            MOTOR_ONE_WRITE(MOTOR_OFF)
