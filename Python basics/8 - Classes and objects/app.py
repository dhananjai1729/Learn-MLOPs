import logging

## logging setting

logging.basicConfig(
    level= logging.DEBUG,
    format= '%(asctime)s - %(name)s-%(levelname)s - %(message)s',
    datefmt = "%Y-%m-%d %H:%M:%",
    handlers= [
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("arithmeticAPP")

#add
def add(a, b):
    logger.debug(f'Adding {a} + {b}'.format(a=a, b=b))
    return a + b

#subtraction
def subtract(a, b):
    logger.debug(f'Subtracting {a} - {b}'.format(a=a, b=b))
    return a - b

#multiplication
def multiply(a, b):
    logger.debug(f'Multiplying {a} * {b}'.format(a=a, b=b))
    return a * b

#division   
def divide(a, b):
    logger.debug(f'Dividing {a} / {b}'.format(a=a, b=b))
    if b == 0:
        logger.error('Cannot divide by zero')
        raise ValueError('Cannot divide by zero')
    return a / b

add(10,15)

subtract(3,2)

multiply(5,3)

divide(10,2)