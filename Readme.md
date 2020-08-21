# This project builds up on <https://healthchecks.io/> to allow you to monitor APIs using healthchecks  

The app checks the status of APIs defined in `apis.json` and if the API can be monitored(pinged) from this app, then the app sends a ping to Healthchecks letiing it know that the app is online. If the app can't ping an API, it doesn't ping healthchecks and thus healthchecks notifies us that the app is down.


### Running the project

In `apis.json`, replace everything with your actual API URL and Healthchecks ping url.

Create a virtualenv and do a pip install `requests`. If you are using pipenv you can just do a pipenv install.
execute the main app `python main.py` 
