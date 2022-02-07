from .gps import Gps

class GROVE(Gps):
    
    def __init__(self, uid, **kwargs):
        print(f'init for GROVE with: {kwargs}')
        
        super().__init__(uid, **kwargs)

    def get_location(self):
        print('grove getting location...')
