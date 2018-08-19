# Minimal IP to be used as a template

The minimal IP that:
 * passes the tests of the prototype validator (v. 2018-08-19) and
 * is valid according to Common Specification (v. 2018-08-19, commit ID: c1a6de5334e73393b58dc516e1fb54dc09dd7048)

The IP fulfills the following requirements:
 * The Information Package folder MUST include a file named “METS.xml” [Ch. 4.1 - CSIP4]
 * mets/@OBJID MUST exist and have a value [Ch. 5.2, CSIP3]
 * all @ID attributes MUST have a value that starts with a prefix, followed by the actual value of the identifier [Ch. 5.2]
 * structMap MUST exist [Ch. 5.3.6., CSIP80]
 * structMap/@TYPE MUST exist [Ch. 5.3.6., CSIP81]
 * structMap/div/@ID MUST exist [Ch. 5.3.6., CSIP84]
 * root folder MUST have `metadata` folder [Ch. 4.1 - CSIP5]
 * root folder MUST have `representations` folder [Ch. 4.1 - CSIP9]
 * `representations` folder MUST include a sub-folder for each individual representation [Ch. 4.1 - CSIP10]

The IP is actually not minimal according to Common Specification for several reasons, incl.:
 * mets/@TYPE can have any value, but the current validator only accepts values in the form "SIP:X", where X is one or more non-space characters
 * mets/metsHdr is not mandatory
