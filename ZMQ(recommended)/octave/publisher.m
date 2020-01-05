% --------------- Looad libraries ----------
 base_path = "C:/nep-matlab";
 javaaddpath ([base_path, "/nep.jar"]);
 javaaddpath ([base_path, "/jeromq-0.4.3.jar"]);
 javaaddpath ([base_path, "/gson-2.8.4.jar"]);
 addpath('jsonlab');
 
% ---------------- New node ----------------
node = javaObject ("nep.Node", "octave_node")

% ------------ Define subscriber -----------
pub = node.new_pub("test", "json");


for c = 1:5
   msg = struct('message','hello','value',c) %Messages to send as structures (python-like dictionaries)
   json_msg = savejson(msg)
   pub.publish(json_msg) 
   pause(1)  
end

% ---------------- Close publisher -----------------
pub.close()  % the subscriber must to be closed.

