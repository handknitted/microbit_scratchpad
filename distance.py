from microbit import *
import utime

print("Starting")
display.off()
pin_trigger = pin10
pin_echo = pin1

PRE_TRIGGER_DELAY = 50
SPEED_OF_SOUND = 343.26  # metres per second


def get_distance():
    stopped_time = None
    started_time = None
    pin_trigger.write_digital(0)
    utime.sleep_ms(PRE_TRIGGER_DELAY)
    pin_trigger.write_digital(1)
    utime.sleep_us(10)
    pin_trigger.write_digital(0)

    start_time = utime.ticks_us()
    while not pin_echo.read_digital():
        started_time = utime.ticks_us()
        print(".")

    stop_time = utime.ticks_us()
    while pin_echo.read_digital():
        stopped_time = utime.ticks_us()

    began_at = started_time or start_time
    ended_at = stopped_time or stop_time
    #if utime.ticks_diff(ended_at, began_at) >= 0.04:
    #    print("Too close!")

    print("Started: {:f}, Start: {:f}, Stopped: {:f}, Stop: {:f}".format(
        started_time, start_time, stopped_time, stop_time))
    round_trip_elapsed_time = utime.ticks_diff(ended_at, began_at)
    print("Elapsed: {:f}".format(round_trip_elapsed_time))
    # round trip distance = speed of sound * elapsed time
    round_trip_distance = round_trip_elapsed_time * SPEED_OF_SOUND / 10000
    print("Round trip distance: {:f}".format(round_trip_distance))
    object_distance = round_trip_distance / 2
    print("Object distance: {:f}".format(object_distance))
    return object_distance


for _ in range(100):
    print("Distance: {:f}".format(get_distance()))
    sleep(3000)
