import nep.client;

% -------------- Start client -----------
try
    nep_client = nep.client("127.0.0.1", 8000);
catch
    nep_client.close();
    nep_client = nep.client("127.0.0.1", 8000);
end

% Define a function that will be executed when Ctrl+C is pressed
finishup = onCleanup(@() myCleanupFun(nep_client));

% -------------- Request -----------
% Transform struct to json
msg = struct('msg','hello')
json_msg = jsonencode(msg)
% Send json request
nep_client.send(json_msg);

% -------------- Response -----------
% Get request
requestData = nep_client.listen_string() % This function is in blocking mode
% Tranform string response to struct
request = jsondecode(string(requestData))

% ---------------- Close client -----------------
function myCleanupFun(f)
f.close()
close(f)
disp('Socket closed')
end


    