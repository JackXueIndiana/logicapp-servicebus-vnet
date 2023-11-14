# logicapp-servicebus-vnet
This is a sample project with logic app workflows, service bus queues and vm for testing. All are in a VNet.

WF1 triggered by message arraived at queue "q" and send the JSON content to "q1"
WF2 manuaaly run to send a JSON message to queue "q"

Python script send.py sends a JSON to queue "q"
Python script receiver.py receives all messages in queue "q1"

In the VNET there are three subnets for
service bus
logic app
bastin VM.
