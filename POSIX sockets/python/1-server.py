import nep  
import time

import nep  # Import nep library
server = nep.server('127.0.0.1', 30000, 'normal') # Create a new server instance

while True:
    msg = "server response"         # Message to send as response (string) 
    request = server.listen_info()  # Wait for client request
    print (request)
    server.send_info(msg)           # Send server response
