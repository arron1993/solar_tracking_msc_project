import Servo_Controller
import argparse
import Solar_Equations
from time import sleep
from math import degrees

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--pin", help="Pin")
parser.add_argument("-a", "--angle", help="Angle")
parser.add_argument("-t","--time",help="Time")
args = parser.parse_args()

if(args.angle == "E"):
    lat = 52.937609
    lng = -1.122017
    time = float(args.time) * 60 
    equations = Solar_Equations.Solar_Equations()

    azimuth_angle = equations.get_solar_azimuth(lat,lng,time)
    elevation = equations.get_solar_elevation(lat,lng,time)

    controller = Servo_Controller.Servo_Controller(args.pin)
    controller.start()
    controller.update(180 - elevation)
    #controller.update(180 - azimuth_angle)
    controller.stop()
elif(args.angle == "A"):
    lat = 52.937609
    lng = -1.122017
    time = float(args.time) * 60 
    equations = Solar_Equations.Solar_Equations()

    azimuth_angle = equations.get_solar_azimuth(lat,lng,time)
    elevation = equations.get_solar_elevation(lat,lng,time)

    controller = Servo_Controller.Servo_Controller(args.pin)
    controller.start()
    controller.update(180 - azimuth_angle)
    controller.stop()	
else:
    controller = Servo_Controller.Servo_Controller(args.pin)
    controller.start()

    controller.update(args.angle)

    controller.stop()
