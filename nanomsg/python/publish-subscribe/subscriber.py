import nep

msg_type = "json"           # Message type to listen. "string" or "json"

node = nep.node("subscriber_sample", "nanomsg")                                # Create a new node
conf = node.broker(mode = "one2many")        # Select the configuration of the subscriber
sub = node.new_sub("pub_sub_test_nn", msg_type, conf)                  # Set the topic and the configuration of the subscriber

while True:
    s, msg = sub.listen()    # Non blocking socket
    if s:                    # Info avaliable only if s == True
        print (str(msg))



