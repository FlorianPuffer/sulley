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
s_initialize("le_read_req_003c")

s_static("\x02")                                                                          #HCI ACL Type
s_static("\x48\x20")                                                                      #Create connection opcode

s_size("l2cap", length=2)                                                         #Parameter total length Length

if s_block_start("l2cap"):
    #L2CAP
    s_static("\x03\x00")                                                                      #L2CAP payload length
    s_static("\x04\x00")                                                                      #CID: Attribute Protocol

    #Bluetooth Attribute Prtocol
    s_byte("\x0a")                                                             #Opcode
    s_word("\x3c\x00", fuzzable= True)                                                                      #Starting Handle: 0x0001
s_block_end()


########################################################################################################################


########################################################################################################################
s_initialize("le_handle_value_notification")

s_static("\x02")                                                                          #HCI ACL Type
s_static("\x48\x20", name="connection_handler_id")                                                                      #Create connection opcode

s_size("l2cap", length=2)                                                         #Parameter total length Length

if s_block_start("l2cap"):
    #L2CAP
    s_word("\x01\x00", fuzzable= False)                                                       #L2CAP payload length
    s_static("\x04\x00")                                                                      #CID: Attribute Protocol

    #Bluetooth Attribute Prtocol
    s_byte([0x02, 0x03, 0x04, 0x05], fuzzable= True)                                                          #Opcode (x1b)
    s_word("\x3c\x00", fuzzable= False)                                                            #Starting Handle: 0x0001
    s_static("\x61\x61\x61\x61")
s_block_end()


########################################################################################################################

########################################################################################################################
s_initialize("le_read_by_groupe_Type_response_LintLength2")

s_static("\x02")                                                                # HCI ACL Type
s_static("\x48\x00")                                                            # Connection Handle

s_size("l2cap", length=2)                                                       # Data total length Length

if s_block_start("l2cap"):
    #L2CAP
    s_static("\x0E\x00")                                                        # L2CAP payload length
    s_static("\x04\x00")                                                        # CID: Attribute Protocol

    #Bluetooth Attribute Prtocol
    s_byte([0x11])                                                              # Opcode: Read by Group type reponse
    s_byte("\x06", fuzzable= False)                                             # Length
    #Bluetooth attribute Data
    s_word("\x01\x00", fuzzable=False)                                          # Generic Attribute Profile
    s_word("\x05\x00", fuzzable=False)                                          # Group End Handle
    s_word("\x01\x18", fuzzable=False)                                          # UUID: Generic Attribute Profile
    # Bluetooth attribute Data
    s_word("\x14\x00", fuzzable=False)                                          # Generic Access Profile
    s_word("\xFF\xFF", fuzzable=False)                                          # Group End Handle
    s_word("\x00\x18", fuzzable=False)                                          # UUID: Generic Access Profile
s_block_end()


########################################################################################################################

########################################################################################################################
s_initialize("le_read_by_type_response_Attribute_List_length_1")

s_static("\x02")                                                                # HCI ACL Type
s_static("\x48\x00")                                                            # Connection Handle

s_size("l2cap", length=2)                                                       # Data total length Length

if s_block_start("l2cap"):
    #L2CAP
    s_static("\x09\x00")                                                        # L2CAP payload length
    s_static("\x04\x00")                                                        # CID: Attribute Protocol

    #Bluetooth Attribute Prtocol
    s_byte([0x09])                                                              # Opcode: Read by Group type reponse
    s_byte("\x07", fuzzable= False)                                             # Length
    #Attribute Data
    s_word("\x02\x00", fuzzable=False)                                          # Handle
    s_byte("\x20", fuzzable=False)                                              # Characteristic Properties
    s_word("\x03\x00", fuzzable=False)                                          # Charaterisitic Value Handle
    s_word("\x05\x2A", fuzzable=False)                                          # UUID: Service changed

s_block_end()


########################################################################################################################

########################################################################################################################
s_initialize("le_send_error_response_Attribute_not_found_Handle_0x0001")

s_static("\x02")                                                                # HCI ACL Type
s_static("\x48\x00")                                                            # Connection Handle

s_size("l2cap", length=2)                                                       # Data total length Length

if s_block_start("l2cap"):
    #L2CAP
    s_static("\x05\x00")                                                        # L2CAP payload length
    s_static("\x04\x00")                                                        # CID: Attribute Protocol

    #Bluetooth Attribute Prtocol
    s_byte([0x01])                                                              # Opcode: Error Response
    s_byte("\x08", fuzzable= False)                                             # Request Opcode in Error:Read by Type Request
    s_word("\xFF\xFF", fuzzable=False, name = "handle_id")                                          # Handle in Error: 0x0001
    s_byte("\x0A", fuzzable=False)                                              # Error Code: Attribute not found

s_block_end()


########################################################################################################################

########################################################################################################################
s_initialize("le_send_error_response_Attribute_not_found_Handle_0x0003")

s_static("\x02")                                                                # HCI ACL Type
s_static("\x48\x00")                                                            # Connection Handle

s_size("l2cap", length=2)                                                       # Data total length Length

if s_block_start("l2cap"):
    #L2CAP
    s_static("\x05\x00")                                                        # L2CAP payload length
    s_static("\x04\x00")                                                        # CID: Attribute Protocol

    #Bluetooth Attribute Prtocol
    s_byte([0x01])                                                              # Opcode: Error Response
    s_byte("\x08", fuzzable= False)                                             # Request Opcode in Error:Read by Type Request
    s_word("\x03\x00", fuzzable=False, name = "handle_id")                                          # Handle in Error: 0x0001
    s_byte("\x0A", fuzzable=False)                                              # Error Code: Attribute not found

