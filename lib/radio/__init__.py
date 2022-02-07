from .rf24 import RF24

def open_resource(**kwargs):
    for derived_class in [RF24]:
        try:
            return derived_class(**kwargs)
        except Exception as e:
            continue

    raise ConnectionError('Unable to open PSU')
