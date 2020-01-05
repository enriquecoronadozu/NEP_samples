import nep 
import time 

node = nep.node("client_test")
client = node.new_client("client_server_sample")


while True:
    msg = {"message":"client request"} # Message to send as request
    client.send_info(msg)   # Send request
    print (client.listen_info()) # Wait for server response
    time.sleep(1) # Wait one second
