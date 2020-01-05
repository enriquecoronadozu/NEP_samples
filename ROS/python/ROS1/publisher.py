import nep
import time
import sys

msg_type = "string"         # Message type to listen. 

node = nep.node("publisher_sample","ROS")               # Create a new node
pub = node.new_pub("pub_sub_test",msg_type)        # Set the topic and the configuration of the publisher

# Publish a message each second
while True: 
	msg = "hello world"
        print ("sending: " + msg)
        pub.publish(msg) 
        time.sleep(1)
 
