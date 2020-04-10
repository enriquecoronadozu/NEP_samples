import nep

def callback(msg):
    print ("Callback get")
    print (msg)

sub_type = "listen"             # Type of subscriber. "callback" or "listen"
msg_type = "json"               # Message type to red. "string" or "json"

node = nep.node("subscriber_sample")        # Create a new node

if sub_type == "listen":    # Listen info inside a while loop
    sub = node.new_sub("test", msg_type)    # Set the topic and the configuration of the subscriber
    while True:
        s, msg = sub.listen()    # Non blocking socket
        if s:                    # Info avaliable only if s == True
            print (msg)

elif sub_type == "callback":    # Listen info inside a event loop

    sub = node.new_callback("test", msg_type , callback)
    node.spin()

    pass


