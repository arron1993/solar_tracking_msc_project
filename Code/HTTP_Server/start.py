
import HTTP_Server
from threading import Thread


http_server = HTTP_Server.HTTP_Server()





http_server.start()

http_server_thread = Thread(target=http_server.start)
http_server_thread.start()
