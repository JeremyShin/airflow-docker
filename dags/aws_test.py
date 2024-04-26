import boto3
import random
import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator

with DAG(
    dag_id="aws_test",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    def select_fruit():
        fruit = ['APPLE','BANANA','ORANGE','AVOCADO']
        rand_int = random.randint(0,3)
        print(fruit[rand_int])

    def aws_test():
        # Retrieve the list of existing buckets
        s3 = boto3.client('s3')
        response = s3.list_buckets()

        # Output the bucket names
        print('Existing buckets:')
        for bucket in response['Buckets']:
            print(f'  {bucket["Name"]}')

    py_t1 = PythonOperator(
        task_id='py_t1',
        python_callable=select_fruit
    )

    py_t2 = PythonOperator(
        task_id='py_t2',
        python_callable=aws_test
    )

    py_t1 >> py_t2

