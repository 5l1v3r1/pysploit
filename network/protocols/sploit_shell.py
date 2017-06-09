"""
Handles the upgrading of simple /bin/sh to a sploitshell that can perform in-memory process hopping, and other
operations that rely on stealthy fileless activity.
"""

from twisted.internet.protocol import Protocol, ClientFactory

class SploitShellUpgradeProtocol(Protocol):
	def __init__(self, reactor, factory, connection_details):
		self.reactor = reactor
		self.factory = factory
		self.connection_details = connection_details

	def connectionMade(self):
		print("[+]\tConnection made to {}".format("xxx"))

	def dataReceived(self, data):
		print("[*]\tData received from {}".format("xxx"))

	def disconnect_with_inactivity(self):
		print("[-]\tDisconnecting from {} due to inactivity".format("xxx"))