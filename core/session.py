"""
Session module for pysploit

Handles interaction with a single host and exploitation of host
"""
import uuid
from core.constants import PROMPT, EXPLOIT_INPUT_HELP_MESSAGE, \
							EXPLOIT_LOAD_BEFORE_USE_MESSAGE
from network.manager import NetworkManager
import threading

class Session:
	def __init__(self):
		self.name = uuid.uuid4().hex
		self.exploit = None
		self.remote_connection = None
		self.prompt = PROMPT["pysploit"]
		self.handler = None

		# state stuff
		self.waiting_on_response = False

	def set_exploit(self, exploit_to_use):
		"""Sets the session's exploit

		Input: <Exploit> from pysploit.core.exploits.*

		Changes the exploit to the exploit object that was passed. Also changes the
		prompt dynamically to the name of the exploit that was set. Also sets the
		name of the session to the name of the exploit currently in use.
		"""
		self.exploit = exploit_to_use
		self.exploit.set_session(self)
		self.name = self.exploit.vuln_name

	def get_prompt(self):
		"""Returns the terminal prompt for the current context
		"""

		# TODO
		# first check to update prompt
		if self.exploit is not None:
			self.prompt = "exploit ({})> ".format(self.exploit.vuln_name)
		elif self.remote_connection is not None:
			self.prompt = "remote@{}> ".format(self.remote_connection.ip)
		return self.prompt

	def set_exploit_field(self, exploit_field_args):
		"""Sets a field of the exploit

		Input: string

		Prompts an error if there is not an exploit set in the session yet.
		Otherwise, passes the values onto the exploit to be set.
		"""
		self.exploit.set_option(exploit_field_args[0], exploit_field_args[1])

	def show_exploit_options(self):
		"""Shows the current state of all exploit options

		If the exploit is unset, it returns a message telling the user to set
		the exploit to use. Otherwise, list the state of all relevant user-set
		fields of the exploit that must be set before exploitation can be
		performed.
		"""
		if self.exploit is None:
			print (EXPLOIT_LOAD_BEFORE_USE_MESSAGE)
			print (EXPLOIT_INPUT_HELP_MESSAGE)
		else:
			self.exploit.show_exploit_options()

	def show_exploit_info(self):
		"""Shows overview information about the exploit 
		
		Shows the user background information about the exploit including
		relevant disclosure IDs, short summary, and targeted architecture for
		the module.
		"""
		if self.exploit is None:
			print (EXPLOIT_LOAD_BEFORE_USE_MESSAGE)
			print (EXPLOIT_INPUT_HELP_MESSAGE)
		else:
			self.exploit.show_exploit_info()

	def run_exploit(self):
		"""
		Run a loaded exploit

		Runs the active exploit for the session. Will throw an error if there
		is not an exploit loaded for the given session. Should also throw an
		error at the exploit level if all necessary options are not configured.
		"""
		if self.exploit is None:
			print (EXPLOIT_LOAD_BEFORE_USE_MESSAGE)
			print (EXPLOIT_INPUT_HELP_MESSAGE)
		else:
			self.exploit.run()

	def set_connection(self, remote_connection):
		"""
		Sets the connection of the session. Performed by connection protocol on connection.

		:param connection:
		"""
		print("[*] Attaching remote connection to session")
		self.remote_connection = remote_connection
		print("[+] Remote connection attached to session successfully")

	def update_waiting_on_response(self, waiting=False):
		if waiting is True:
			print("[*] waiting on remote response")
			self.waiting_on_response = waiting
		else:
			print("[+] received remote response")
			self.waiting_on_response = waiting
