from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.session import Session

db = SQLAlchemy()
session: Session = db.session
