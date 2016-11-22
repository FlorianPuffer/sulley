import struct
import time
import os
import bluetooth._bluetooth as bluez
import bluetooth as pybluez

from sulley   import *
from requests import bluetooth

serial_id_device = "XXXXXXXXXX"                                                #define Android ID for adb debugging here

def _toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0' + hv
        lst.append(hv)
    return reduce(lambda x, y: x + y, lst)

def search_device(sess, target_name):

    sess.bluetoothSocket.send("\x01\x0c\x20\x02\x01\x00")                           #Enable LE scan

    results = []
    done = False
    while not done:
        pkt = sess.bluetoothSocket.recv(255)
        ptype, event, plen = struct.unpack("BBB", pkt[:3])
        if event == 62:
            pkt = pkt[3:]
            nrsp = pybluez.get_byte(pkt[0])
            for i in range(nrsp):
                addr = bluez.ba2str(pkt[4 + 6 * i:4 + 6 * i + 6])
                if target_name in pkt:
                    print(" %s found with mac %s" %(target_name,addr))
                    sess.bluetoothSocket.send("\x01\x0c\x20\x02\x00\x00")           #Disable LE scan
                    done = True
                    time.sleep(2)
                    return pkt[4 + 6 * i:4 + 6 * i + 6]                             #Return as hex
                results.append((addr, -1))
                print("[%s] (no RRSI)" % addr)

        else:
            print("unrecognized packet type 0x%02x" % ptype)
        #print("event ", event)


def connect_to_device(sess, target_mac):
    # Setup before fuzzing session
    sess.bluetoothSocket.send(
        "\x01\x0d\x20\x19\x60\x00\x30\x00\x00\x01" + target_mac + "\x00\x18\x00\x28\x00\x00\x00\xbc\x02\x00\x00\x00\x00")

    done = False
    # TODO refactor HCI event handler
    while not done:
        pkt = sess.bluetoothSocket.recv(512)
        ptype, event, plen = struct.unpack("BBB", pkt[:3])
        if (ptype == 0x04):
            if event == 0x3E:
                print("EVT_LE_META Connection complete")
                done=True
            else:
                print("unhandled Event")

    time.sleep(3)

def bt_service_is_alive():

    #android platform tools path
    platform_tools_path="/home/student/Desktop/android-sdk-linux/platform-tools"

    #check that the target processes still alive
    _, stdout = os.popen2(platform_tools_path + '/adb -s ' + serial_id_device +' shell pgrep /system/bin/brcm-uim-sysfs')
    pid = stdout.read()
    if pid == '':
        return ''

    _, stdout = os.popen2(platform_tools_path + '/adb -s ' + serial_id_device +' shell pgrep com.android.bluetooth')
    pid = stdout.read()
    if pid == '':
        return ''

    _, stdout = os.popen2(platform_tools_path + '/adb -s ' + serial_id_device +' shell pgrep system_server')
    pid = stdout.read()
    if pid == '':
        return ''

    return pid

def bt_service_restart():
    '''Restart the target. Called when instrumentation (post) fail.'''
    print ("BLUETOOTH SERVICE CRASH!!!!!!!!!!")
    #os.popen2('ssh %s /etc/init.d/target restart' % IP_DST)


def do_fuzz ():
    #setup monitoring
    sess   = sessions.session(proto="bluetooth")
    target = sessions.target("127.0.0.1", 0)
    #target.netmon = pedrpc.client("127.0.0.1", 26001)                                  #network monitor is not working due no support of bluetooth decoding in impackt module
    target.procmon = instrumentation.external(post=bt_service_is_alive, start=bt_service_restart)
    sess.add_target(target)

    #find and connect device
    target_name = "target"
    target_mac=search_device(sess, target_name)
    connect_to_device(sess, target_mac)

    #setup fuzzing
    sess.connect(s_get("le_test_block"))
    #sess.connect(s_get("le_read_by_group_type_request_1"))

    sess.fuzz()


    print "fuzzing done"



do_fuzz()

