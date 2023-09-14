import sqlalchemy
from sqlalchemy import create_engine, Column, Text, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///database.db')
engine.connect()

Base = declarative_base()

class Clients(Base):
	__tablename__ = 'clients'
	client_number = Column(Integer, primary_key = True)
	firstname = Column(Text(20))
	surname = Column(Text(20))
	email = Column(Text(100))
	phone = Column(Text(20))

	def __init__(self, first, last, email, phone):
		self.firstname = first
		self.surname = last
		self.email = email
		self.phone = phone

	def __repr__(self):
		return f"Surname: {self.surname}, Firstname: {self.firstname}, Email: {self.email}, Number: {self.phone}"

class Loans(Base):
	__tablename__ = 'loans'

	client = relationship(Clients)

	def __repr__(self):
		return f""

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
