import docker
from config import registry, user, base_dir
client = docker.from_env()

def find_image(tag):
    return client.images.get(tag)

def parse_id(image):
    return image.id[7:]

def build_path(name):
    return base_dir+name

def build_tag(name):
    return "{0}/{1}/{2}".format(registry, user, name)

def tag_and_push(name):
    tag=build_tag(name)
    client.images.build(path=build_path(name), tag=tag)
    client.images.push(repository=tag)
    print "image {0} - {1} created and pushed".format(parse_id(find_image(tag)), tag)
