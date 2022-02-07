class Gps:
    '''Interface class to control a GPS.'''

    def __init__(self, uid, **kwargs):
        print(f'init for GPS with: {kwargs}')
        
        self.uid = uid

    def get_location(self, **kwargs):
        '''Send a message.'''
        raise NotImplementError('Should be implemented by derived class.')


def parse_cmdline():
    pass

def main():
    from . import open_resource

    options = parse_cmdline()
    gps = open_resource(uid='gps_uid')

    options.functions(options, gps)

if __name__ == '__main__':
    main()
