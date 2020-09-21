from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
 
migrate = Migrate()
db = SQLAlchemy()
_session = db.session

def save(model: db.Model):
    _session.add(model)
    commit()
    return model

def commit():
    _session.commit()