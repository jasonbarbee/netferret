# models.py

import datetime
from app import db

class Inventory(db.Model):

    __tablename__ = 'inventory'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    address = db.Column(db.String,unique=True)
    device_type_id = db.Column(db.Integer, db.ForeignKey('device_types.id'))
    device_type = db.relationship('DeviceTypes', backref=db.backref('inventory', lazy='dynamic'))
    connect_method_id = db.Column(db.Integer, db.ForeignKey('connect_methods.id'))
    connect_method = db.relationship('ConnectMethods', backref=db.backref('inventory', lazy='dynamic'))
    date_added = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, address, device_type_id, connect_method_id):
        self.name = name
        self.address = address
        self.device_type_id = device_type_id
        self.connect_method_id = connect_method_id
        self.date_added = datetime.datetime.now()

class DeviceTypes(db.Model):

    __tablename__ = 'device_types'

    id = db.Column(db.Integer, primary_key=True)
    device_type = db.Column(db.String, nullable=False)

    def __init__(self, device_type):
        self.device_type = device_type

class ConnectMethods(db.Model):

    __tablename__ = 'connect_methods'

    id = db.Column(db.Integer, primary_key=True)
    connect_method = db.Column(db.String, nullable=False)

    def __init__(self, connect_method):
        self.connect_method = connect_method
