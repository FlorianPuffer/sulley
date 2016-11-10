
from sulley   import *
import btsocket as bt
from requests import bluetooth


def do_fuzz ():
    sess   = sessions.session(proto="bluetooth")
    target = sessions.target('4BEE7037B840', 6666)

    sess.add_target(target)
    sess.connect(s_get("1234"))

    sess.fuzz()


    print "fuzzing done"



do_fuzz()