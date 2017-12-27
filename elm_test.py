import elm
import serial
import logging

# TODO test with elm dongle


def main():
    #     setup comport
    ser = serial.Serial(port='\\.\COM5',
                        baudrate=115200,
                        bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE)
    logging.basicConfig(filename='myapp.log')
    elm_instance = elm.Elm327(ser)
    elm_instance.initialize()
    pass

if __name__ == '__main__':
    main()