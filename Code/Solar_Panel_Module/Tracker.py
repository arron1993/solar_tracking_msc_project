import RPi.GPIO as GPIO
from time import sleep
from threading import Thread

import Solar_Equations
import Servo_Controller

class Tracker:
    def __init__(self,pins):
        self.equation = Solar_Equations.Solar_Equations()
        self.latitude = 53.540799
        self.longitude = -0.159103
        self.current_angle = 0
        self.pins = pins

        

    def SA_update(self):
        controller = Servo_Controller.Servo_Controller(self.pins[0])
        angle = 0
        
        current_time_minutes = self.equation.get_time(True)
        #current_time_minutes = 60*4
        azimuth_angle = self.equation.get_solar_azimuth(self.latitude,self.longitude,current_time_minutes)


        if(azimuth_angle >= 180):
            print("SA_UPDATE:",azimuth_angle)
            self.current_angle = "Dark - Evening"
            controller.start()
            controller.update(0) #reset to face east
            controller.stop()
        elif(azimuth_angle <= 0):
            self.current_angle = "Dark - Morning"
            angle = "dark"
            controller.start()
            controller.update(180) #reset to face west
            controller.stop()
            print("WARNING: Single Axis Tracking Inactive! It is Dark")
        else:
            self.current_angle = azimuth_angle
            controller.start()
            controller.update(180 - azimuth_angle) 
            controller.stop()
        return self.current_angle

    def DA_update(self):  
        time = self.equation.get_time(True)

        top_servo = Servo_Controller.Servo_Controller(self.pins[0]) #elevation
        bottom_servo = Servo_Controller.Servo_Controller(self.pins[1]) #azimuth

        azimuth_angle = self.equation.get_solar_azimuth(self.latitude,self.longitude,time)
        elevation = self.equation.get_solar_elevation(self.latitude,self.longitude, time)
        if(azimuth_angle >= 180):
            self.current_angle = "Dark - Evening"
            bottom_servo.start()
            bottom_servo.update(15)
            bottom_servo.stop()
        elif(azimuth_angle <= 0):
            self.current_angle = "Dark - Morning"
            angle = "dark"
            bottom_servo.start()
            bottom_servo.update(180) 
            bottom_servo.stop()
        else:
            self.current_angle = azimuth_angle
            bottom_servo.start()
            bottom_servo.update(180 - azimuth_angle) 
            bottom_servo.stop()
			


        if(elevation < 10):
            top_servo.start()
            top_servo.update(160)
            top_servo.stop()
        else:
            self.current_angle = "{}+{}".format(azimuth_angle,elevation)
            top_servo.start()
            top_servo.update(180 - elevation)
            top_servo.stop()

        return self.current_angle

