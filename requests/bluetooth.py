import logging

from sulley import *


def _toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0' + hv
        lst.append(hv)
    return reduce(lambda x, y: x + y, lst)


def rpc_request_encoder (data):
    return data

########################################################################################################################
s_initialize("1234")
s_block_start("connect", encoder=rpc_request_encoder)

s_static("\x01")                                                                          #HCI command opcode
s_static("\x05\x04")                                                                      #Create connection opcode

#s_static("\x0D")
#s_byte([0, 1, 2], name = "paramter_length")
s_byte(13, fuzzable=True, full_range=True , name="parameter_length")                          #Parameter total length Length
s_static("\x4B\xEE\x70\x37\xB8\x40")                                                      #MAC adress of the target
s_static("\x18\xCC")                                                                      #Packet type

s_static("\x01")                                                                          #Page scan repetition
s_static("\x00")                                                                          #Page scan mode (Mandatory Page scan mode -> 0x00)

s_static("\x48\x38")                                                                      #Clock offset

s_static("\x01")                                                                            #Allow role switch (Master/Slave)

s_block_end()



########################################################################################################################


