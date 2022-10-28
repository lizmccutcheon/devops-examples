
## Istio service mesh
### Architecture 
- A single mysql Deployment and its associated Service, PersistentVolume, PersistentVolumeClaim and Configmap. These  are identical to those in the kubernetes section.
- Two versions of the userapi Deployment, and an associated Service (userapi-service). Almost identical to that found in kubernetes section, except now there are 2 versions. Additionally the load balancer on the service is no longer required as we will use a gateway instead to access the application.
- A DestinationRule, which defines 2 subsets of the userapi-service (corresponding to the 2 versions of the application deployed).
- A Gateway, which is a load balancer which controls http/tcp traffic at the edge of the istio mesh.
- A VirtualService, which applies traffic routing to the userapi-service.  

The architecture looks like this :  
![architecture](https://github.com/lizmccutcheon/devops-project/blob/main/architecture.png)

### Manifests
In the deployment folder:  
- `app-deployment-two-version.yaml`, which contain the application deployment + service
- `mysql-deployment.yaml`, which contains the mysql deployment + service
- `persistent-volume-claim.yaml`, which contains the PVC and ConfigMap definitions for mysql storage and initialization.
- `secrets.yaml`, which contains the necessary environment variables
- `gateway.yaml`, which is the config for the Gateway
- `destination-rules.yaml`, which defines the subsets of the userapi service
- `virtual-service-default.yaml`, which configures the default routing rules.  

In the configuration folder (details below in Configuration section):  
- `virtual-service-percentage.yaml`
- `virtual-service-routing.yaml`  

In the addons folder:  
- yaml for kiali, grafana, etc. (default setup provided on kubernetes installation). As the two versions of the deployed app look identical, kiali can be installed and used to visualise the architecture and traffic.

### How to run
It is assumed that you already have virtualization software (e.g VirtualBox) with minikube, kubectl and istioctl installed. Instructions 
- enable istio injection into the default namespace : `kubectl label namespace default istio-injection=enabled`
- `kubectl apply -f deployment/`
- get ingress host name : `export INGRESS_HOST=$(minikube ip)`
- get ingress port : `export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].nodePort}')`
- get the userapi url : `export GATEWAY_URL=$INGRESS_HOST:$INGRESS_PORT && echo $GATEWAY_URL`
- Start a tunnel with `minikube tunnel`
- The application can now be viewed in your browser at $GATEWAY_URL  

The above steps launch the default application set-up, i.e. with no special routing rules applied.

### Configuration
Three routing configurations have been provided.  
1. Default configuration
- In `deployment/virtual-service-default.yaml`.
- Applied when following the instructions in the section above.
- Sends all http traffic through to the userapi-service.
- No additional traffic management - userapi-service defaults to a round-robin strategy i.e. 50% of traffic goes to each of v1 and v2 of the app.
2. Request routing  
- In 'configuration/virtual-service-routing.yaml'
- To apply this configuration, first remove the existing virtual service with `kubectl delete virtualservice --all` then do `kubectl apply -f configuration/virtual-service-routing.yaml`
- This configuration sends incoming traffic to homepage or /hello endpoint to v1 of userapi and all other traffic to v2.
3. Traffic shifting  
- In 'configuration/virtual-service-percentage.yaml'
- To apply this configuration, first remove the existing virtual service with `kubectl delete virtualservice --all` then do `kubectl apply -f configuration/virtual-service-percentage.yaml`
- This configuration sends 80% of incoming traffic to v1 of userapi and 20% to v2.

(As both versions of the front-end appear idential, traffic can be visualised with kiali)
