# fastapi-docker-treafik

Project how to dockerize a python app.

## Links

* https://www.youtube.com/watch?v=SORiTsvnU28
* https://testdriven.io/blog/fastapi-docker-traefik/
* https://www.youtube.com/watch?v=qC8AJzML3E4

## Running uvicorn

Keep uvicorn reloading changes

    $ uvicorn app.main:app --reload

## Docker

Build the docker images

    $ docker-compose build –no-cache

Run the docker image

    $ docker-compose up -d

Stop the docker image

    $ docker ps
    CONTAINER ID   IMAGE                        COMMAND                  CREATED          STATUS          PORTS                                       NAMES
    342ac02fdd43   fastapi-docker-traefik_web   "uvicorn app.main:ap…"   52 seconds ago   Up 52 seconds   0.0.0.0:8008->8000/tcp, :::8008->8000/tcp   fastapi-docker-traefik_web_1
    $ docker stop 342ac02fdd43

## Debug docker

    $ docker-compose logs

## Swagger docs

The swagger docs are available at

    http://<hostname>:<port>/docs

## Redoc

The redoc you find

    http://<hostname>:<port>/redoc



    

