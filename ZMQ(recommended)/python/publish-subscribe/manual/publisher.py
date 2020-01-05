import nep
import time

node = nep.node('sender')
conf = node.direct(ip = '127.0.0.1', port =  3000, mode ='one2many')
pub = node.new_pub('test_subcriber','json',conf)

while True:
	# Here is your code ...
	msg = {'message':'hello'}	# An example of message
	pub.publish(msg)		# Send message
	time.sleep(.01)
