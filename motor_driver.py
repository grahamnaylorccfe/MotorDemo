import numpy as np
from scipy import signal
import time
import zmq
import json

#import sys

data = {'values': None}

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://10.0.0.63:5555")

def update_axis_1():

    global data
    socket.send(b'GET {"table":"reportPIMotor", "filters":{"key":"axis1Pos"}, "columns":["value"]}')
    time.sleep(0.1)
    position=str(socket.recv())
    PIMotor=json.loads(position[9:-1])["reportPIMotor"]
    actual_position=float(PIMotor[0]['value'][2:])
    data['values'] = actual_position
    

def set_axis_1(angle):
    ToSend='PUT {"table":"settingsPIMotor", "filters":{"key":"axis1Position"}, "data":{"value":"'+str(angle)+'"}}'
    socket.send(bytes(ToSend,'UTF-8'))
    rx = socket.recv()
    
