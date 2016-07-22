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
with open('device_types.yml') as file:
	device_type_list = load(file, Loader=Loader)

# Add device types to the database
for device_type in device_type_list:
	add_if_new(db.session, DeviceTypes, device_type=device_type)
