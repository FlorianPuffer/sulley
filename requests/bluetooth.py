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
s_initialize("brd_connect")
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


########################################################################################################################
s_initialize("ble_connect")
s_block_start("connect", encoder=rpc_request_encoder)

s_static("\x01")                                                                          #HCI command opcode
s_static("\x20\x0D")                                                                      #Create connection opcode

s_static("\x19")                                                                          #Parameter total length Length
s_static("\x60\x00")                                                                      #Scan Interval
s_static("\x30\x00")                                                                      #Scan Window
s_static("\x00")                                                                          #Initiator Filter Policy
s_static("\x01")                                                                          #Peer Address Type: Random Device Adress
s_static("\xAE\x74\x78\xA7\xD0\x64")                                                      #MAC adress of the target

s_static("\x18\x00")                                                                      #Connection Interval Min
s_static("\x28\x00")                                                                      #Connection Interval Miax
s_static("\x00\x00")                                                                      #Connection Latency
s_static("\xBC\x02")                                                                      #Supervision Timeout

s_static("\x00\x00")                                                                      #Min CE length
s_static("\x00\x00")                                                                      #Max CE length



s_block_end()

########################################################################################################################

########################################################################################################################
s_initialize("le_read_remote_used_features")
s_block_start("read", encoder=rpc_request_encoder)

s_static("\x01")                                                                          #HCI command opcode
s_static("\x16\x20")                                                                      #Create connection opcode

s_static("\x02")                                                                          #Parameter total length Length
s_static("\x40\x00")                                                                      #Connection Handle


s_block_end()

########################################################################################################################


########################################################################################################################
s_initialize("le_read_by_group_type_request_1")
s_block_start("read", encoder=rpc_request_encoder)

s_static("\x02")                                                                          #HCI ACL Type
s_static("\x40\x20")                                                                      #Create connection opcode

s_static("\x0B\x00")                                                                      #Parameter total length Length

#L2CAP
s_static("\x07\x00")                                                                      #L2CAP payload length
s_static("\x04\x00")                                                                      #CID: Attribute Protocol

#Bluetooth Attribute Prtocol
s_static("\x10")                                                                          #Opcode
s_static("\x01\x00")                                                                      #Starting Handle: 0x0001
s_static("\xff\xff")                                                                      #Ending Handle: 0xFFFF
s_static("\x00\x28")                                                                      #UUID: GATT Primary Service Declaration


s_block_end()

########################################################################################################################

########################################################################################################################
s_initialize("le_read_by_group_type_request_30")
s_block_start("read", encoder=rpc_request_encoder)

s_static("\x02")                                                                          #HCI ACL Type
s_static("\x40\x20")                                                                      #Create connection opcode

s_static("\x0B\x00")                                                                      #Parameter total length Length
s_static("\x40\x00")                                                                      #Connection Handle

#L2CAP
s_static("\x07\x00")                                                                      #L2CAP payload length
s_static("\x04\x00")                                                                      #CID: Attribute Protocol

#Bluetooth Attribute Prtocol
s_static("\x10")                                                                          #Opcode
s_static("\x30\x00")                                                                      #Starting Handle: 0x0001
s_static("\xff\xff")                                                                      #Ending Handle: 0xFFFF
s_static("\x00\x28")                                                                      #UUID: GATT Primary Service Declaration


s_block_end()

########################################################################################################################


########################################################################################################################
s_initialize("le_read_by_group_type_request_list2")
s_block_start("read", encoder=rpc_request_encoder)

s_static("\x02")                                                                          #HCI ACL Type
s_static("\x40\x20")                                                                      #Create connection opcode

s_static("\x12\x00")                                                                      #Parameter total length Length

#L2CAP
s_static("\x0E\x00")                                                                      #L2CAP payload length
s_static("\x04\x00")                                                                      #CID: Attribute Protocol

#Bluetooth Attribute Prtocol
s_static("\x11")                                                                          #Opcode
s_static("\x06")                                                                          #Length of Attribute Data
s_static("\x01\x00")                                                                      #Handel: Generic Attribute Profile
s_static("\x05\x00")                                                                      #Group End Handle
s_static("\x01\x18")                                                                      #UUID: Generic Attrbute Profile

s_static("\x14\x00")                                                                      #Handel: Generic Attribute Profile
s_static("\xFF\xFF")                                                                      #Group End Handle
s_static("\x00\x18")                                                                      #UUID: Generic Attrbute Profile

s_block_end()

########################################################################################################################









########################################################################################################################
s_initialize("le_sent_connection_parameter_update")
s_block_start("read", encoder=rpc_request_encoder)

s_static("\x02")                                                                          #HCI ACL Type
s_static("\x40\x20")                                                                      #Create connection opcode

s_static("\x0A\x00")                                                                      #Parameter total length Length

#L2CAP
s_static("\x06\x00")                                                                      #L2CAP payload length
s_static("\x05\x00")                                                                      #CID: LOW Energy L2CAP Signaling Channel

#Connection Parameter update response
s_static("\x13")                                                                          #Command Code: Connection Paramter Update Response
s_static("\x02")                                                                          # Command identifier

s_static("\x02\x00")                                                                      #Command length
s_static("\x00\x00")                                                                      #Move Result: Accepted


s_block_end()

########################################################################################################################

########################################################################################################################
s_initialize("le_test_block")

s_static("\x02")                                                                          #HCI ACL Type
s_static("\x48\x20")                                                                      #Create connection opcode

s_size("ParamterLength", length=2)                                                         #Parameter total length Length

if s_block_start("ParamterLength"):
    #L2CAP
    s_static("\x07\x00")                                                                      #L2CAP payload length
    s_static("\x04\x00")                                                                      #CID: Attribute Protocol

    #Bluetooth Attribute Prtocol
    s_byte("\x10", fuzzable=True)                                                             #Opcode
    s_static("\x01\x00")                                                                      #Starting Handle: 0x0001
    s_static("\xff\xff")                                                                      #Ending Handle: 0xFFFF
    s_static("\x00\x28")                                                                      #UUID: GATT Primary Service Declaration
s_block_end()


########################################################################################################################