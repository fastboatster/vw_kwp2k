import elm
import serial
import logging

# TODO test with elm dongle


def main():
    #     setup comport
    ser = serial.Serial(port='\\.\COM3',
                        baudrate=115200,
                        bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE)
    logging.basicConfig(filename='myapp.log')
    elm_instance = elm.Elm327(ser)
    elm_instance.initialize()
    # test if we can set up a communication channel with engine (mk5 jetta)
    resps = []
    elm_instance.SEND_cmd(b'atsh200')
    resps.append(elm_instance.RTRV_record())
    elm_instance.SEND_cmd(b'atcra201')
    resps.append(elm_instance.RTRV_record())
    elm_instance.SEND_cmd(b'01 c0 00 10 00 03 01 1')
    resps.append(elm_instance.RTRV_record())

    elm_instance.SEND_cmd(b'atsh740')
    resps.append(elm_instance.RTRV_record())
    elm_instance.SEND_cmd(b'atcra300')
    resps.append(elm_instance.RTRV_record())
    elm_instance.SEND_cmd(b'a0 0f 8a ff 32 ff')
    # elm_instance.SEND_cmd(b'a0 0f ff 32 ff')
    resps.append(elm_instance.RTRV_record())
    elm_instance.SEND_cmd(b'10 00 02 10 89')
    resps.append(elm_instance.RTRV_record())
    elm_instance.SEND_cmd(b'b1')
    resps.append(elm_instance.RTRV_record())



    pass

if __name__ == '__main__':
    main()