import json
import asyncio 
from azure.servicebus.aio import ServiceBusClient 
from azure.servicebus  import ServiceBusMessage

payload = { "id": 123, "name": "John Doe", "age": 30, "email": "johndoe@example.com"}

NAMESPACE_CONNECTION_STR = "Endpoint=sb://zedisb.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey="
QUEUE_NAME = "zediq"

async def send_single_message(sender):
    # Create a Service Bus message and send it to the queue
    message = ServiceBusMessage(json.dumps(payload), content_type='application/json') 
    await sender.send_messages(message) 
    print("Sent a single message") 

async def run():
    # create a Service Bus client using the connection string
    async with ServiceBusClient.from_connection_string( conn_str=NAMESPACE_CONNECTION_STR, logging_enable=True) as servicebus_client:
        # Get a Queue Sender object to send messages to the queue
        sender = servicebus_client.get_queue_sender(queue_name=QUEUE_NAME) 
        async with sender:
            # Send one message
            await send_single_message(sender)
            
asyncio.run(run()) 
print("Done sending messages")
print("-----------------------")