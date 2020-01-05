import nep
import time

node = nep.node("surveyor_test")
resp = node.new_respondent('surveyor_sample');
i=0
while True:
    x = {"node":"sucess"}
    s, msg = resp.listen_json(block_mode=False)
    if s:
        i = i + 1
        if i%2 == 0:
            print i
        resp.send_json(x)
