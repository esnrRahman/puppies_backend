import os

basedir = os.path.abspath(os.path.dirname("__file__"))

PUPPIES_TESTDB_CONFIG = {
    "username": "root",
    "password": "password",
    "environment": "localhost",
    "name": "puppies_db"
}

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}/{}".format(PUPPIES_TESTDB_CONFIG["username"],
                                                               PUPPIES_TESTDB_CONFIG["password"],
                                                               PUPPIES_TESTDB_CONFIG["environment"],
                                                               PUPPIES_TESTDB_CONFIG["name"])

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')