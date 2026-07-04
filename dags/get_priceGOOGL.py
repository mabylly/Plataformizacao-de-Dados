from aiflow import DAG
from airflow.decorators import task
from datetime import datetime

with DAG(
    "get_price_GOOGL", 
    start_date=datetime(2026, 1, 1), 
    schedule_interval="@weekly", 
    catchup=False) as dag:

    @task
    def extract(stock):
        return stock

    @task
    def process(stock):
        return stock

    @task
    def send_email(stock):
        return stock

    send_email(process(extract(3324)))