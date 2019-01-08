E-ARK IP Validation
====================

Validation Process
------------------
We model and implement Information Package validation as a three stage process.

### Stage 1: Well-Formedness Checks
Checks the structure of the package but doesn't open or parse any of the contents (so empty files are OK for testing). These requirements are generally found in [Section 4.1 of the common specification](https://dilcisboard.github.io/E-ARK-CSIP/implementation/). Tests include:
- the form of the submission (zip preferred);
- the presence of expected named folders (e.g. metadata folder expected);
- the presence of expected files (e.g. root `METS.xml`).

Note: "Well-formedness" is to be interpreted as "Information Package well-formedness," not to be confused with XML document well-formedness. A well-formed Information Package conforms to the basic structural rules set in CSIP. This stage of validation is not concerned with well-formedness of the XML files inside the Information Package.

### Stage 2: Validity Checks
Depends on the presence of the `METS.xml` file. At this stage, we're parsing and validating the XML documents and probably some of the associated metadata. These tests will generally be drawn from [Section 5.3 Use of METS](https://dilcisboard.github.io/E-ARK-CSIP/implementation/#53-use-of-mets). Examples are:
- validation of the METS document against the METS schema;
- applying additional schema, e.g. the E-ARK extension schema for an `OAISPACKAGETYPE`: https://github.com/DILCISBoard/E-ARK-CSIP/blob/doc/readme/xml/DILCISExtensionMETS.xsd;
- running Schematron checks that enforce requirements from the implementation section of the common specification.

Note: "Validity" is to be interpreted as "Information Package validity." It is not to be confused with XML document validity (the document's conformance to the rules set in a particular XML schema), which is only a part of Information Package validity. This stage of validation includes checking individual METS.xml files for well-formedness and validity against schemas (mets.xsd, E-ARK extension schema), and running Schematron checks for requirements set in CSIP.

### Stage 3: Integrity Checks
The final checks are physical tests on the package content and include:
- ensuring files listed in the METS document are present on the file system;
- these files have the correct checksums (if the values are available);
- that there are no files in the package NOT mentioned in the METS document.

Note: "Integrity" is to be interpreted as "Information Package integrity," not to be confused with individual file integrity. Thus, "integrity" refers to the accuracy and consistency of the whole Information Package, while individual file integrity is part of it.

Validation Errors
-----------------
The validator uses the `commons-ip` ValidationEntry structure for errors, which defines the following fields:

- Level: One of `[INFO | WARNING | ERROR]` where
  - `ERROR` indicates the violation of a `MUST` specification clause;
  - `WARNING` is issued for violations of `SHOULD` clauses;
  - `INFO` for all other messages, current example is that the validator reports finding the `METS.xml` file.
- Message: A free text string, currently hard-coded.
- Description: A free text description, often unpopulated, again hard-coded.
- A list of Paths to referenced objects, e.g. a single path to the METS document if that's not valid.

While we'll work within these constraints we quite probably require further information:

- a unique identifier for the error condition;
- a reference to the precise validation check where message and description are outside of the code and in approved, specification friendly terms.
