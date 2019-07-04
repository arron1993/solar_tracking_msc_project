from time import sleep
from threading import Thread

import Scanner
import Tracker
import Voltmeter
import Servo_Controller

class Solar_Panel:
    def __init__(self,channel,angle_mode,gpio_pin):
        self.ANGLE_MODE = angle_mode #S=scanner, F=fixed, T=Tracked
        self.GPIO_PINS = gpio_pin #Servo gpio pin(s)
        self.CHANNEL = int(channel) #ADC Channel
        self.voltage = 0 #current voltage
        self.angle = 0 #current angle
        self.DELAY_MINUTES = 15
        self.DELAY = self.DELAY_MINUTES * 60 #calculate delay in seconds

        self.voltmeter = Voltmeter.Voltmeter(channel)

    def _start_SA_scanner(self):
        while 1:
            scanner = Scanner.Scanner(self.GPIO_PINS,self.CHANNEL)
            best_angle = scanner.scan()
            self.angle = best_angle
            scanner.set_angle(best_angle)
            sleep(self.DELAY)

    def _start_DA_scanner(self):
        while 1:
            scanner = Scanner.Scanner(self.GPIO_PINS,self.CHANNEL)
            best_angle = scanner.DA_scan()
            self.angle = best_angle

            sleep(self.DELAY)

    def _start_SA_tracker(self):
        while 1:
            tracker = Tracker.Tracker(self.GPIO_PINS)
            self.angle = tracker.SA_update()

            sleep(self.DELAY)  

    def _start_DA_tracker(self):
        while 1:
            tracker = Tracker.Tracker(self.GPIO_PINS)
            self.angle = tracker.DA_update()
            sleep(self.DELAY)  

    def initalise_tracking(self):
        if(self.ANGLE_MODE == "SA-S"):
            thread = Thread(target=self._start_SA_scanner)
            thread.start()
        elif(self.ANGLE_MODE == "SA-T"):
            thread = Thread(target=self._start_SA_tracker)
            thread.start()
        elif(self.ANGLE_MODE == "SA-F"):
            controller = Servo_Controller.Servo_Controller(self.GPIO_PINS[0])
            controller.start()
            controller.update(self.angle)
            controller.stop()
        elif(self.ANGLE_MODE == "DA-T"):
            thread = Thread(target=self._start_DA_tracker)
            thread.start()
        elif(self.ANGLE_MODE == "DA-S"):
            thread = Thread(target=self._start_DA_scanner)
            thread.start()
    def set_angle(self,angle):
        self.angle = angle

    def get_angle_mode(self):
        return self.ANGLE_MODE

    def get_channel(self):
        return self.CHANNEL

    def get_gpio_pin(self):
        pins = ""
        i = 0
        for pin in self.GPIO_PINS:
           pins += str(pin)
           if(i != len(self.GPIO_PINS)-1):
                pins += "+"
           i+=1
        return pins

    def get_voltage(self):
        self.voltage = self.voltmeter.get_voltage()
        return self.voltage

    def get_angle(self):
        return self.angle
