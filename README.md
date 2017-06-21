# Demo Puppies Backend app using the following technologies -

* Framework -> Flask
* Language -> Python
* DB -> MySQL
* Migration tool -> Alembic

## Pre-Requirements ->

* MySQL installed
* A db is created that is called *puppies_db*
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

* Run test script

`./test.sh`

#### Caveats -
