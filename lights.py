from machine import Pin
import time

led0 = Pin(0, Pin.OUT)
led1 = Pin(1, Pin.OUT)
led2 = Pin(2, Pin.OUT)
led3 = Pin(3, Pin.OUT)
led4 = Pin(4, Pin.OUT)
led5 = Pin(5, Pin.OUT)
led6 = Pin(6, Pin.OUT)
led7 = Pin(7, Pin.OUT)
led8 = Pin(8, Pin.OUT)
led9 = Pin(9, Pin.OUT)

def reset():
    led0.off()
    led1.off()
    led2.off()
    led3.off()
    led4.off()
    led5.off()
    led6.off()
    led7.off()
    led8.off()
    led9.off()

def one():
    reset()
    led0.on()
    
def two():
    one()
    led1.on()
    
def three():
    two()
    led2.on()
    
def four():
    three()
    led3.on()

def five():
    four()
    led4.on()
    
def six():
    five()
    led5.on()
    
def seven():
    six()
    led6.on()

def eight():
    seven()
    led7.on()

def nine():
    eight()
    led8.on()
    
def ten():
    nine()
    led9.on()

    