% --------------- Looad libraries ----------
 base_path = "C:/nep-matlab";
 javaaddpath ([base_path, "/nep.jar"]);
 javaaddpath ([base_path, "/jeromq-0.4.3.jar"]);
 javaaddpath ([base_path, "/gson-2.8.4.jar"]);
 addpath('jsonlab');
 
% ---------------- New node ----------------
node = javaObject ("nep.Node", "octave_node")

% ------------ Define subscriber -----------
sub = node.new_sub("test");

% --------------- Read data ---------------
%listen 10 samples
for c = 1:5
   msg = sub.listen(); % listen data 
   if strcmp(msg,"{}")
     pause(.001)  
   else
         try
           data=loadjson(msg);
           data.message
         catch exception
         end 
   end
 
   pause(1)
end


