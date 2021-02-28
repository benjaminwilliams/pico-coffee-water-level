from machine import Pin
import time
import utime

trigger = Pin(11, Pin.OUT)
echo = Pin(12, Pin.IN)

def sensor():
    trigger.low()
    time.sleep(0.2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
        start = utime.ticks_us()
    while echo.value() == 1:
        end = utime.ticks_us()
    timePassed = end - start
    distance = (timePassed * 0.0343) / 2
    print(distance)
    return distance
    
    