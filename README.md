

I have included comments the views.py and test.py, explaining what parts of the code do.


Exercise part 1. -  Webserver 


Ensure docker is installed follow this link - https://docs.docker.com/docker-for-mac/install/

In terminal run  git clone https://github.com/Ralphap/webserver.git  to save repo in location of choice

$cd webserver

$docker-compose build

$docker compose up

site should be up and running on localhost http://127.0.0.1:8000/





Exercise part 2 - automated functional test  


Follow guide to install the chromedriver  (I refer to this https://www.swtestacademy.com/install-chrome-driver-on-mac/). 

This needed to launch the chrome browser so selenium can execute test script


Make sure Python3 is installed run, Pip3 is installed with Python3 

$ brew install python3


To install virtualenv via pip run

$ pip3 install virtualenv


In the webserver directory create

python3 -m venv  <“name”>

start the virtual environment(activate)

source <“name”>/bin/activate

Install the project dependencies:

pip install -r requirements.txt 

run python3 manage.py test 

This starts the functional test, make sure open different terminal to where you deployed webserver image

if ok come back test has passed
