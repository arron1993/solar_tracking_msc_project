import socket
import sys
import datetime

from threading import Thread
from time import sleep

from database.database import Database


class Server:
    def __init__(self):
        print("Data Server Created")
        self.received_data = []

    def encode(self, data):
        return data.encode("utf-8")

    def decode(self, data):
        return data.decode("utf-8")

    def request_measurements(self):
        while 1:
            now = datetime.datetime.now()
            file_name = "./storage/{}{}{}".format(now.day,now.month,now.year)
            db = Database(file_name)            

            response = "ERROR: Response Not Defined"
            try:
                host = "192.168.0.13" #location of PIS
                port = 8501 # PIS port
                request = "hi" #irrelevant, PIS always returns everything
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((host,port))
                sock.send(self.encode(request))  
                response = sock.recv(1024)
                response = self.decode(response)
                db.insert(response)#insert into DB
                self.received_data.append(response) #response is the readings, append them onto end of list
                sock.close()
            except OSError as os_error:
                print(os_error)
                response = "ERROR: Could Not Connect to Data Server at {}:{}".format(host,port)

            sleep(1)
            
    def start_server(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if(len(sys.argv) > 1):
            port = sys.argv[1]
        else:
            port = 15000
            
        s.bind(('0.0.0.0',int(port)))
        print("Server Started on Port",port)
        s.listen(5)
        while 1:
            conn, addr = s.accept()
            conn_thread = Thread(target=self.handle_conn, args=(conn,))
            conn_thread.start()

    def handle_conn(self,conn):
        data = conn.recv(1024)
        data = self.decode(data)
        
        response = data
        args = data.split(" ")
        method_type = args[0]
        if(method_type == "GET_DATA"):
            property_ = args[1] #voltage, current power etc
            if(property_ == "A"): #get ALL
                quantity = int(args[2]) #how many
                total = len(self.received_data)
                if(quantity <= total):
                    response = ""
                    start = total - quantity
                    for i in range(start,total):
                        response = response + self.received_data[i] 
                else:
                    response = "ERROR: Quantity cannot exceed total"
        response = self.encode(response)
        conn.send(response)
