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
        for service in servicegroup.services:
            self.add_service(service)

    def add_service(self, service):
        sdRef = pybonjour.DNSServiceRegister(name = service.name,
                                            regtype = service.type,
                                            port = service.port,
                                            domain = "local.")
        atexit.register(self.cleanup_service, sdRef)

    def cleanup_service(self, sdRef):
        sdRef.close()


    def remove_group(self, alternate_location=None):
        print "NOT IMPLEMENTED"

    def query(self, type=None):
        print "NOT IMPLEMENTED"
