import nep  # Import nep library
server = nep.server('127.0.0.1', 8000) #Create a new server instance

while True:
    msg = {"message":"hello"} # Message to send as response
    request = server.listen_info() # Wait for client request
    server.send_info(msg) # Send server response
    print (request) 
