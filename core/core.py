import os
import sys
import threading
from pydoc import locate

from core.session import Session
from core.constants import 	INTEGER_VALUE_ERROR_MESSAGE, SESSION_INDEX_TYPE_ERROR, \
							CORE_INPUT_HELP_MESSAGE, SESSION_INPUT_HELP_MESSAGE, \
							EXPLOIT_INPUT_HELP_MESSAGE, INVALID_EXPLOIT_ERROR, \
							INTRO_ART, SESSION_BY_NAME_FAILURE


class Core:
	"""Core module for pysploit
	"""
	def __init__(self):
		# array: holds all of the sessions for the core
		self.sessions = []
		# <Session>: active session
		self.active_session = None
		# integer: index of the currently active session
		self.active_session_index = 0
		# <NetworkHandler>: self-explanatory

	def new_session(self):
		"""Create a new session
		
		Produces a new session and adds it to the core's list of session objects.
		The active session is then set to the newly created session.
		"""
		new_sess = Session()
		self.sessions.append(new_sess)
		self.active_session_index = len(self.sessions) - 1
		self.active_session = self.sessions[self.active_session_index]

		print ("[+]	New session created")

	def delete_session(self, session_index):
		"""Deletes a session from the core

		Input: integer

		Deletes the session from the core that corresponds to the given index
		"""
		try:
			del self.sessions[int(session_index)]
		except ValueError as ve:
			print (INTEGER_VALUE_ERROR_MESSAGE)
		except TypeError as te:
			print (SESSION_INDEX_TYPE_ERROR)

	def list_sessions(self):
		"""View all sessions in the core

		Lists all of the sessions in the core. Additionally the active session
		is marked.
		"""
		print ("[*]	Current sessions:")
		for idx, session in enumerate(self.sessions):
			if idx == self.active_session_index:
				print ("  [{}]	{} **Active**".format(idx, session.name))
			else:
				print ("  [{}]	{}".format(idx, session.name))

	def change_active_session(self, session_index):
		"""Change the active session to the given session

		Input: integer

		First lists all of the active sessions, and then attempts to switch to
		the given index of the desired active session.
		"""

		try:
			self.active_session_index = int(session_index)
			self.active_session = self.sessions[self.active_session_index]
			print ("[+]	Successfully changed sessions")
			self.list_sessions()
		except ValueError as ve:
			print (INTEGER_VALUE_ERROR_MESSAGE)
		except TypeError as te:
			print (SESSION_INDEX_TYPE_ERROR)

	def get_prompt(self):
		"""Gets the prompt for the command terminal

		Prompt depends on the terminal context. i.e.
			staging is a pysploit prompt
			post-exploitation on windows is a windows prompt
			post-exploitation on linux is a linux prompt
		"""
		return self.active_session.get_prompt()

	def load_exploit(self, exploit_to_load):
		"""Loads a given exploit to the active session

		Checking for exploit validity happens in this method. The check is a
		dynamic module load from the exploits module dir. If we don't get an
		error, then the exploit exists. If we get an error, the exploit was
		not entered correctly. Accession-by-title.
		"""
		#try:
		exploit_module = locate("exploits." + exploit_to_load.strip() + "." + exploit_to_load.strip())
		exploit_instance = exploit_module()
		self.active_session.set_exploit(exploit_instance)
		#except ModuleNotFoundError as mnfe:
		#	print ("{}\n\t[*] Entered: {}".format(INVALID_EXPLOIT_ERROR, exploit_module_name))

	def get_session_by_name(self, session_name):
		"""Returns a session in the core by its name. Error if no session exists by that name

		:param session_name:
		:return: Session or SESSION_BY_NAME_FAILURE
		"""
		for session in self.sessions:
			if session.name == session_name:
				return session
			else:
				return SESSION_BY_NAME_FAILURE

	def display_core_help(self):
		"""Display the help message for session commands"""

		print (CORE_INPUT_HELP_MESSAGE)

	def exit_pysploit(self):
		print ("[*] Saving state\t\t\t\t(not implemented)")
		print ("[*] Closing off connections\t\t(not implemented)")
		print ("[*] Exiting")
		sys.exit(0)

	def clear_screen(self):
		os.system("clear")

	# TODO convert to getopt...
	def process_input(self, sploit_command):
		"""Handles input to pysploit

		...
		"""
		#input_context = self.get_input_context() # TODO this is a better way of doing commands

		args = sploit_command.strip().split(" ")
		if self.active_session.has_shell():
			self.active_session.send_command(sploit_command)
		elif args[0] == "session":
			# process in context of session commands
			if args[1] == "help":
				print(SESSION_INPUT_HELP_MESSAGE)
			elif args[1] == "list":
				self.list_sessions()
			elif args[1] == "delete":
				self.delete_session(args[[2]])
			elif args[1] == "change":
				self.change_active_session(args[2])
			elif args[1] == "new":
				self.new_session()
			else:
				print(SESSION_INPUT_HELP_MESSAGE)

		elif args[0] == "exploit":
			# process in context of exploit commands
			if args[1] == "load":
				self.load_exploit(args[2])
			elif args[1] == "set":
				self.active_session.set_exploit_field(args[2:])
			elif args[1] == "options":
				self.active_session.show_exploit_options()
			elif args[1] == "info":
				self.active_session.show_exploit_info()
			elif args[1] == "check":
				self.active_session.check_exploit_vulnerability()
			elif args[1] == "run":
				self.active_session.run_exploit()
			else:
				print(EXPLOIT_INPUT_HELP_MESSAGE)

		else:
			# process in dynamic context
			if args[0] == "exit":
				self.exit_pysploit()
			elif args[0] == "clear":
				self.clear_screen()
			else:
				print(CORE_INPUT_HELP_MESSAGE)

	def preinput_processing(self):
		"""
		Ensures that we wait until timeout before passing on a sent request (twisted shell). Ensures that
		requests and responses to external resources are printed and processed before the next input
		sequence.
		"""
		# print("[*] Pre-processing before next input")
		if self.active_session is not None:
			while self.active_session.waiting_before_input():
				pass
		# print("[+] Pre-processing complete")

	def run(self,new_startup_session=True):
		"""Runs the core"""

		# give us a session to start with
		if new_startup_session:
			self.new_session()

		# initialize everything
		print("[*] Initializing all the initializables")

		# intro art
		print(INTRO_ART)

		while True:
			try:
				self.preinput_processing()
				sploit_command = input("{}".format(self.get_prompt()))
				self.process_input(sploit_command)
			except KeyboardInterrupt as ke:
				print ("\n[*] Caught keyboard interrupt.")
				exit = input("	Would you like to exit? (y/n): ")
				if exit.lower() == "y" or exit.lower() == "yes":
					self.exit_pysploit()
				else:
					print ("[*]	Continuing")












