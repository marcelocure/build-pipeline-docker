import os

def get_environment_variable(name):
	try:
		return os.environ[name]
	except:
		return None

registry = get_environment_variable("REGISTRY") or "localhost:5000"
user = get_environment_variable("USER") or "curecure"
base_dir = get_environment_variable("BASE_DIR") or "/home/marcelocure/github/"