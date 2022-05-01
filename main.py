#####################################
# IMPORTS
#####################################
from satsystems.radio.rf24 import RF24
from satsystems.gps.grove import Grove
from satsystems.camera.picam import PiCam
from satsystems.logger.logger import SatelliteLogger
from gpiozero import LED
from time import sleep

class OBC:
    def __init__(self):
        self.logger = SatelliteLogger.get_logger('main.py')
        self.green_led = LED(22)
        self.yellow_led = LED(23)
        self.red_led = LED(24)

        self.expected_commands = [
            'smile',
            'picture',
            'rotate',
        ]

    def run_command(self, cmd, *args, **kwargs):
        cmd = cmd.strip()
        if cmd is None:
            raise ValueError('no command given to obc!')
        
        if cmd == 'smile':
            self.do_smile(*args, **kwargs)
            return True
        
        if cmd == 'picture':
            self.do_picture(*args, **kwargs)
            return True

        if cmd == 'rotate':
            self.do_rotate(*args, **kwargs)
            return True

    def do_smile(self, *args, **kwargs):
        for i in range(5):
            self.red_led.on()
            sleep(1)
            self.red_led.off()
            sleep(1)

    def do_picture(self, *args, **kwargs):
        pass

    def do_rotate(self, *args, **kwargs):
        pass


def main():

    '''initialize all the systems'''
    obc = OBC()
    obc.logger.info('begining main satellite program')

    comms = RF24(port='/dev/ttyACM0')
    obc.logger.info('created comms')

    grove_gps = Grove(uid='gps-2', port='/dev/ttyUSB1', baudrate=115200)
    obc.logger.info('created gps')

    payload = PiCam()
    obc.logger.info('created payload')


    '''main loop'''
    while True:
        msg_received = comms._receive_single_message()
        if msg_received in obc.expected_commands:
            obc.logger.info(f'starting command: {msg_received}')
            try:
                obc.run_command(msg_received)
                obc.logger.info(f'finished command: {msg_received}')
            except:
                obc.logger.warning(f'failed to run command: {msg_received}')
        sleep(1)
        obc.yellow_led.toggle()

if __name__ == '__main__':
    main()
