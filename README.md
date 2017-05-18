# OrthoConversion
We are taking existing orthoMcl(OMCL) re Written Perl and Translating it to Python
The orgrinal software OrthoMCL-DB project was initiated by Feng Chen in April 2005, and people from PCBI/Penn Center for Bioinformatic center.  The project has been funded in whole or in part with Federal funds from the National Institute of Allergy and Infectious Diseseases, National Institutes of Health, Department of Health and Human Services, under Contract No. HHSN266200400037C. The major PIs are Drs. David Roos and Chris Stoeckert.

Our work will intially be to translate the code from Perl to Python for the ease of manipulation.  We are pursuing a means of genomic comparison that will detect subtile differences in proteins both intra and inter species.  The following is our understanding and the methods we are using to approach this problem.  
ORTHOMCL
OrthoMCL software package 2.0 consits of 14 diffrent modules aka Packages and one main engine.  The engine is the commands for operating each specfic sequence.  We will lable each working file with a .py for python with the same name as the orginal file from OMCL.  We invite anyone with experience in Perl to Python tranlations to join us in making a translated version for the use of any who might find it easier to manipulate.
To date here is what we have done OMCL adjust fasta, needs regrex commands and import libraries; OMCL Blast Parser, needs method get genes from fasta and regrex commands and import libraries;ortho Drop schema needs coding for Mysql data base import export and config files; Dump parse files needs base call? and to finish coding for Mysql; Extract protein Ids is farily strait forward it nneds some work with mysql calls;  Basepy is just started it needs work all around.  
What we really need is help with regrex commands any TODO lists as these are not readily apparent to non CS biologist.

PLease feel free to Contact me Jaduran@miners.utep.edu
