"""
Class that handles network interaction for pysploit
"""
from twisted.internet import reactor
from network.protocols.reverse_tcp import ReverseTCPFactory
from core.constants import REVERSE_TCP

class NetworkManager:
	def __init__(self, session):
		self.session = session
		self.active_factories = []

	def add_handler(self, handler_type, port):
		"""Starts a network handler of a given type on the given port.

		A network handler generally acts as a pass-between for connections and pysploit sessions.
		"""

		if handler_type == REVERSE_TCP:
			print("[*] Setting up a reverse tcp handler listening on port {}".format(port))
			reverse_factory = ReverseTCPFactory(self.session)
			reactor.listenTCP(port, reverse_factory)
			self.active_factories.append(reverse_factory)
			print("[+] Handler added successfully")

	def start(self):
		print("[*] Starting the network handler")
		reactor.run(installSignalHandlers=0)
		print("\t[+] Network handler started successfully!")
