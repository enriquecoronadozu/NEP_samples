import nep
import time
import sys

msg_type = "json"         # Message type to listen. "string" or "json"

node = nep.node("publisher_sample", "nanomsg")             # Create a new node
conf = node.broker(mode = "one2many")           # Select the configuration of the publisher
pub = node.new_pub("pub_sub_test_nn",msg_type,conf)        # Set the topic and the configuration of the publisher

# Publish a message each second
while True: 
    #  --- String example ---
    if msg_type == "string":
        msg = "hello world"
        print ("sending: " + msg)
        pub.publish(msg) 
        time.sleep(1)
    # --- JSON example ---
    if msg_type == "json":
        msg =  data = {"node":"perception", "primitive":"speech", "input":"add", "robot":"pepper", "parameters":"0"}
        print ("sending: " + str(msg))
        pub.publish(msg) 
        time.sleep(1)
