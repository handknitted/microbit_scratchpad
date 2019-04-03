from microbit import *
import radio

compass.calibrate()

radio.on()
radio.config(channel=47, power=5)

MOTOR_ON = 720
MOTOR_OFF = 0

FADE_RIGHT = 'one'
FADE_LEFT = 'two'

FORWARD_TRANS = 2
STOP_TRANS = 0
BACKWARD_TRANS = 1
MAINTAIN_TRANS = 3

MOTOR_ONE_POS_WRITE = pin16.write_analog
MOTOR_ONE_NEG_WRITE = pin0.write_analog
MOTOR_TWO_POS_WRITE = pin8.write_analog
MOTOR_TWO_NEG_WRITE = pin12.write_analog


def get_turn_direction_and_angle(desired_heading):
    angle_of_turn = compass.heading() - desired_heading
    absolute_turn = angle_of_turn - 180
    degrees_turn = 180 - (absolute_turn % 360)
    return degrees_turn


def spin_left(factor=700):
    MOTOR_ONE_POS_WRITE(factor)
    MOTOR_ONE_NEG_WRITE(MOTOR_OFF)
    MOTOR_TWO_POS_WRITE(MOTOR_OFF)
    MOTOR_TWO_NEG_WRITE(factor)


def spin_right(factor=700):
    MOTOR_ONE_POS_WRITE(factor)
    MOTOR_ONE_NEG_WRITE(MOTOR_OFF)
    MOTOR_TWO_POS_WRITE(MOTOR_OFF)
    MOTOR_TWO_NEG_WRITE(factor)


def motors_off():
    MOTOR_ONE_POS_WRITE(MOTOR_OFF)
    MOTOR_ONE_NEG_WRITE(MOTOR_OFF)
    MOTOR_TWO_POS_WRITE(MOTOR_OFF)
    MOTOR_TWO_NEG_WRITE(MOTOR_OFF)


def turn_to_heading(required_heading):
    diff_degrees = get_turn_direction_and_angle(required_heading)
    motor_factor = int(abs(diff_degrees) * (1023/180))
    if motor_factor < 100:
        motor_factor = 100

    if diff_degrees == 0:
        motors_off()
        return True
    elif diff_degrees < 0:
        spin_right(motor_factor)
    else:
        spin_left(motor_factor)
    return False


def trim(heading):
    """get a trim for each motor 1 - 100"""
    angle = get_turn_direction_and_angle(heading)
    trim_value = int(angle / 1.8)
    return trim_value/2, -trim_value/2


def set_motor(motor_pos, motor_neg, speed=0):
    if speed < 0:
        motor_pos(speed)
        motor_neg(0)
    elif speed > 0:
        motor_pos(0)
        motor_neg(speed)


current_heading = compass.heading()

while True:
    transmitted_state = radio.receive()
    if transmitted_state is not None:
        # noinspection PyBroadException
        try:
            state = transmitted_state.split(',')

            fade_right = int(state[1])
            fade_left = int(state[3])
            direction_modifier = int(state[4])
            if fade_right ^ fade_left:
                if fade_right:
                    current_heading += 5
                    if current_heading > 360:
                        current_heading -= 360
                else:
                    current_heading -= 5
                    if current_heading < 0:
                        current_heading += 360

            trim_values = trim(current_heading)
            print("Current heading: {}, Trim: {}".format(current_heading, trim_values))

            if STOP_TRANS == direction_modifier:
                MOTOR_ONE_POS_WRITE(MOTOR_OFF)
                MOTOR_ONE_NEG_WRITE(MOTOR_OFF)
                MOTOR_TWO_POS_WRITE(MOTOR_OFF)
                MOTOR_TWO_NEG_WRITE(MOTOR_OFF)
            elif FORWARD_TRANS == direction_modifier:
                set_motor(MOTOR_ONE_POS_WRITE, MOTOR_ONE_NEG_WRITE, int(5 * trim_values[0]) + 300)
                set_motor(MOTOR_TWO_POS_WRITE, MOTOR_TWO_NEG_WRITE, int(5 * trim_values[1]) + 300)
            elif BACKWARD_TRANS == direction_modifier:
                set_motor(MOTOR_ONE_NEG_WRITE, MOTOR_ONE_POS_WRITE, int(5 * trim_values[1]) + 300)
                set_motor(MOTOR_TWO_NEG_WRITE, MOTOR_TWO_POS_WRITE, int(5 * trim_values[0]) + 300)
            else:
                MOTOR_ONE_POS_WRITE(MOTOR_OFF)
                MOTOR_ONE_NEG_WRITE(MOTOR_OFF)
                MOTOR_TWO_POS_WRITE(MOTOR_OFF)
                MOTOR_TWO_NEG_WRITE(MOTOR_OFF)

        except Exception:
            set_motor(MOTOR_TWO_POS_WRITE, MOTOR_TWO_NEG_WRITE, 0)
            set_motor(MOTOR_ONE_POS_WRITE, MOTOR_ONE_NEG_WRITE, 0)
