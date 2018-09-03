# Test case description template

Test cases should be described using the following structure and markdown.

&#35; Short description  
&ast;&ast;ID:&ast;&ast; Unique identifier of the test case  
&ast;&ast;Rule:&ast;&ast; Detailed description of the rule  
&ast;&ast;Reference:&ast;&ast; Reference or link to the rule in CS  
&ast;&ast;Referenced CSIP version:&ast;&ast; Commit ID and date of CSIP  
&ast;&ast;Dependencies:&ast;&ast; Dependencies with other test cases (if exist)  
&ast;&ast;Comments:&ast;&ast; Comments about the test case (if exist)

&#45;&#45;&#45;

&ast;&ast;Violation ID:&ast;&ast; Unique identifier of the violation  
&ast;&ast;Violation description:&ast;&ast; Description of the violation  
&ast;&ast;Error level:&ast;&ast; One of `[INFO | WARNING | ERROR]`  
&ast;&ast;Error message:&ast;&ast; Error message for this violation  
&ast;&ast;Minimal test IP structure:&ast;&ast; Description of the IP that implements this violation  

---
Notes:
* All values of description elements can be multiple paragraphs
* Each violation should have its own &ast;&ast;Violation:&ast;&ast; section