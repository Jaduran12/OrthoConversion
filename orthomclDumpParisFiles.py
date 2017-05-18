#TODO: import bin, DBI, lib, main Base

import sys

config file = sys.argv[0]

parentDir = sys.argv[1]  #undocumented: for workflow applications
suffix = sys.argv[2]     #same

#chdir parentDir
  #if parentDir

if(configFile)
    usage()

base = #imported base module with configFile
dbh = # base getDBH

orthologTable = #base->getConfig("orthologTable")
inParalogTable = #base->getConfig("inParalogTable")
coOrthologTable = #base->getConfig("coOrthologTable")

dir = "pairs"

#makes new directory doesnt override existing an existing
#use a system command to create a new directory

printOrthologsFile(dbh, orthologTable, dir+"/orthologs.txt")
printInparalogsFile(dbh, inParalogTable, dir+"/inparalogs.txt")
printOrthologsFile(dbh, coOrthologTable, dir+"/coorthologs.txt")
printMclAbcFile(dbh, orthologTable, inParalogTable, coOrthologTable, "mclInput")

def printInparalogsFile():
    #takes inputs dbh inparalogTable and filename

    sql = #sql command?

    stmt = #dbh/Base command, kill if error

    IN = open(fileName, 'w')
    while: #variables equal to output from stmt

        #TODO: finnish this def, finish other two print def, figure out how to make base call

def usage():
    print("""\
    Dump files from the database produced by the orthomclPairs program.

    usage: orthomclDumpPairsFiles config_file

    where:
      config_file : see below (you can use the same file given to orthomclPairs)

    Database Input:
      - InParalog, Ortholog, CoOrtholog tables - populated by orthomclPairs

    Output files:
      mclInput                               - file required by the mcl program
      pairs/                                 - dir holding relationship files
        potentialOrthologs.txt               - ortholog relationships
        potentialInparalogs.txt              - inparalog relationships
        potentialCoorthologs.txt             - coortholog relationships

    The pairs/ files contain the pairs found by the orthomclPairs tables, and their
    average normalized scores.  This is the same information as in the
    orthomclMclInput file, but segregated by relationship type.  These are
    candidate relationships (edges) that will subsequently be grouped (clustered)
    by the mcl program to form the OrthoMCL ortholog groups.  These files contain
    more sensitive and less selective relationships then the final ortholog groups.

    Standard Error:
      - logging info

    EXAMPLE: orthomclSoftware/bin/orthomclDumpPairsFile my_orthomcl_dir/orthomcl.config

    Sample Config File:

    dbVendor=oracle  (or mysql)
    dbConnectString=dbi:Oracle:orthomcl
    dbLogin=my_db_login
    dbPassword=my_db_password
    orthologTable=Ortholog
    inParalogTable=InParalog
    coOrthologTable=CoOrtholog
          """)
    sys.exit(0)