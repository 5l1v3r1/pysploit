from core.core import Core


test_core = Core()
test_core.new_session()
test_core.load_exploit("test_reverse_tcp")
test_core.active_session.run_exploit()
