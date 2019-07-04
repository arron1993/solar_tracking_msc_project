import Data_Server

from threading import Thread



data_server = Data_Server.Data_Server()

start_thread = Thread(target=data_server.start_server)
start_thread.start()

request_thread = Thread(target=data_server.request_measurements)
request_thread.start()
