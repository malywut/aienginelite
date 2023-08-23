import time
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pika

app = FastAPI()

class PredictionInput(BaseModel):
    data: str

@app.post("/predict")
def predict_endpoint(payload: PredictionInput):
    input_data = payload.data
    
    # Connect to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()

    # Declare the prediction queue and response queue
    channel.queue_declare(queue='prediction_queue')
    channel.queue_declare(queue='response_queue')

    # Push input_data to the prediction queue
    channel.basic_publish(exchange='', routing_key='prediction_queue', body=input_data)

    # Poll the response queue for a response
    max_poll_attempts = 10  # Number of attempts before giving up
    poll_interval = 1  # Interval in seconds between poll attempts
    for _ in range(max_poll_attempts):
        method_frame, header_frame, body = channel.basic_get(queue='response_queue')
        if method_frame:
            prediction_result = body.decode('utf-8')
            channel.basic_ack(method_frame.delivery_tag)
            connection.close()
            return {"prediction": prediction_result}
        time.sleep(poll_interval)

    connection.close()
    return {"prediction": "No response available"}
