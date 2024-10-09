#!/usr/bin/env bash

# Export the Google Cloud credentials and Airflow connection variables
export GOOGLE_APPLICATION_CREDENTIALS=${GOOGLE_APPLICATION_CREDENTIALS}

# Upgrade the Airflow database
airflow db upgrade

# Create the default Airflow admin user
airflow users create \
    -r Admin \
    -u admin \
    -p admin \
    -e admin@example.com \
    -f admin \
    -l airflow

# Start the Airflow webserver
airflow webserver

