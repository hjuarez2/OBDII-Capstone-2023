from machine import Pin, PWM
from time import sleep

IN1 = Pin(23, Pin.OUT)
IN2 = Pin(24, Pin.OUT)

speed = PWM(Pin(18))
speed.freq(1000)

while True:
        speed.duty_u16(10000)
        IN1.low()  #spin forward
        IN2.high()
        sleep(5)
        
        IN1.low()  #stop
        IN2.low()
        sleep(2)
        
        speed.duty_u16(20000)
        IN1.high()  #spin backward
        IN2.low()
        sleep(5)
        
        IN1.low()  #stop
        IN2.low()
        sleep(2)
    
        speed.duty_u16(30000)
        IN1.low()  #spin forward
        IN2.high()
        sleep(5)
        
        IN1.low()  #stop
        IN2.low()
        sleep(2)
        
        speed.duty_u16(40000)
        IN1.high()  #spin backward
        IN2.low()
        sleep(5)
        
