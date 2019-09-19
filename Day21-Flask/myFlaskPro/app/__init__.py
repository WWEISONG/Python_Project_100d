# in Pyhton, a sub-directory that includes a __init__.py file is considered a
# package, and can be imported. When you import a package, the __init__.py 
# executes and defines what symbols the package exposes to the outside world

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# __name__ is the name of package that application in
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# the data that will be stored in the database will be represented by a collection
# of classes, usually called database models.The ORM layer within SQLAlchemy will
# do the translations required to map objects created from these classes into
# rows in the proper database tables
from app import routes, models