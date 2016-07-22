# Overview
Network discovery and inventory tool

# Launch

## Docker

- docker-compose up -d
- docker-compose run web python /usr/src/app/create_db.py

## Local Development

- Create and activate a python virtual environment
- Load required python modules with pip install -r requirements.txt
- Create .env_local with the required settings
- Source .env_local to set environmental variables
- Setup PostgreSQL with DB matching the .env_local settings
- Initialize the database by running python ./web/create_db.py
- Start the app from the ./web/ folder with python app.py