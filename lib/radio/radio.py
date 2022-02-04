class Radio:
    '''Interface class to control a radio.'''

    def __init__(**kwargs):
        print(f'init for Radio with: {kwargs}')

    def send():
        '''Send a message.'''
        raise NotImplementError('Should be implemented by derived class.')


    def receive():
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
