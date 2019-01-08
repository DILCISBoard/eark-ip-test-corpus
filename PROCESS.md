Process for Creation and Review of Test Cases and Corpus Packages
=================================================================

TODO
----
- [ ] Further details of the `integration` branch automatic QA and merge to the release branch.
- [ ] Git pre-commits for XML indents and validation, plus...
- [ ] Requirements for sign off
- [ ] Handling related / identical / redundant tests, e.g. CSIPSTR2 and CSIP2
- [ ] Current test case identifier scheme won't handle multiple test cases for a single requirement

GitHub reference
----------------

### Branches

#### Permanent branches
For now we'll maintain the following permanent branches in the corpus repo:

- `master` should contain the latest release version of the test cases and corpus, obviously we have no current release. For now we'll use this to control editorial policy, only test case and corpus package sets that have been externally reviewed by the A2 group, will be merged here from the `csip/rel/2.0-draft` branch.
- `csip/rel/2.0-draft` This is the internally reviewed current working version and it's name has been chosen to match the current draft CSIP specification version we're working to.
- `integration` the branch against which all Pull Requests are made, it's used to ensure that the integrated whole works, i.e. package creation, documentation generation, etc. PRs merged here will have been reviewed by the A3 team in isolation, this branch ensures tests the automation steps on the merged whole. Once this QA has passed, integration can be merged to the `csip/rel/2.0-draft` branch.

#### Working branches
In addition to the permanent branches the team will create working branches when producing test cases and corpus packages. These should follow a hierarchical naming convention, `<spec-name>/<spec-part>/<req-id>`. We don't need to be prescriptive about the value of `<spec-part>`, the intention is too allow logical grouping without agonising over classification. These branches will track all of the work done on a particular requirement from test case definition through corpus package creation and review. Once a test case branch has been reviewed by the A2 group and merged to master the working branch can be deleted.

### Labels
We use a small set of GitHub labels to categorise and track our Issues and Pull Requests. An up to date list of labels with explanations and colours is available [on the project Issue Tracker on GitHub](https://github.com/DILCISBoard/eark-ip-test-corpus/labels).

Process
-------
1. **Issue Submission:** The creation of a new test case is initiated by the submission of a new GitHub issue, ideally using the [test case template](https://github.com/DILCISBoard/eark-ip-test-corpus/issues/new?template=test-case.md). Internally the A3 and A2 teams should always use the template, it's possible that external submitters might not use the template.

2. **Test Case Backlog:** Issues will be triaged regularly by the A3 team. Test case issues will be given a `test case` label and any missing details in the template will be populated. The issue is now given a standard name. This process will tie the test case to a specific to requirement, by ID, so we can track and report coverage. These triaged test cases will then wait assignment to a member of the A3 team to work on them. This list of unassigned test cases is the "Test Case Backlog".

3. **Work in Progress:** Test cases from the backlog will be assigned to a member of the A3 team, at this stage they become "Work in Progress", which effectively measures our open activity. The team should work hard to ensure that the list of "in progress" test cases does not become too large, which suggests we're struggling to complete and sign off corpus cases. Work assignment is the responsibility of the A3 lead but it will generally be carried out as a group in the team meetings.

4. **Test Case Definition:** The test case assignee now creates a new branch on GitHub for the test case using the [working branch convention above](#working-branches). All of the work on the test case XML definition should be done in this branch. They then consult the specification and create a new folder in the corpus project tree if necessary. A full XML description of the test case is created, where the case is decomposed into individual validation rules. Within a rule there is space to define the corpus packages necessary to test the rule, though these needn't be complete at this stage. A documented XML template for test cases is [available here](./test-case.xml). Once the XML test case description is fully populated, excepting the corpus package elements, a GitHub pull request is prepared for review, this is also given the `test case` label and tied to the Issue via a [GitHub Flavoured Markdown reference](https://help.github.com/articles/autolinked-references-and-urls/#issues-and-pull-requests) in the Pull Request description.

5. **Test Case Review:** The full XML description is now reviewed by another member of the A3 corpus group. This is done using the GitHub review interface. For many Straightforward test cases this may be enough and the test case PR can be merged. If there are problems interpreting the requirement then an issue should be raised on the [specification project tracker](https://github.com/DILCISBoard/E-ARK-CSIP/issues). The requirement can then be discussed by the A2 group and a resolution found. If there's a problem devising suitable corpus packages then the case should be circulated to the A3 Team for review and discussed in the weekly A3 meeting. If the A3 team can't devise a suitable test strategy/suitable corpus packages for a test case then they should:
  - label the requirement as "invalid" to indicate that we don't believe that a valid test case can be derived from the requirement;
  - change the `testable` attribute in the `test-case.xml` document to `FALSE`; and
  - raise an issue on the the [specification project tracker](https://github.com/DILCISBoard/E-ARK-CSIP/issues) that links to the test case and explains the problem.

  Again, these will be discussed in the weekly A2 meetings. If they're deemed untestable then the the test case PR will be merged and the test case issue closed. The `testable="FALSE"` attribute will mark the test case as complete but untestable for reporting purposes.

  All other test cases, that is all that are judged testable, now go forward to corpus creation. The Pull Request used to review the test case XML is merged to `integration` and the branch is now used for corpus package creation. The original, still open, issue with the `test case` label is given an additional `corpus package` label.

6. **Corpus Package Creation:** A member of the A3 team now takes the defined XML test case and starts to create suitable test packages for the validation rules, including pass and fail cases. Details of the test packages created are added to the test case XML. Once they're satisfied that they've provided sufficient test packages to exercise the requirement another pull request is created from the branch. This time the PR is given the `corpus package` label and again review is requested from an A3 team member. If they're happy then the PR is given the `ready` tag. These PRs are reviewed at the A3 meetings and merged into the `integration` branch when approved. The `ready` tag is not removed but another `ready` label is given to the original issue. Following successful automated QA of the integration branch the branch is then pushed to the `csip/rel/2.0-draft` branch.

7. **External Review:** At this stage there are the following elements to a test case and accompanying corpus packages:
  - the original issue opened to initiate the test case with the following properties:
    + a label `test case`;
    + a label `corpus package`;
    + a label `ready`; and
    + an assignee
  - a now closed pull request with the following properties:
    + a label `test case`;
    + an assignee;
  - a now closed pull request with the following properties:
    + a label `corpus package`;
    + a label `ready`; and
    + an assignee;

This set provides an audit trail for individual test cases and accompanying corpus packages. Review by the A2 group will normally be done at a higher level, e.g. the difference between the `csip/rel/2.0-draft` branch and the master branch. The more detailed audit trail can be consulted when review by the A2 team becomes automatic. The final sign off by the A2 team results in a merge to the `master` branch and the closing of the original issue.
