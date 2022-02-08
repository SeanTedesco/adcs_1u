from lib.radio.rf24 import RF24
from lib.gps.grove import GROVE

print('hello from the satellite program!')
print()

comms = RF24(uid='transmitter-1', port='/dev/ttyUSB0', baudrate=115200)
grove_gps = GROVE(uid='gps-2', port='/dev/ttyUSB1', baudrate=115200)

print(f'using {comms.uid} as comms device')
print(f'using {grove_gps.uid} as gps device')
comms.send()
print()
