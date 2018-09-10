eark-ip-test-corpus
===================
Test corpus of E-ARK information packages to test validator functionality against the specification.

Introduction
------------
This repository is home to the E-ARK information package validation test corpus. The corpus comprises a set of information packages, each is intended to violate the [E-ARK Common Specification for Information Packages](DILCISBoard/E-ARK-CSIP) **(CSIP)** in a single specific way. The corpus serves two purposes:

- It provides a set of information package samples that can be used to test software validators for the CSIP, this includes our [own validator](DILCISBoard/rest-ip-validator).
- The creation of the corpus tests our understanding of the current specification document. Every test case represents a simple, implemented example of a validation error or warning with accompanying valid cases.
__________

Status
------
The test corpus and validator are currently in early development, we'll provide a more detailed roadmap in September 2018.
__________

Validation Corpus Creation
--------------------------
### Process Overview
The E-ARK Common Specification is the source of requirements and the yardstick by which progress is measured. The test corpus creation process is driven by the specification conditions. These requirements are read carefully and used to produce test cases. These documented test cases provide the backlog for the creation of corpus test packages. For each test case there should be corpus packages demonstrating the pass and fail conditions.

### Requirements to Test Cases
While the aim is to produce test cases, analysis of the specification will also lead to improvements to the specification.  To illustrate, consider a seemingly simple requirement from the specifcation:

> CSIP4: The Information Package folder MUST include a metadata file named `METS.xml`, which includes information about the identity and structure of the package and its components;

At first this suggests a simple pass and fail case, one with the file present and another from which it is missing. A more careful reading reveals that the file should contain "information about the identity and structure of the package...". The wording is problematic as there are no details of what the information should be. Reading with a testing mindset yields further varieties of test case, e.g. what about case-sensitivity in the name - are `mets.xml`, `METS.XML`, or even `mEts.xMl` acceptable?

#### Producing Test Cases
The next actions here should be:
- add the set of test cases to be produced to the [project issue tracker](https://github.com/DILCISBoard/eark-ip-test-corpus/issues) (Guide / Template / this example coming soon).
- log an issue on the [specification project tracker](https://github.com/DILCISBoard/E-ARK-CSIP/issues) suggesting that the wording for the second part of the requirement is reviewed or removed.

Documenting the test cases:
- Assign an ID
- Provide reference to the specification
- Define the error level, message and description expected from the validator
- Document the minimal corpus package structure.

There is a one to many relationship between specification requirements and test cases. The test cases provide fine-grained, detailed demonstrations of pass and fail conditions for the requirments.

### Test Cases to Corpus Packages
Every test case should be atomic and minimal. Atomic means that it violates only a single aspect of the specification. Minimal means that it contains only the data and metadata required to ensure only a single validator error is produced. **NOTE: To simplify this we want to introduce the concepts of "well-formed", "valid", and "audited" (what's a good word for passing integrity checks?), to allow minimal files that pass only the well formed structural checks possible, without the need for content**
The E-ARK information package validation process has been broken into 3 parts, [described here](VALIDATION.md).

There should be pass and fail corpus packages for each test case, although it's possible that multiple test cases share a single "pass" case for brevity.

Producing test corpus packages that match the test cases:
- create the package locally;
- test against the prototype validator instance (locally or online)
- submit to GitHub corpus repository as a pull request for review

#### Corpus Structure
**To Be Discussed**
__________________

Progress Metrics
-----------------
### Specification Coverage
An ideal validation corpus should be a physical demonstration of each and every requirement stated in the Common Specification. In testing terms, this aspiration is expressed as 100% coverage of the specification. The progress towards this milestone can be expressed as a percentage coverage of the specification requirements.

While this is the most important metric, it's not easy to provide an objective, automatable measure. The A2 specification group will be the aribiter here.

### Test Case backlog
The number of open issues with a test case label...
**To Be Discussed**
