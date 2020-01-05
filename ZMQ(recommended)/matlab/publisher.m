import nep.node;

% ---------------- New node ---------------
node = nep.node("matlab");

% ------------ Define publisher -----------
% Direct
%pub = node.new_sub("pub_sub_test", "127.0.0.1", 9090,"one2many");
% Using master
pub = node.new_pub("pub_sub_test");

% Define a function that will be executed when Ctrl+C is pressed
finishup = onCleanup(@() myCleanupFun(sub));

% --------------- Send data ---------------

msg = struct('message','hello') % Messages defined as structures
json_msg = jsonencode(msg) % Convert matlab structures to JSON

for c = 1:5
   pub.publish(json_msg) 
   pause(.01)  
end

% ---------------- Close publisher -----------------
pub.close()  % the subscriber must to be closed.

function myCleanupFun(f)
f.close()
close(f)
disp('Socket closed')
end