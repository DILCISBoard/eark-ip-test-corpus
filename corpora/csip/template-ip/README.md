Minimal Information Package
===========================
These two packages represent 
- a minimal information package 
- a minimal information package with schemas
that is valid according to the current draft of the E-ARK Common Specification. 

The minimal package consists of
a minimal physical structure. This contains only the set of files and folders
that are mandatory according to the specification. The package
[METS file](package/METS.xml) contains only mandatory XML elements and
attributes, including those needed to satisfy specification requirements
regarding elements and attributes that correspond to the minimal package files
and folders.

The minimal package with schemas consists of
a minimal physical structure. This contains only the set of files and folders
that are mandatory according to the specification + local schemas. The package
[METS file](package/METS.xml) contains only mandatory XML elements and
attributes, including those needed to satisfy specification requirements
regarding elements and attributes that correspond to the minimal package files
and folders for an IP with local schemas.

Status
------

### Assertions
This minimal IP:
 * ~~passes the tests of the prototype validator (v. 2018-08-19) and~~
 * is valid according to Common Specification (v. 2018-09-18, commit ID: 220988a70bfd1f1c19ff50d2c1409b5ddf7aa250), pending review by the DILCIS Board

### ToDo
- [] Test against current prototype validator instance
- [] Review by DILCIS Board members
- [] Check dependency against ID requirements inferred from ["The use of identifiers"](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/metadata/#the-use-of-identifiers) section of the CSIP.

Physical Package Structure
--------------------------
The IP physical structure contains a single representation and consists of the
mandatory files and folders shown below:
```
root/
  |
  |- METS.xml
  |- metadata/
  |- representations/
       |
       |- rep1/
            |
            |- data/
```
This structure satisfies the following MUST structural requirements:
-
[CSIPSTR1](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/structure/#CSIPSTR1)
  IP MUST be included in a single physical folder;
- [CSIPSTR4](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/structure/#CSIPSTR4)
  IP root folder MUST include a metadata file named `METS.xml`;
- [CSIPSTR5](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/structure/#CSIPSTR5)
  IP root folder MUST include a folder named `metadata`;
- [CSIPSTR9](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/structure/#CSIPSTR9)
  IP root folder MUST include a folder named `representations`;
- [CSIPSTR10](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/structure/#CSIPSTR10)
  `Representations` folder MUST include a folder for each representation; and
- [CSIPSTR11](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/structure/#CSIPSTR11)
 `Representation` folder MUST include a folder `data`.

Package Metadata
----------------
The package consists of a single root [`METS.xml` file](package/METS.xml). The
file contains only the XML elements and attributes required to describe the
physical structure described above.

- [CSIP1](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/metadata/#CSIP1)
`mets` root element required;
- [CSIP2](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/metadata/#CSIP2)
`mets/@OBJID` attribute required;
- [CSIP3](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/metadata/#CSIP3)
`mets/@TYPE` attribute required;
- [CSIP4](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/metadata/#CSIP4)
`mets/@CONTENTTYPESPECIFICATION` attribute with value from fixed vocabulary set required;
- [CSIP6](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/metadata/#CSIP6)
`mets/@PROFILE`
- [CSIP7](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/metadata/#CSIP7)
`metsHdr` element required;
- [CSIP9](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/metadata/#CSIP9)
`metsHdr/@CREATEDATE` attribute required;
- [CSIP11](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/metadata/#CSIP11)
`metsHdr/@csip:OAISPACKAGETYPE` attribute with value from fixed vocabulary set required;
- [CSIP12](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/metadata/#CSIP12)
`metsHdr/agent` element required;
- [CSIP13](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/metadata/#CSIP13)
`metsHdr/agent/@ROLE` attribute with value `CREATOR` required;
- [CSIP15](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/metadata/#CSIP15)
`metsHdr/agent/@TYPE` attribute with value `OTHER` required;
- [CSIP16](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/metadata/#CSIP16)
`metsHdr/agent/@OTHERTYPE` attribute with value `SOFTWARE` required;
- [CSIP17](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/metadata/#CSIP17)
`metsHdr/agent/name` element required;
- [CSIP18](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/metadata/#CSIP18)
`metsHdr/agent/note` element required, inferred by CSIP16 above;
- [CSIP19](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/metadata/#CSIP19)
`metsHdr/agent/[note](NOTETYPE)` attribute with value `SOFTWARE VERSION` required, inferred by CSIP16 above;
- [CSIP80](https://dilcisboard.github.io/E-ARK-CSIP/specification/implemenxtation/metadata/#CSIP80)
`structMap` element required;
- [CSIP81](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/metadata/#CSIP81)
`structMap/@TYPE` attribute with value `physical` required;
- [CSIP82](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/metadata/#CSIP82)
`structMap/@LABEL` attribute with value `Common Specification structural map` required.
- [CSIP83](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/metadata/#CSIP83)
`structMap/div` elements required to describe mandatory metadata and representations folder structures;
- [CSIP84](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/metadata/#CSIP83)
`structMap/div/@ID` attribute required with unique ID (within package), ID must comply with E-ARK ID criteria (currently without link).
- [CSIP85](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/metadata/#CSIP85)
`structMap/div/@LABEL` attribute required, top level div label value should be the package ID, all other div label values should correspond to the folder name.
