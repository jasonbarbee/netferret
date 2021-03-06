# app.py

from flask import Flask
from flask import request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)

from models import *

# Query for id of a specific data row
def get_id_by_name(model, **kwargs):
    result = model.query.filter_by(**kwargs).first().id
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        device_name       = request.form['device_name']
        device_address    = request.form['device_address']
        device_type_id    = get_id_by_name(DeviceTypes, device_type=request.form['device_type'])
        connect_method_id = get_id_by_name(ConnectMethods, connect_method=request.form['connect_method'])
        device = Inventory(device_name, device_address, device_type_id, connect_method_id)
        db.session.add(device)
        db.session.commit()
        return redirect(url_for('index')) # redirect to prevent POSTDATA error on refresh

    devices = Inventory.query.order_by(Inventory.name).all()
    device_types = DeviceTypes.query.order_by(DeviceTypes.device_type.desc()).all()
    connect_methods = ConnectMethods.query.order_by(ConnectMethods.connect_method.desc()).all()
    return render_template('index.html', inventory=devices, device_types=device_types,
                           connect_methods=connect_methods)

if __name__ == '__main__':
    app.run()
