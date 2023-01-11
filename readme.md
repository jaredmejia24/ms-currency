# Currency exchange API

## Prerequisites

Have installed docker and python

## Build

Steps to build a Docker image:

1.  Clone this repo

        git clone https://github.com/jaredmejia24/ms-currency.git

2.  Build both images the backend server with the name api_reservations and the PostgreSQL database with the name db_reservations

        docker compose build

3.  Run the images. It will automatically run in port 8000

        docker compose up

4.  Once everything has started up, you should be able to access the webapp via [http://localhost:8000/](http://localhost:8000/) on your host machine.

## Documentation 

