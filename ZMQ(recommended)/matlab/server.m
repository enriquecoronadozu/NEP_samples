import nep.server;

% -------------- Define server -----------
try
    server = nep.server("127.0.0.1", 8000);
catch
    server.close();
    server = nep.server("127.0.0.1", 8000);
end


% Define a function that will be executed when Ctrl+C is pressed
finishup = onCleanup(@() myCleanupFun(server));

while 1
        % ---------------- Request -----------------
        % Get request
        requestData = nep_server.listen_string(); % This function is in blocking mode
        % Tranform byte response to struct
        request = jsondecode(string(requestData))
      

        % ------------- Response ----------------------
        % Transform struct to json
        msg = struct('message','server response','value',0) 
        json_msg = jsonencode(msg)
        % Send json response
        nep_server.send_info(json_msg);
end


% ---------------- Close server -----------------
function myCleanupFun(f)
f.close()
close(f)
disp('Socket closed')
end

    
