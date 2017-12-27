from . import elm
import serial
import logging

def main():
    #     setup comport
    ser = serial.Serial(port='\\.\COM6',
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