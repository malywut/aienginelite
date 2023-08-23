import time
import pika
from wrapper import Wrapper

def main():
    # Connect to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))

    # Initialize the model
    wrapper = Wrapper()
    wrapper.initialize()

    channel = connection.channel()

    # Declare the prediction queue
    channel.queue_declare(queue='prediction_queue')

    while True:
        # Consume input data from the prediction queue
        method_frame, header_frame, body = channel.basic_get(queue='prediction_queue')
        if method_frame:
            input_data = body.decode('utf-8')

            # Model prediction
            prediction_result = wrapper.predict(input_data)
            print(f'Model prediction : {prediction_result}')
            # Push the prediction result to the response queue
            channel.queue_declare(queue='response_queue')
            channel.basic_publish(exchange='', routing_key='response_queue', body=prediction_result)

            print(f"Traité : '{input_data}', Résultat : '{prediction_result}'")
            channel.basic_ack(method_frame.delivery_tag)
        else:
            time.sleep(1)  # Wait if there's no data in the queue

if __name__ == "__main__":
    main()
