from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL')
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
