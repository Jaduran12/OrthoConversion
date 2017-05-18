

import textwrap
import sys


def usage():
    print("""\
    Create an OrthoMCL compliant .fasta file, by adjusting definition lines.

    Usage:
      orthomclAdjustFasta taxon_code fasta_file id_field

    where:
      taxon_code:  a three or four letter unique abbreviation for the taxon
      fasta_file:  the input fasta file
      id_field:    a number indicating what field in the definition line contains
                   the protein ID.  Fields are separated by either ' ' or '|'. Any
                   spaces immediately following the '>' are ignored.  The first
                   field is 1. For example, in the following definition line, the
                   ID (AP_000668.1) is in field 4:  >gi|89106888|ref|AP_000668.1|

    Input file requirements:
      (1) .fasta format
      (2) a unique id is provided for each sequence, and is in the field specified
          by id_field

    Output file format:
      (1) .fasta format
      (2) definition line is of the form:
             >taxoncode|unique_protein_id

    The output file is named taxoncode.fasta

    Note: if your input files do not meet the requirements, you can do some simple perl or awk processing of them to create the required input files to this program, or the required output files.  This program is provided as a convenience, but OrthoMCL users are expected to have the scripting skills to provide OrthoMCL compliant .fasta files.

    EXAMPLE: orthomclSoftware/bin/orthomclAdjustFasta hsa Homo_sapiens.NCBI36.53.pep.all.fa 1
              """)
    sys.exit(0)


if (len(sys.argv) == 3):

    taxoncode = sys.argv[0]
    inputfile = sys.argv[1]
    idField = sys.argv[2]
    cmd = taxoncode + ".fasta"
    IN = open(inputfile, -r)
    OUT = open(cmd, -w)

    #  Needs exceptions 
	# Needs Translation of regrex 
	for line in IN:
        if ( /\ > / ):
            s / ^ \ >  \s * //
            s / \s + / / g
            s / \s * \ |  \s * / \ | / g

            a = split( / [\s\ |] / )
            id = a[idField - 1]

            die
            "Fasta file 'inputfile' contains a duplicate id: id\n" if ids
            {id}
            ids
            {id} = 1;
            print
            OUT
            ">$taxoncode|$id\n"
            else
            print
            OUT_


else
    usage()


