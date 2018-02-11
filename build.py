import docker
from config import registry, user

name="todo-api"
tag="{0}/{1}/{2}".format(registry, user, name)

client = docker.from_env()
client.images.build(path="/home/marcelocure/github/todo-api", tag=tag)
client.images.push(repository=tag)
