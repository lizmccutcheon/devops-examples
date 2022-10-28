## DevOps examples
A basic web application and various methods of deploying it. Originally developed as an assessment for the DevOps unit, [Applied MSc in Data Engineering for Artificial Intelligence](https://www.datasciencetech.institute/applied-msc-in-data-engineering-for-artificial-intelligence/) at [DSTI](http://www.datasciencetech.institute).

### Contents
- `userapi` : CRUD API in Python/Flask, with Swagger implementation, suite of unit tests and Dockerfile, deployed to Heroku using GitHub CI.
- `userapi_mysql` : Same application with MySQL backend
- `dockercompose` : Container orchestration with Docker Compose
- `kubernetes` : Container orchestration using Kubernetes
- `istio` : Istio service mesh deploying two versions of the front-end with a shared back end. Default, percentage-routing and traffic routing configuration options provided.

The application can be seen at https://my-stupid-flask-api.herokuapp.com/  

Documentation for each deployment methodology can be found in the relevant folders.

#### Author
Liz McCutcheon  
October 2022  