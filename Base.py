#import ; package OrthoMCLEngine::Main::Base;

def new(class, configFile, loghandle):
    self = {}
    #TODO bless
    parseConfigFile(self, configFile, loghandle)
    return self

def parseConfigFile(self, configFile, loghandle):
    file = open(configFile, 'r+')
    self[configFile] = configFile
    for line in file:
        line.rstrip('\n')
        #TODO regular expressions
        key = #matches to regex search
        val = #matches to regex search
        self[config[key]] = val
        if(loghandle)# db password



def getConfig(self, prop):
    if(self[config[prop]])
       return self[config[prop]]
    else
        sys.exit(0)

def getDbh(self):
    if(!self[dbh]):
        dbVendor = self[getConfig("dbVendor")]
        if(dbVendor == 'oracle')
            import #DBD::Oracle;
        elif(dbVendor == 'mysql')
            import #DBD::mysql
        else
            sys.exit(0)
        self[dbh]=#sql commands

    return self[dbh]

