from microbit import *


def get_pot():
    return pin0.read_analog()


def display_left(intensity):
    display.clear()
    for row in (0,1,2,3,4):
        for col in (0,1):
            display.set_pixel(col, row, int(intensity))


def display_right(intensity):
    display.clear()
    for row in (0,1,2,3,4):
        for col in (3,4):
            display.set_pixel(col, row, int(intensity))


def display_mid():
    display.show(
        Image("00900:"
              "00900:"
              "00900:"
              "00900:"
              "00900:"))


def get_intensity(pot_value):
    return (pot_value - 1) // 45


while True:
    pot_value = get_pot()
    if pot_value < 450:
        display_left(get_intensity(450 - pot_value))
    elif pot_value > (1023 - 450):
        display_right(get_intensity(pot_value - (1023 - 450)))
    else:
        display_mid()
