from logger import logging

def add(a,b):
    logging.debug('adding')
    return a + b

logging.debug('adding functions is called')
print(add(10,15))