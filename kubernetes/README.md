## Kubernetes Deployment
### Contents
The following configuration files are located in `./deployment`:
1. `secrets.yaml`, which contains a template for the environment variables to be used by the deployed containers.
2. `persistent-volume-claim.yaml`, which consists of a PersistentVolumeClaim for the mysql backend and a ConfigMap to initialize the database.
3. `mysql-deployment.yaml`, which consists of a Deployment for the mysql container and its associated Service. The deployment pulls the mysql image from Docker hub, mounts the persistent volume and sets port for communication. The mysql root password is retrieved from kubernetes secrets.
4. `app-deployment.yaml`, which consists of Deployment for the userapi container and its associated Service. The deployment pulls the app image from Docker hub, sets the port for communication and passes environment variables to the application from kubernetes secrets.

### How to run
The below assumes you already have virtualization software (e.g VirtualBox) with minikube and kubectl installed.
- pull the repository and make sure the VM is running
- `kubectl apply -f deployment/`
- `minikube ip` to get minikube ip address
- `kubectl get svc` to determine the port mapping of the userapi-service (port 8000 will be mapped/forwarded to a randomly assigned external port)
- visit `http://<minikube ip>:<external port>` to see the application.



