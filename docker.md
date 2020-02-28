# Basic Docker Setup

### Create the docker image

Make a directory and create a file called Dockerfile inside that directory.

```
mkdir docker_dir
cd docker_dir
touch Dockerfile
```

Insert this code into the Dockerfile.

```
# In path/to/your/dev/folder/Dockerfile
# Base Image
FROM python:3.6

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 8000

CMD python -c "print('hello world')"

```

Line by line explanation: 

```
FROM python 3.6
```
This will build the image from another pre-exsiting Python 3.6 image.


```
RUN apt-get update && apt-get install -y --no-install-recommends \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
```
RUN is doing bash shell commands for updates and installs.

```
EXPOSE 8000
```
This will expose a port.

```
CMD python -c "print('hello world')"
```
This will run a command to print "hello world" in python.

Now check if the dockerfile was properly saved.

```
cat Dockerfile
```

Now build the dockerfile.

```
docker build -t hello-world -f Dockerfile .
```

### Commands

Shows all the images that you have.

```
docker iamges
```

Shows all the containers that are running.

```
docker ps -a
```

Creates a container from your tagged image.

```
docker run -it <tag-name>
```

Stop a docker instance.

```
docker stop <continer id>
```

Remove a docker instance
```
docker rm <continer id>
```

Enter bash shell in docker
```
docker run -it <tag-name> /bin/bash
```

You can enter python from the bash shell by typing in `python` and exit python by typing `exit`



