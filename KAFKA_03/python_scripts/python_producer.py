from kafka import KafkaProducer
from random import random
import json


topic = 'kafka-test'
producer = KafkaProducer(
    bootstrap_servers='kafka:9093',
)


def publish_messages(limit):
    for i in range(limit):
        data = {
            'title': 'test_title',
            'director': 'Bennett Miller',
            'year': '2011',
            'rating': random(),
        }
        producer.send(topic, json.dumps(data).encode('utf-8'))

publish_messages(5)