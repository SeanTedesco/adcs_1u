#import serial

class Radio:
    '''Interface class to control a radio.'''

    def __init__(self, port, baudrate, **kwargs):
        print(f'init for Radio with: {kwargs}')

        self.port = port
        self.baudrate = baudrate
        self.arduino = 10
        #self.arduino = serial.Serial(port=self.port, baudrate=self.baudrate, timeout=10, rtscts=True)


    def send(self, **kwargs):
        '''Send a message.'''
        raise NotImplementError('Should be implemented by derived class.')


    def receive(self, **kwargs):
        '''Receive a message.'''
        raise NotImplementError('Should be implemented by derived class.')


def parse_cmdline():
    pass

def main():
    from . import open_resource

    options = parse_cmdline()
    radio = open_resource(uid='radio_uid')

    options.functions(options, radio)

if __name__ == '__main__':
    main()
