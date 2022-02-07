from .radio import Radio

class RF24(Radio):
    
    def __init__(self, uid, **kwargs):
        print(f'init for RF24 with: {kwargs}')
        
        self.uid = uid
        
        super().__init__(uid, **kwargs)

    def send(self):
        print('rf24 sending...')

    def receive(self):
        print('rf24 receiving...')
