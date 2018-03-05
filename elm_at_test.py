import elm
import serial
import logging
import time

# TODO test with elm dongle


def main():
    # create file handler which logs even debug messages
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    # create a file handler
    handler = logging.FileHandler('debug.log')
    handler.setLevel(logging.DEBUG)

    # create a logging format
    formatter = logging.Formatter('%(asctime)s - %(relativeCreated)d - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(handler)

    # fh = logging.FileHandler('spam.log')
    # fh.setLevel(logging.DEBUG)
    # # create formatter and add it to the handlers
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # fh.setFormatter(formatter)
    # # add the handlers to logger
    # logger.addHandler(fh)
    logger.debug('Logger initialized')
    #     setup comport
    ser = serial.Serial(port='/dev/tty.OBDII-Port',
                        baudrate=115200,
                        bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        timeout=None)
    # logging.basicConfig(filename='myapp.log')
    elm_instance = elm.Elm327(ser, logger)
    elm_instance.initialize()
    # test if we can set up a communication channel with engine (mk5 jetta)
    resps = []
    elm_instance.SEND_cmd(b'atsh200')
    resps.append(elm_instance.RTRV_record())
    elm_instance.SEND_cmd(b'atcra202')
    resps.append(elm_instance.RTRV_record())
    elm_instance.SEND_cmd(b'02 c0 00 10 00 03 01 1')
    resps.append(elm_instance.RTRV_record(2))

    elm_instance.SEND_cmd(b'atsh760')
    resps.append(elm_instance.RTRV_record())
    elm_instance.SEND_cmd(b'atcra300')
    resps.append(elm_instance.RTRV_record())
    # maybe send b'a0 0f ca ff 32 ff' to set the timeout to 1 sec?
    # 8a - 100 msecs timeout, 32 - 50 msec between packets, 4A - 10 msecs
    # elm_instance.SEND_cmd(b'a0 0f 8a ff 32 ff')
    # elm_instance.SEND_cmd(b'a0 0f ca ff 32 ff')
    elm_instance.SEND_cmd(b'a0 0f 8a ff 4a ff')
    resps.append(elm_instance.RTRV_record(2))
    # could try to write '30 00 02 10 89' - not expecting acknowledgement
    # try to get only 2 messages here:
    # time.sleep(0.05)
    elm_instance.SEND_cmd(b' 30 00 02 10 89')
    # time.sleep(0.05)
    resps.append(elm_instance.RTRV_record(3))
    # time.sleep(0.05)
    elm_instance.SEND_cmd(b' b1')

    resps.append(elm_instance.RTRV_record(1))
    # elm_instance.recwaiting = 0

    # elm_instance.SEND_cmd(b'a3')
    # resps.append(elm_instance.RTRV_record())
    # time.sleep(0.1)
    elm_instance.SEND_cmd(b' 11 00 02 21 06')


    resps.append(elm_instance.RTRV_record())
    # time.sleep(0.1)
    # elm_instance.SEND_cmd(b' b1')

    # resps.append(elm_instance.RTRV_record(3))
    # elm_instance.recwaiting = 0

    # elm_instance.SEND_cmd(b'a3')
    # resps.append(elm_instance.RTRV_record())
    # time.sleep(0.1)
    #
    # elm_instance.SEND_cmd(b'11 00 02 21 01')
    #
    # resps.append(elm_instance.RTRV_record(2))
    #
    # # elm_instance.SEND_cmd(b'11 00 02 1A 9B')
    # # resps.append(elm_instance.RTRV_record(3))
    #
    # # elm_instance.SEND_cmd(b'13 00 02 1A 9B')
    # # resps.append(elm_instance.RTRV_record(3))
    # elm_instance.SEND_cmd(b'13 00 02 21 01')
    #
    # resps.append(elm_instance.RTRV_record(2))

    elm_instance.SEND_cmd(b' b5')
    resps.append(elm_instance.RTRV_record())
    pass

if __name__ == '__main__':
    main()