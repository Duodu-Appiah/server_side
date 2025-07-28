#import pandas as pd
#import quandl
#from math import sqrt
#from statistics import mean
#import numpy as np
#import matplotlib.pyplot as plt
#from collections import Counter
#from matplotlib import style
#import warnings
#from tkinter import *
import socket

import socket

host = 'localhost'
port = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    print(f"Server listening on {host}:{port}")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
