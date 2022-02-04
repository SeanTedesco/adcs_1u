import radio.Radio

class RF24(Radio):
    
    def __init__(self, **kwargs):
        print(f'init for RF24 with: {kwargs}')
        super.__init__(**kwwargs)

    def send():
        print('rf24 sending...')

    def receive():
        print('rf24 receiving...')
