import logging

logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')


class A:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

aa = A(100)
print(aa)
