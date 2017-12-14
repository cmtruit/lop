import socket, os, sys


class DomainName(object):
    def __init__(self, shortname=None, fqdn=None, ip=None): 
        
       
        self.shortname = shortname.lower()
        self.fqdn = fqdn.lower()
        self.ip = ip

    def getFQDN(self):
        try:
            fqdn = socket.getfqdn(self.shortname)
            return fqdn
        except:
            print "Cannot get fqdn by shortname ", self.shortname

    def convertToHostname(self):
        try:
            name = socket.gethostname(self.ip)
            return name
       except:
            "Cannot get name by ip ", self.ip
            
         

    

