import nep

def callback(msg):
    print ("Callback get")
    print (msg)

msg_type = "string"           # Message type to listen.

node = nep.node("subscriber_sample","ROS2")      # Create a new node

# Listen info inside a event loop
sub = node.new_callback("pub_sub_test", msg_type , callback)

node.spin()




