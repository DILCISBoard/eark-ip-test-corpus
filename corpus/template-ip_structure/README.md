Information Package with recommended physical structure
===========================
This package represents
- a physical structure
that includes all the files and folders described in the MUST and SHOULD requirements in the current draft of the E-ARK Common Specification.

The IP package with physical structure includes only the files and folders that have been described in the MUST and SHOULD requirements of the specification. The package [METS file](IP_physical_structure/METS.xml) is empty file. All the folders include only either other folder(s) or .gitkeep file.

Status
------

### Assertions
This IP:
 * is based on following [pull request] (https://github.com/DILCISBoard/E-ARK-CSIP/blob/1c1e4ee22936d2f83a8aa2ac8b5ff27a66a21965/specification/implementation/structure/folders/index.md).



Physical Package Structure
--------------------------
The IP physical structure contains a single representation and consists of the
mandatory files and folders shown below:
```
root/
  |
  |- METS.xml
  |- metadata/
       |
       |- preservation/
       |- descriptive/
  |- representations/
       |
       |- rep1/
            |
            |- METS.xml/
            |- data/
            |- metadata/
  |- schemas/
  |- documentation/


```
This structure includes all the files and folders that are described in following requirements.

- [CSIPSTR1](https://github.com/DILCISBoard/E-ARK-CSIP/blob/1c1e4ee22936d2f83a8aa2ac8b5ff27a66a21965/specification/implementation/structure/folders/index.md)
  IP MUST be included in a single physical folder;
- [CSIPSTR4](https://github.com/DILCISBoard/E-ARK-CSIP/blob/1c1e4ee22936d2f83a8aa2ac8b5ff27a66a21965/specification/implementation/structure/folders/index.md)
  IP root folder MUST include a metadata file named `METS.xml`;
- [CSIPSTR5](https://github.com/DILCISBoard/E-ARK-CSIP/blob/1c1e4ee22936d2f83a8aa2ac8b5ff27a66a21965/specification/implementation/structure/folders/index.md)
  IP root folder SHOULD include a folder named `metadata`;
- [CSIPSTR6](https://github.com/DILCISBoard/E-ARK-CSIP/blob/1c1e4ee22936d2f83a8aa2ac8b5ff27a66a21965/specification/implementation/structure/folders/index.md)
  If preservation metadata are available, they SHOULD be included in sub-folder `preservation`;
- [CSIPSTR7](https://github.com/DILCISBoard/E-ARK-CSIP/blob/1c1e4ee22936d2f83a8aa2ac8b5ff27a66a21965/specification/implementation/structure/folders/index.md)
  If descriptive metadata are available, they SHOULD be included in sub-folder `descriptive`;
- [CSIPSTR9](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/structure/#CSIPSTR9)
  IP root folder SHOULD include a folder named `representations`;
- [CSIPSTR10](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/structure/#CSIPSTR10)
  `Representations` folder SHOULD include a folder for each representation;
- [CSIPSTR11](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/structure/#CSIPSTR11)
 `Representation` folder SHOULD include a folder `data`;
- [CSIPSTR12](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/structure/#CSIPSTR11)
  `Representation` folder SHOULD include a metadata file named `METS.xml`;
- [CSIPSTR13](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/structure/#CSIPSTR11)
  `Representation` folder SHOULD include a folder `metadata`;
- [CSIPSTR15](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/structure/#CSIPSTR11)
  Schema documents SHOULD be placed in a sub-folder called `schemas`;
- [CSIPSTR16](https://dilcisboard.github.io/E-ARK-CSIP/specification/implementation/structure/#CSIPSTR11)
  Supplementary documentation SHOULD be placed in a sub-folder called `documentation`;
