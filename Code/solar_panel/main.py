import Panel_Information_Server
import Solar_Panel
import argparse

try:
    server = Panel_Information_Server.Panel_Information_Server(8501) #supply port number, host is always 0.0.0.0

    server.load_panel_information()

    server.start_panel_tracking_systems()

    server.start_information_server()
except KeyboardInterrupt:
    exit(1)
