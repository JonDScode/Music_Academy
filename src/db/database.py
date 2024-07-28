import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv



# Cargar variables de entorno
load_dotenv()

db = SQLAlchemy()
Base = declarative_base()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)


    from src.models import models 
    
    with app.app_context():
        Base.metadata.create_all(db.engine)