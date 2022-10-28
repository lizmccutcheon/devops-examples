## To run
### Locally 
`docker build -t userapi .`   
`docker run -p 5000:5000 userapi`  

The app will then be available on localhost:5000 (running on the built-in Flask development server).  

### With Gitlab CI
The workflow is set up to deploy to Heroku on push to `/userapi` folder on `master` branch. A Procfile is also provided to enable using gunicorn as WSGI server on Heroku.  

If deploying to Heroku, you will also need to add your api key and email to GitHub Secrets.

At the time of development, there was an ongoing security issue which resulted in Heroku suspending GitHub integration - see https://status.heroku.com/incidents/2413. A community workflow, which allowed push to Heroku, was used as a workaround - see https://github.com/AkhileshNS/heroku-deploy.  

## Endpoints
The following endpoints are available :
 - /hello [GET] - Say hello, awww!
 - /swagger [GET]- API docs
 - /users [GET] - Retrieve all users in DB (only the very best security around here)
 - /users/{username} [GET | POST | DELETE] -  Get/update/delete a user
 - /health [GET] - Healthcheck
 - / [GET] - Super home page
  
[Link to app on Heroku](https://my-stupid-flask-api.herokuapp.com/) 

