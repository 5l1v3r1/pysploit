from network.protocols.reverse_tcp import ReverseTCPFactory
from twisted.internet import reactor
import subprocess
from core.core import Core
from network.protocols.reverse_tcp import ReverseTCPFactory
from core.constants import REVERSE_TCP
import threading

test_core = Core()
test_core.new_session()
test_core.load_exploit("test_reverse_tcp")
test_core.active_session.run_exploit()
