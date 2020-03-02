import socket
from struct import unpack_from
import time

UDP_IP = "0.0.0.0"
UDP_PORT = 6000

properties = ['x_acc', 'y_acc', 'z_acc', 'x_gravity', 'y_gravity', 'z_gravity',  'x_rotation', 'y_rotation', 'z_rotation',
              'x_orientation', 'y_orientation', 'z_orientation', 'deprecated_1', 'deprecated_2', 'ambient_light', 'proximity',
              'keyboard_button_pressed']


def unpack_and_return(data, offset):
    return unpack_from("!f", data, offset)[0]


def process_data(data):
    offset = 0
    result = {}
    for property in properties:
        result[property] = unpack_and_return(data, offset)
        offset += 4
    return result


def listen_sensor_data():
    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        data = process_data(data)
        yield data, addr

#
# prev_data = {}
#
# def has_changed(data, address):
#     result = False
#     previous = prev_data[address]
#     current = data
#
#     if data['ambient_light']
#
#
#
# for d, a in listen_sensor_data():
#     prev_data[a] = d
#     print(d, a)

