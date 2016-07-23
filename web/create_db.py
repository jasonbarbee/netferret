# create_db.py

from app import db
from yaml import load, dump, CLoader as Loader, CDumper as Dumper
from models import *

# Create the database schema
db.create_all()

# Add row if a match is not already present
def add_if_new(session, model, **kwargs):
	instance = session.query(model).filter_by(**kwargs).first()
	if not instance:
		instance = model(**kwargs)
		session.add(instance)
		session.commit()

# Open the yaml file containing the default device types
with open('data_defaults.yaml') as file:
	data_defaults = load(file, Loader=Loader)

# Add device types to the database
for item in data_defaults['device_types']:
	add_if_new(db.session, DeviceTypes, device_type=item)

# Add connection methods to the database
for item in data_defaults['connect_methods']:
	add_if_new(db.session, ConnectMethods, connect_method=item)
