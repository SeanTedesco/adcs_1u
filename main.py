from lib.radio.rf24 import RF24
from lib.gps.grove import GROVE

print('hello from the satellite program!')

comms = RF24(uid='/dev/ttyUSB0')
grove_gps = GROVE(uid='/dev/ttyUSB1')

comms.send()
