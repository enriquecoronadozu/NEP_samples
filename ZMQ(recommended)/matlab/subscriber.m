import nep.node;

% ---------------- New node ----------------
node = nep.node("matlab");

% ------------ Define subscriber -----------
% Direct
%sub = node.new_sub("pub_sub_test", "127.0.0.1", 9090,"one2many");
% Using master
sub = node.new_sub("pub_sub_test");

% Define a function that will be executed when Ctrl+C is pressed
finishup = onCleanup(@() myCleanupFun(sub));

% --------------- Read data ---------------
%listen 10 samples
for c = 1:5
   msg = sub.listen(); % listen data 
   if strcmp(msg,"{}")
     pause(.001)  
   else
         try
            value = jsondecode(string(msg))
         catch exception
         end 
   end
 
   pause(1)
end

% ---------------- Close subscriber ---------------

sub.close()  % the subscriber must to be closed.
function myCleanupFun(f)
f.close()
close(f)
disp('Socket closed')
end
