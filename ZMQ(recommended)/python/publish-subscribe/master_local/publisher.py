import nep
import time
import sys

msg_type = "json"         # Message type to listen. "string" or "json"

node = nep.node("publisher_sample")             # Create a new node
pub = node.new_pub("test",msg_type)        # Set the topic and the configuration of the publisher

# Publish a message each second
i = 0
while True: 
    #  --- String example ---
    if msg_type == "string":
        msg = "hello world"
        print ("sending: " + msg)
        pub.publish(msg) 
        time.sleep(1)
    # --- JSON example ---
    if msg_type == "json":
        i = i + 1
        msg =  data = {"message":"hello"}
        print ("sending: " + str(msg))
        pub.publish(msg) 
        time.sleep(1)
