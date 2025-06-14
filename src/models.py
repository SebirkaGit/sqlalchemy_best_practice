from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
import sys
import os

# Add the current script's directory to Python's search path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Base class for all our SQLAlchemy models
Base = declarative_base()

class Contact(Base):
    # Name of the table in the database
    __tablename__ = 'contacts'

    # Columns in the contacts table:
    id = Column(Integer, primary_key=True, autoincrement=True)  
    # 'id' is the primary key, auto-incremented integer

    name = Column(String(100), nullable=False)  
    # 'name' column: string up to 100 chars, required (not nullable)

    email = Column(String(100), nullable=False, unique=True)  
    # 'email' column: string up to 100 chars, required and unique

    phone = Column(String(20), nullable=True)  
    # 'phone' column: optional string up to 20 chars

    def __repr__(self):
        # String representation to easily inspect Contact objects
        return f"<Contact(name='{self.name}', email='{self.email}', phone='{self.phone}')>"
