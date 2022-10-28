#### To run
To run with Docker Compose :  
- pull the repository
- cd into dockercompose
- create a *.env* file (see *.env_example* in this directory for the variables required) and place it in the dockercompose directory.
- do `docker compose up`  
  
The app then will be available at http://localhost:8000

`docker-compose.yaml` pulls a pre-built image from Docker Hub. Alternatively you can build the same image with the Dockerfile and files in `userapi_mysql/app` directory.