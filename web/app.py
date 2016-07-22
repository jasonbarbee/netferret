# app.py

from flask import Flask
from flask import request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)

from models import *

def get_device_type_id_by_name(model, device_type):
    device_type_id = model.query.filter_by(device_type=device_type).first().id
    return device_type_id

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        device_name = request.form['device_name']
        device_address = request.form['device_address']
        device_type_id = get_device_type_id_by_name(DeviceTypes, request.form['device_type'])
        device = Inventory(device_name, device_address, device_type_id)
        db.session.add(device)
        db.session.commit()
        return redirect(url_for('index')) # redirect to prevent POSTDATA error on refresh

    devices = Inventory.query.order_by(Inventory.name).all()
    device_types = DeviceTypes.query.order_by(DeviceTypes.device_type.desc()).all()
    return render_template('index.html', inventory=devices, device_types=device_types)

if __name__ == '__main__':
    app.run()
