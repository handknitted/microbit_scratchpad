from microbit import *
import utime

display.off()
while True:
    pin6.write_digital(0)
    sleep(50)
    echo_stop = None
    pin6.write_digital(1)
    utime.sleep_us(10)
    trig_stop = utime.ticks_us()
    pin6.write_digital(0)
    utime.sleep_us(10)
    while echo_stop is None:
        if pin7.read_digital() > 0:
            while pin7.read_digital() > 0:
                if trig_stop - utime.ticks_us() > 1000:
                    break
                    break
            echo_stop = utime.ticks_us()
    if echo_stop is not None:
        stop_delay = echo_stop - trig_stop  
        print(stop_delay)
        print("Delay = %s" % str(stop_delay))
        print("Distance = %s" % str((stop_delay * 343)/2000000))
    else:
        print("No appreciable echo")