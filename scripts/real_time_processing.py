# scripts/real_time_processing.py
from kafka import KafkaConsumer

def real_time_processing():
    consumer = KafkaConsumer('recommendations', bootstrap_servers=['localhost:9092'])
    for message in consumer:
        # Process real-time data
        print(message.value)

if __name__ == "__main__":
    real_time_processing()
    print("Real-time processing started!")
