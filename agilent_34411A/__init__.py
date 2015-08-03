

import socket

class Agilent_34411A(object):

    EOL = '\n'
    timeout = 5.0

    def __init__(self, host, port=5025):
        self.host = host
        self.port = port
        self.connect()

    def connect(self):
        try:
            self.s = socket.create_connection((self.host, self.port), self.timeout)
        except (ConnectionRefusedError, socket.gaierror) as e:
            raise Agilent34411AConnectionException("Connection to host {} could not be established: {}".format(self.host, e))

    def query_cmd(self, cmd):
        cmd_line = cmd + Agilent34411A.EOL
        self.s.sendall(cmd_line.encode('ascii'))
        return self.s.recv(1024).decode('ascii').strip()

    def read(self):
        return float(self.query_cmd('READ?'))

    @property
    def idn(self):
        return self.query_cmd('*IDN?')

class Agilent34411AException(Exception):
    pass

class Agilent34411AConnectionException(Agilent34411AException):
    pass
