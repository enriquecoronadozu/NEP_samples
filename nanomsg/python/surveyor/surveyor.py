import nep
import time

node = nep.node("surveyor_test")
sur = node.new_surveyor('surveyor_sample', timeout = 1000);
while True:
    x = {"node": "action"}
    print ("data to send:" + str(x))
    sur.send_json(x)
    s, msg = sur.listen_json()
    if s:
        print ("data read" + str(msg))
    else:
        print ("respondent not connected")
    time.sleep(1)
