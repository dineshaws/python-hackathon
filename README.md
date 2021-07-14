# python-hackathon

Microservice to run the the sync data for hackathon project

## Getting Started

These instructions will provide the necessary steps to build an environment to run the microservices locally or on the AWS environment.

## Prerequisite

- Linux;
- Python 3;
- Docker.

- The file app/infrastructure/config/config_factory.py contains settings of each environment (development, staging or production).

- The Dockerfile contains all the steps to create an image containing all the required infrastructure.

## Process Sumary


Steps:

* Read csv and seed data into accounts table;
* Read csv and seed data into transactions table;

## Service documentation

```
http://localhost:5001/docs#/
```

## Run code Locally

### Create a python virtualenv

If you already have a Python environment such as pyenv-virtualenv just create a new virtual environment, otherwise some basic steps to do so are:

* Install the virtualenv tool, if it hasn't been installed yet: `pip3 install virtualenv`;
* Create a new virtual environment inside the service directory, if it hasn't been created yet: `python3 -m venv env`;
* Activate the virtual env: `source env/bin/activate`;

### Export environment variables:

Have these globals exported *only in your local shell session* i.e. *NEVER* to be commited in any branch at all:

```
export ENV='development'
```

### Install python dependencies

```
pip3 install -r requirements.txt
```

### Start the server:

```
uvicorn app.server:app --reload --port 5001
```

- APIs: 

```
curl -X POST http://localhost:5001/api/v1/seed-data
```

### Build on local machine

Clone the project

```
git clone https://<YOU_USER_NAME>@github.org/dineshaws/python-hackathon.git
```

Within a shell session (terminal emulator opened), install docker (if not already) and then build the docker image:

```
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

```
docker build -t python-hackathon --build-arg ENV=development .
```

```
docker images
```

```
docker run -p 5001:5001 --network="host" --name python-hackathon python-hackathon
```