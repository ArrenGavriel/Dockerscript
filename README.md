### DOCKER DEMONSTRATION
This project was intended to demonstrate docker for building components of fullstack applications.
The images built in this project are:
- frontent image
- backend image
- database image [mongodb and mongo-express]

While the frontend and backend images were built from local image, the database images `mongo` and `mongo-express` were pulled from remote repository.

The build process was executed using Dockerfile within each component directory, as well as the `docker-compose.yml` in the root directory. 

The pre-built local images [frontend and backend] were already pushed on [docker hub](https://hub.docker.com/repository/docker/argav/dockerscript/general).
