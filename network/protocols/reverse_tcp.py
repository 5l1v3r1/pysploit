"""
Handles a reverse tcp connection from a compromised target.

Catches the shell and interacts with it, passing commands and arguments to and from the remote shell.
"""
from twisted.internet.protocol import Protocol, ClientFactory

class ReverseTCPProtocol(Protocol):
	def __init__(self, reactor, factory, connection_details):
		self.reactor = reactor
		self.factory = factory
		self.connection_details = connection_details

	def connectionMade(self):
		pass

	def dataReceived(self, data):
		pass

	def disconnect_with_inactivity(self):
		pass

class ReverseTCPFactory(ClientFactory):
	def __init__(self, reactor, connection_details):
		self.reactor = reactor
		self.connection_details = connection_details
		self.connections = []

	def startedConnecting(self, connector):
		print("[*] starting connection to xxx")

	def buildProtocol(self, addr):
		protocol = ReverseTCPProtocol(self.reactor, self, self.connection_details)
		self.connections.append(protocol)
		return protocol

	def clientConnectionLost(self, connector, reason):
		print("[!] connection lost to xxx")

	def clientConnectionFailed(self, connector, reason):
		print("[!] connection failed to xxx")
