import sys
import os

if(len(sys.argv) < 2)
    usage

blastFile = sys.argv[0]
sys.argv = argv[1:]
fastaFilesDir = sys.argv[0]
sys.argv = sys.argv[1:]

fastaFiles = []
for filename in os.listdir(fastaFilesDir):
    fastaFiles.append(filename)

genes = getGenesFromFasta(fastaFilesDir, fastaFiles)

files = open(blastFile, "r+") #kill if cant open


#query_name, hitname,
#$pcid, len,
#mismatches, ngaps,
#start('query'), end('query'),
#start('hit'), end('hit'),
#evalue, bits

prevSubjectId = 'blah'
prevQueryId = 'blah'

if __name__ == '__main__':
    for line in files:
        line.rstrip('\n')
        queryId, subjectId, percentIdentity, length, mismatches, ngaps, queryStart, queryEnd, subjectStart, subjectEnd, evalue, bits = line.split()
        if(queryId != prevQueryId or subjectId != prevSubjectId):
            #print previous subject, update hash
            #TODO: look up: hash




        # Get additional infro from subsequent HSPs
        hspspan = [subjectStart, subjectEnd]
        if(subject -> {queryShorter})
            hspspan = [queryStart, queryEnd]
        #TODO: where are they getting the queue, update hash
#print previous

def getGenesFromFasta():














