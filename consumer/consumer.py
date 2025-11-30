#Import necessary libraries
import json
import boto3 # to deal with s3 bucket(minio)
import time
from kafka import KafkaConsumer

#minio connection
s3 = boto3.client(
    's3',
    endpoint_url='http://localhost:9002',
    aws_access_key_id = 'admin',
    aws_secret_access_key = 'password123'
)  

bucket_name = 'bronzetransactions'

# Initialize Kafka Consumer
consumer = KafkaConsumer(
    'stock_quotes',
    bootstrap_servers = ['host.docker.internal:29092'],
    enable_auto_commit = True,
    auto_offset_reset = 'earliest',
    group_id = 'bronze-consumer',
    value_deserializer = lambda x: json.loads(x.decode('utf-8'))
)

print("Consumer is listening to the topic 'stock_quotes'...")

#main function to consume messages and store in minio
for message in consumer:
    record = message.value
    symbol = record.get('symbol')
    ts = record.get('fetched_at', int(time.time()))
    key = f"{symbol}/{ts}.json"

    # Upload the record to minio as a json file
    s3.put_object(
        Bucket=bucket_name,
        Key=key,
        Body=json.dumps(record),
        ContentType='application/json'
    )   

    print(f"Stored record for {symbol} at {key} in bucket {bucket_name}")