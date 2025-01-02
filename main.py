from machine import Pin, PWM,UART
import utime
from time import sleep

pwm= PWM(Pin(15))
pwm.freq(50)
uart = UART(0,9600)

trigger = Pin(6, Pin.OUT)
echo = Pin(7, Pin.IN)
distance = 0
led=Pin(17,Pin.OUT)
led1=Pin(5,Pin.OUT)
led2=Pin(10,Pin.OUT)
led3=Pin(22,Pin.OUT)

def servo(angle):
    c= int((34.45*angle)+1800)
    pwm.duty_u16(c)

def get_distance():
    global distance
    trigger.high()
    utime. sleep(0.00001)
    trigger.low()
    while echo.value() == 0:
        start = utime.ticks_us()
        
    while echo. value() == 1:
        stop = utime.ticks_us()
    duration = stop - start
    distance = (duration *0.0343)/2
    print(distance,"cm")
    
    
    return distance

while True:
    
    get_distance()
    
    sleep(2)
    if uart.any(): 
        data=uart.read() #Getting data
        data=str(data)
        data=data[2:-5]
        print(data)
        if  'a' in data:
            while True:
                get_distance()
                if distance>30:
                    servo(0)
                    led.value(0)
                    led2.value(0)
                    led3.value(0)
                if distance>20 and distance<30:
                    servo(45)
                    led.value(0)
                    led2.value(0)
                    led3.value(0)
                if distance>15 and distance<20:
                    servo(90)
                    led.value(0)
                    led2.value(0)
                    led3.value(1)
                if distance>10 and distance<15:
                    led.value(0)
                    led2.value(1)
                    led3.value(1)
                    servo(120)
                if distance >1 and distance<10:
                    led.value(1)
                    led2.value(1)
                    led3.value(1)
                    servo(180)
                sleep(3)
                if uart.any(): #Checking if data available
                    data=uart.read() #Getting data
                    data=str(data)
                    data=data[2:-5]
                    print(data)
                    if 'b' in data:                 
                         while True:
                            if uart.any(): #Checking if data available
                                data=uart.read() #Getting data
                                data=str(data)
                                data=data[2:-5]
                                print(data)
                                if 'a' in data:
                                    break
                                if int(data)>150:
                                    led.value(1)
                                    led2.value(1)
                                    led3.value(1)
                                if int(data)>100 and int(data)<=150:
                                    led.value(0)
                                    led2.value(1)
                                    led3.value(1)
                                if int(data)>50 and int(data)<=100:
                                    led.value(0)
                                    led2.value(0)
                                    led3.value(1)
                                if int(data)<=50 :
                                    led.value(0)
                                    led2.value(0)
                                    led3.value(0)
                                servo(int(data))