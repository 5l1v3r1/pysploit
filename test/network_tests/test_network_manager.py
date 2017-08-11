from core.session import Session
from core.constants import REVERSE_TCP

test_session = Session()


test_session.network_manager.add_handler(REVERSE_TCP, 31337)
