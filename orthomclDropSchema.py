#TODO: import bin and libraries, import main orthoMCL engine-base

if(len(sys.argv) >= 1)
    usage()
configFile = sys.argv[0]
sqlLog = sys.argv[1]
suffix = sys.argv[3]

base = #base new configFile
dbh = #base get DBH

if(sqlLog)
    #open(LOGFILE, >sqlLog

#runSql("drop table ". $base->getConfig("similarSequencesTable"). $suffix);
#runSql("drop table ". $base->getConfig("inParalogTable"). $suffix);
#runSql("drop table ". $base->getConfig("orthologTable"). $suffix);
#runSql("drop table ". $base->getConfig("coOrthologTable"). $suffix);
#runSql("drop view ". $base->getConfig("interTaxonMatchView"). $suffix);

def runSql():
    sql = [0]
    if(sqlLog)
        logSql(sql)
    #TODO: system calls to main base

def logSql():
    sql = [0]
    print LOGFILE "\nsql"


def usage():
    print("""\
    Drop OrthoMCL schema

    usage: orthomclDropSchema config_file sql_log_file

    where:
    config_file : see below
    sql_log_file : optional log of sql executed

    EXAMPLE: orthomclDropSchema my_orthomcl_dir/orthomcl.config my_orthomcl_dir/drop_schema.log

    NOTE: the database login in the config file must have the required database privileges on the tables specified in the config file.

    Sample Config File:

    dbVendor=oracle  (or mysql)
    dbConnectString=dbi:Oracle:orthomcl
    dbLogin=my_db_login
    dbPassword=my_db_password
    oracleIndexTablespace=
    similarSequencesTable=SimilarSequences
    orthologTable=Ortholog
    inParalogTable=InParalog
    coOrthologTable=CoOrtholog
    interTaxonMatchView=InterTaxonMatch
    """)
    sys.exit(0)


