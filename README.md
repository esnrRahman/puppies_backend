# Demo Puppies Backend app using the following technologies -

* Framework -> Flask
* Language -> Python
* DB -> MySQL
* Migration tool -> Alembic

## Pre-Requirements ->

* MySQL installed
* A db is created that is called **puppies_db**
* virtualenv installed

### Steps before running test script ->

* Create a virtualenv with the following command

`virtualenv <venv_name>`

* Activate virtualenv

`source <venv_name>/bin/activate`

* Run requirements file

`cd puppies_backend`
<br/>
`pip install -r requirements.txt`

* Run alembic script

`alembic upgrade head`

* Run app

`python app.py`

* Run test script

`./test.sh`

#### Notes -

* Test script uses **curl** but I highly recommend using **Postman** to test API freely

* jpeg, jpg, png, gif images are supported for now

* Set up a simple bash script file to test basic core functionality


#### Caveats -

* Did not set up a testing codebase

* Did not set up a custom Exception handler for unsupported image files [Or any exception for that matter]

* Did not set up a proper reactions table for further feature addition (like multiple reactions)

* Did not set up a rate limiter for APIs that do not require login (i.e. cookie) to access

* Can upload any pic to be honest now. There is no code to validate that the pic is actually of a dog

