# Minimal IP to be used as a template

The absolute minimal IP to pass the current version (as of 2018-08-14) of the validator is this 13-line METS.xml file, no other files or folders needed.

It is not actually valid according to Common Specification for several reasons, incl.:
 * mets/@OBJID must have a value
 * structMap/@TYPE is mandatory
 * structMap/div/@ID is mandatory
 * metadata folder is mandatory in the root folder of IP

It is also not minimal according to Common Specification for several reasons, incl.:
 * mets/@TYPE can have any value, but the current validator only accepts values in the form "SIP:X", where X is one or more non-space characters
 * mets/metsHdr is not mandatory
 * structMap/div/div is not mandatory
