import RPi.GPIO as GPIO
from time import sleep

class Servo_Controller:
    def __init__(self,pin):
        self.pin = int(pin)
        self.current_angle = 0
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def update(self,angle): 

        print("MOVEMENT: Pin {} moving to {} degrees".format(self.pin,angle))
        angle = float(angle)       
        duty_cycle = 1/18 * (angle) + 2
        self.pwm.ChangeDutyCycle(duty_cycle)
        self.current_angle = angle
        sleep(0.5)

        

    def start(self):
        self.pwm = GPIO.PWM(self.pin,50)
        self.pwm.start(7)


    def stop(self):
        self.pwm.stop()
