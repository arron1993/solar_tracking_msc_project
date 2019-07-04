from threading import Thread
import time

import socket
import Solar_Panel

class Panel_Information_Server:
    def __init__(self,port):
        self.host = '0.0.0.0'
        self.port = int(port)        
        self.Solar_Panels = []



    def load_panel_information(self):

        file = open("Panel_Information.txt")
        lines = file.readlines()
        for line in lines:
            gpio_pins = []
            line = line.replace("\n","")
            line = line.replace("\r","")
            values = line.split(",")
            channel = values[0] #read channel from first index
            angle_mode = values[1]
            if(angle_mode == "DA-T" or angle_mode == "DA-S"):
                gpio_pins.append(values[2])#top
                gpio_pins.append(values[3])#bottom
            else:
                gpio_pins.append(values[2])

            temp = Solar_Panel.Solar_Panel(channel,angle_mode,gpio_pins)

            if(len(values) == 4 and angle_mode == "SA-F"):
                angle = values[3]
                temp.set_angle(angle)

            self.Solar_Panels.append(temp)

    def start_panel_tracking_systems(self):
        for panel in self.Solar_Panels:
            panel.initalise_tracking()

    def start_information_server(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           
        s.bind((self.host,self.port))
        print("INFO: Started Server on Port",self.port)
        s.listen(5)
        while 1:
            conn, addr = s.accept()
            conn_thread = Thread(target=self.handle_conn, args=(conn,))
            conn_thread.start()

    def _get_response_string(self):
        return_string = ""
        current_time = int(time.time())
        for panel in self.Solar_Panels:            
            channel = panel.get_channel()
            gpio_pin = panel.get_gpio_pin()
            angle_mode = panel.get_angle_mode()
            angle = panel.get_angle()
            voltage = panel.get_voltage()
            return_string += "{},{},{},{},{},{}/".format(current_time,channel,gpio_pin,angle_mode,angle,voltage)
        return return_string

    def handle_conn(self,conn):
        data = conn.recv(1024)
        data = self.decode(data)


        response = self._get_response_string()
        print(response)   
        response = self.encode(response)
        conn.send(response)
        conn.close()

    def encode(self, data):
        return data.encode("utf-8")

    def decode(self, data):
        return data.decode("utf-8")
