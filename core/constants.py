prompt = {
	"pysploit": "pysploit> ",
}

INTEGER_VALUE_ERROR_MESSAGE = "	[!] Incorrect value specified in integer input"
SESSION_INDEX_TYPE_ERROR = "	[!] Session index must be an integer in range"
CORE_INPUT_HELP_MESSAGE = """[*] Usage:
	`session [command]`: 				interact with the active session
	`exploit [command]`: 				interact with exploitation
"""
SESSION_INPUT_HELP_MESSAGE = """[*] Usage:
	`session help`: 					show these help commands
	`session list`: 					show all sessions available
	`session delete [session number]`: 	delete session x
	`session change [session number]`: 	change session to session x
	`session new`: 						add a new session
"""
EXPLOIT_INPUT_HELP_MESSAGE = """[*] Usage:
	`exploit help`:						show these help commands
	`exploit load [exploit name]`:  	load the exploit of the given name
	`exploit search [search term]`: 	search for an exploit
	`exploit set [field] [value]`:		sets a field of the exploit
	`exploit execute`: 					executes the loaded and configured exploit
"""
INVALID_EXPLOIT_ERROR = "	[!] Invalid exploit. Please enter a valid exploit"
EXPLOIT_LOAD_BEFORE_USE_MESSAGE = "	[!] Load exploit before checking options"