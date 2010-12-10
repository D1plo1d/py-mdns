
class servicegroup:
    def __init__(self, replace_wildcards=False):
        self.__name = None
        self.__services = []
        self.__replace_wildcards = replace_wildcards

    @property
    def name(self):
        return self.__name
    
    @property
    def replace(self):
        return self.__replace_wildcards
    
    @property
    def services(self):
        return self.__services

class service:
    def __init__(self, **kwargs):
        # Required
        if len(kwargs) > 0:
            self.__type = kwargs['type']
            self.__port = kwargs['port']
            self.__localized_name = kwargs['name']
            self.__sysname = kwargs['sysname']
            self.__state = kwargs['state']
        
        # Optional
        self.__protocol = 'ipv4'
        self.__domain_name = None
        self.__host_name = None
        self.__subtypes = None
        self.__txt = {}
        
    def __str__(self) :
        return str(self.__dict__)

    def __eq__(self, other) : 
        return self.__dict__ == other.__dict__
    
    def __hash__(self):
        return hash((self.__type,
                     self.__port,
                     self.__localized_name,
                     self.__sysname,
                     self.__state))
            
    @property
    def type(self):
        return self.__type;

    @property
    def type_full(self):
        return (self.__type, self.__localized_name);

    @property
    def port(self):
        return int(self.__port);
    
    @property
    def protocol(self):
        return self.__protocol;
    
    @property
    def domain_name(self):
        return self.__domain_name;
    
    @property
    def host_name(self):
        return self.__host_name;

    @property
    def subtypes(self):
        return self.__subtypes;
    
    @property
    def txt(self):
        return self.__txt;
    
    @property
    def localized_name(self):
        return self.__localized_name
    
    @property
    def sysname(self):
        return self.__sysname;

    @property
    def state(self):
        return self.__state;
