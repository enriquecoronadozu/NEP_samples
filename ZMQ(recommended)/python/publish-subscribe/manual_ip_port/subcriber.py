import nep

sub_type = "normal"                 # Type of subscriber. "callback" or "normal"
msg_type = "json"                   # Message type to listen. "string" or "dict"

node = nep.node("subscriber_sample")                                                        # Create a new node
conf = node.direct(ip = "127.0.0.1", port =  3000, mode ="one2many")                         # Select the configuration of the subscriber

def callback(msg):
    print ("Callback get")
    print (msg)

if sub_type == "normal":            # Listen info inside a while loop
    sub = node.new_sub("test_subcriber", msg_type, conf) 
    while True:
        s, msg = sub.listen()       # Non blocking socket
        if s:                       # Info avaliable only if s == True
            print(msg)

elif sub_type == "callback":        # Listen info inside a event loop

    sub = node.new_callback("test_subcriber", msg_type , callback, conf)
    node.spin()

    pass


