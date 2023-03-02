eark-ip-test-corpus
===================

The purpose of the E-ARK test corpus is to make it possible to see if any given validator is covering all the rules laid out in the specifications. 

Quick Start
-----------
- [An overview of the 3 stage information package validation process](./VALIDATION.md)
- [Process documentation for test case and corpus package creation](./PROCESS.md)
- [A guide to documenting test cases](./TESTCASES.md)

Introduction
------------
This repository is home to the E-ARK information package validation test corpus. 

The E-ARK test corpus comprises a set of human readable and machine readable test cases which also includes E-ARK information packages that contain valid and invalid samples related to each of the requirements within the following specifications: 
-	[the Common Specification for Information Packages](https://earkcsip.dilcis.eu/) - hereafter called CSIP
-	[the E-ARK Specification for Submission Information Packages](https://earksip.dilcis.eu/) hereafter called SIP
-	[the E-ARK Specification for Dissemination Information Packages](https://earkdip.dilcis.eu/) hereafter called DIP 

The corpus serves two purposes:

- It provides a set of information package samples that can be used to test software validators for the CSIP, SIP, and DIP, this includes our [own validator](https://github.com/E-ARK-Software/py-rest-ip-validator).
- The creation of the corpus tests our understanding of the current specification document. Every test case represents a simple, implemented example of a validation error or warning with accompanying valid cases.
__________

Status
------
The test corpus is currently in development.
__________

Scope & Coverage
----------------
### Specification coverage
An ideal validation corpus should be a physical demonstration of each and every requirement stated in the specifications. In testing terms, this aspiration is expressed as 100% coverage of the specification. The progress towards this milestone can be expressed as a percentage coverage of the specification requirements.


### Out of scope
There are some test case and corpus examples that we consider to be explicitly out of scope

#### Testing METS schema validation
We won't be providing test cases and corpus examples for issues that should be caught by automated XML parsing with XML schema validation enabled. The E-ARK CSIP METS implementation is based upon version 1.12 of the METS schema: https://www.loc.gov/standards/mets/version112/mets.xsd. 
We won't be creating test cases that represent a missing `mets` root element, the lack of a `structMap` element, or mis-spelled METS element and attribute names in general.
__________________

#### Corpus Structure
**To Be Discussed**
__________________

Validation Corpus Creation
--------------------------
### Process Overview
The E-ARK Common Specification is the source of requirements and the yardstick by which progress is measured. The test corpus creation process is driven by the specification conditions. These requirements are read carefully and used to produce test cases. These documented test cases provide the backlog for the creation of corpus test packages. For each test case there should be corpus packages demonstrating the pass and fail conditions.

### Requirements to Test Cases
While the aim is to produce test cases, analysis of the specification will also lead to improvements to the specification.  To illustrate, consider a seemingly simple requirement from the specification:

> CSIP4: The Information Package folder MUST include a metadata file named `METS.xml`, which includes information about the identity and structure of the package and its components;

At first this suggests a simple pass and fail case, one with the file present and another from which it is missing. A more careful reading reveals that the file should contain "information about the identity and structure of the package...". The wording is problematic as there are no details of what the information should be. Reading with a testing mindset yields further varieties of test case, e.g. what about case-sensitivity in the name - are `mets.xml`, `METS.XML`, or even `mEts.xMl` acceptable?

### Adding Test Cases to the backlog
The next actions here should be:
- add the set of test cases to be produced to the [project issue tracker](https://github.com/DILCISBoard/eark-ip-test-corpus/issues) (Guide / Template / this example coming soon).
- log an issue on the [specification project tracker](https://github.com/DILCISBoard/E-ARK-CSIP/issues) suggesting that the wording for the second part of the requirement is reviewed or removed.

### Creating Test Cases
The full guide to test case creation is in the [`TESTCASES.md`](./TESTCASES.md)
document.

Tracking Progress & Metrics
---------------------------
### Test Case backlog
The number of open issues with a test case label...
**To Be Discussed**
