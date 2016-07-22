# models.py

import datetime
from app import db

class Inventory(db.Model):

    __tablename__ = 'inventory'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    address = db.Column(db.String,unique=True)
    device_type_id = db.Column(db.Integer, db.ForeignKey('device_types.id'))
    date_added = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, address, device_type_id):
        self.name = name
        self.address = address
        self.device_type_id = device_type_id
        self.date_added = datetime.datetime.now()

class DeviceTypes(db.Model):

    __tablename__ = 'device_types'

    id = db.Column(db.Integer, primary_key=True)
    device_type = db.Column(db.String, nullable=False)

    def __init__(self, device_type):
        self.device_type = device_type