s_block_end()


########################################################################################################################

########################################################################################################################
s_initialize("le_send_error_response_Attribute_not_found_Handle_0x0004")

s_static("\x02")                                                                # HCI ACL Type
s_static("\x48\x00")                                                            # Connection Handle

s_size("l2cap", length=2)                                                       # Data total length Length

if s_block_start("l2cap"):
    #L2CAP
    s_static("\x05\x00")                                                        # L2CAP payload length
    s_static("\x04\x00")                                                        # CID: Attribute Protocol

    #Bluetooth Attribute Prtocol
    s_byte([0x01])                                                              # Opcode: Error Response
    s_byte("\x04", fuzzable= False)                                             # Request Opcode in Error: Find Information Request
    s_word("\x04\x00", fuzzable=False, name = "handle_id")                      # Handle in Error: 0x0001
    s_byte("\x0A", fuzzable=False)                                              # Error Code: Attribute not found

s_block_end()


########################################################################################################################

########################################################################################################################
s_initialize("le_send_error_response_Attribute_not_found_Handle_0x0014")

s_static("\x02")                                                                # HCI ACL Type
s_static("\x48\x00")                                                            # Connection Handle

s_size("l2cap", length=2)                                                       # Data total length Length

if s_block_start("l2cap"):
    #L2CAP
    s_static("\x05\x00")                                                        # L2CAP payload length
    s_static("\x04\x00")                                                        # CID: Attribute Protocol

    #Bluetooth Attribute Prtocol
    s_byte([0x01])                                                              # Opcode: Error Response
    s_byte("\x04", fuzzable= False)                                             # Request Opcode in Error: Find Information Request
    s_word("\x04\x00", fuzzable=False, name = "handle_id")                      # Handle in Error: 0x0001
    s_byte("\x0A", fuzzable=False)                                              # Error Code: Attribute not found

s_block_end()


########################################################################################################################

########################################################################################################################
s_initialize("le_sent_Connection_Parameter_Update_Response")

s_static("\x02")                                                                # HCI ACL Type
s_static("\x48\x00", name="connection_handler_id")                                                            # Connection Handle

s_size("l2cap", length=2)                                                       # Data total length Length

if s_block_start("l2cap"):
    #L2CAP
    s_static("\x06\x00")                                                        # L2CAP payload length
    s_static("\x05\x00")                                                        # CID: Conenction Parameter Update Response

    #Connection Paramter Update Response
    s_byte([0x13])                                                              # Command Code: Connection Paramter Update Response
    s_byte("\x02", fuzzable= False)                                             # Command Identifier
    s_word("\x02\x00", fuzzable=False, name = "Command Length")                      # Handle in Error: 0x0001
    s_word("\x00\x00", fuzzable=False, name = "Move Result")                                              # Error Code: Attribute not found

s_block_end()


########################################################################################################################


########################################################################################################################
s_initialize("le_write_nxp_qpps")

s_static("\x02")                                                                # HCI ACL Type
s_static("\x48\x00", name="connection_handler_id")                              # Connection Handle

s_size("l2cap", length=2)                                                       # Data total length Length

if s_block_start("l2cap"):
    #L2CAP
    s_size("attribute_protocol", length=2)                                      # L2CAP payload length
    s_static("\x04\x00")                                                        # CID: Attribute Protocol

    if s_block_start("attribute_protocol"):
        #Connection Paramter Update Response
        s_byte([0x12])                                                              # Command Code: Write Request
        s_word("\x12\x00", fuzzable=False, name = "Handle")
        if s_block_start("data"):
            s_byte([0x41], fuzzable=False)
        s_block_end("data")
        s_repeat("data", min_reps=100, max_reps=1000, step=1)
    s_block_end("attribute_protocol")
s_block_end()


########################################################################################################################

########################################################################################################################
s_initialize("le_write_nxp_qpps_bug_trigger")

s_static("\x02")                                                                # HCI ACL Type
s_static("\x48\x00", name="connection_handler_id")                              # Connection Handle

s_size("l2cap", length=2)                                                       # Data total length Length

if s_block_start("l2cap"):
    #L2CAP
    s_size("attribute_protocol", length=2)                                      # L2CAP payload length
    s_static("\x04\x00")                                                        # CID: Attribute Protocol

    if s_block_start("attribute_protocol"):
        #Connection Paramter Update Response
        s_byte([0x12])                                                              # Command Code: Write Request
        s_word("\x12\x00", fuzzable=False, name = "Handle")
        if s_block_start("data"):
            s_byte([0x41], fuzzable=False)
            s_byte([0x41], fuzzable=False)
            s_byte([0x41], fuzzable=False)
            s_byte([0x41], fuzzable=False)
            s_byte([0x41], fuzzable=False)
            s_byte([0x41], fuzzable=False)
            s_byte([0x41], fuzzable=False)
            s_byte([0x41], fuzzable=False)
            s_byte([0x41], fuzzable=False)
            s_byte([0x41], fuzzable=False)

            s_byte([0x42], fuzzable=False)
            s_byte([0x42], fuzzable=False)
            s_byte([0x42], fuzzable=False)
            s_byte([0x42], fuzzable=False)
            s_byte([0x42], fuzzable=False)

            s_byte([0x43], fuzzable=False)
            s_byte([0x43], fuzzable=False)
            s_byte([0x43], fuzzable=False)
            s_byte([0x43], fuzzable=False)
            s_byte([0x43], fuzzable=False)
        s_block_end("data")
        #s_repeat("data", min_reps=6, max_reps=6, step=1)
    s_block_end("attribute_protocol")
s_block_end()


########################################################################################################################