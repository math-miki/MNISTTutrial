import socket
import sys, os
sys.path.append(os.pardir)
import numpy as np
from Common.layers import *
from Common.functions import *
import time
from tester import *

port = 10001
host = "192.168.1.237"
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #オブジェクトの作成
socket_client.connect((host, port))


data = np.load('params.npz')
tester = Tester(data['W1'], data['b1'], data['W2'], data['b2'])

def check():
    data = socket_client.recv(2048)
    if data!=b'':
        msg = str(data)
        data = setupData(msg)
        result = tester.predict(data)
        socket_client.send((str(result)).encode('utf-8'))

def setupData(msg):
    a = msg.split(',')
    a[0] = a[0][2]
    a[783] = a[783][0]
    print(a, len(a))
    data = np.zeros(784)
    for i in range(784):
        data[i] = int(a[i])
    return data

while True:
    check()
    time.sleep(0.01)
