import os
import select
import sys
import pybonjour
import atexit
from pprint import pprint


class Backend:
    def types(self):
        print "NOT IMPLEMENTED"
    
    def load_group(self, alternate_location=None):
        print "NOT IMPLEMENTED"
    
    def save_group(self, servicegroup, alternate_location=None):
        name = servicegroup['name']
        self.add_service(name, servicegroup['services'])

    def add_service(self, name, opts):
        sdRef = pybonjour.DNSServiceRegister(name = name,
                                            regtype = opts['type'],
                                            port = opts['port'],
                                            domain = opts['domain'])
        atexit.register(self.cleanup_service, sdRef)

    def cleanup_service(self, sdRef):
        sdRef.close()


    def remove_group(self, alternate_location=None):
        print "NOT IMPLEMENTED"

    def query(self, type=None):
        print "NOT IMPLEMENTED"
