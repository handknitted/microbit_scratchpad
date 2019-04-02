from microbit import *

compass.calibrate()

MOTOR_ON = 720
MOTOR_OFF = 0

MOTOR_ONE = 'one'
MOTOR_TWO = 'two'

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


headings = [45, 270, 15, 180, 0]

for heading in headings:
    on_heading = False
    while not on_heading:
        on_heading = turn_to_heading(heading)
    sleep(10000)

print('Finished')
