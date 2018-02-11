# build pipeline docker
Project created to run a build of your application with docker and push to a configurable registry

## usage:
python main.py projectname

## It will
run docker-compose up on the project folder
build dockerfile
tag it
push to configurable registry