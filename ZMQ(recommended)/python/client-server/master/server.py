import nep  # Import nep library
node = nep.node("server_test")
server = node.new_server("client_server_sample")

while True:
    msg = {"message":"hello"} # Message to send as response
    request = server.listen_info() # Wait for client request
    server.send_info(msg) # Send server response
    print (request) 
