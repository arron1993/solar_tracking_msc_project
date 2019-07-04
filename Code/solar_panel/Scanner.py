import Voltmeter
import Servo_Controller

import RPi.GPIO as GPIO
from time import sleep



class Scanner:
    def __init__(self,pins,channel):
        print("Scanner Started")
        self.current_angle = 0
        self.channel  = channel
        self.controller = Servo_Controller.Servo_Controller(pins[0])
        self.pins = pins

    def scan(self):
        angle = 0
        voltmeter = Voltmeter.Voltmeter(self.channel)

        best_angle = 0
        best_voltage = 0
        
        self.controller.start()      
        for angle in range(0,180,10):
            self.controller.update(angle)
            voltage = voltmeter.get_voltage()
            print("{} degrees {}V".format(angle,voltage))
            if(voltage > best_voltage):
                best_voltage = voltage
                best_angle = angle
        self.controller.stop()
        print("Scanning Complete.")
        return best_angle

    def DA_scan(self):
        bottom_controller = Servo_Controller.Servo_Controller(self.pins[0])
        top_controller = Servo_Controller.Servo_Controller(self.pins[1])
        voltmeter = Voltmeter.Voltmeter(self.channel)
        best_azimuth = 0
        best_elevation = 0
        best_voltage = 0
        bottom_controller.start() 
        top_controller.start() 
  
        for azimuth_angle in range(0,180,10):
            bottom_controller.update(azimuth_angle)                                   
            for elevation in range(20,120,10):
                top_controller.update(elevation)
                voltage = voltmeter.get_voltage()
                print("SCANNER: A: {}, E: {}, V: {}".format(azimuth_angle,elevation,voltage))
                if(voltage > best_voltage):
                    best_voltage = voltage
                    best_azimuth = azimuth_angle
                    best_elevation = elevation



        bottom_controller.update(best_azimuth)                                   
        top_controller.update(best_elevation)
        print("SCANNER: Scanning Complete.")
        print("SCANNER: Setting Best...")
        print("SCANNER:Azimuth: {} Elevation: {}".format(best_azimuth,best_elevation))
        bottom_controller.stop() 
        top_controller.stop()
        return_string = "{}+{}".format(best_azimuth,best_elevation)
        return return_string

    def set_angle(self,angle):
        self.current_angle = angle      
        self.controller.start()  

        self.controller.update(angle)
        self.controller.stop()




