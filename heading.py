from microbit import *


def get_angle_from_heading(desired_heading):
    angle_of_turn = compass.heading() - desired_heading
    absolute_turn = angle_of_turn - 180
    degrees_turn = 180 - (absolute_turn % 360)
    return degrees_turn

