#!/usr/bin/env bash
##
# author Carl Wilson carl@openpreservation.org
#
# Test case runner for E-ARK IP validation of test packages and returns:
#
#  0 If succeeds
# Setup:
#  - requires git
#  - python
#  - XML tools
#  - CLI Python validator

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export SCRIPT_DIR

# Obtain current git branch name and take appropriate action:
currentBranch="$(git rev-parse --abbrev-ref HEAD)"
echo "Parsed branch:" $currentBranch
# Pick up Travis' PR branch if it exists
echo "Travis branch:" $TRAVIS_BRANCH
if [[ -v TRAVIS_BRANCH ]]; then
    currentBranch=$TRAVIS_BRANCH
fi
echo "Post Travis branch:" $currentBranch
# IF integration then test find and run all test cases
if [[ "$currentBranch" == "integration" ]]; then
  echo "Processing all test cases"
  find ./corp* -type f -iname "testcase.xml"
  # Loop through all testCase.xml files under a filtered subset and call the test case processor
else
  testCase="$(echo $currentBranch | awk -F/ '{print $NF}')"
  echo "Processing test case:" $testCase
  find . -path \*/$testCase/\* -iname testcase.xml
  # ELSE assume a single test case
  # Parse test case ID from branch
  # Locate test case file via find
  # call test case runner on single test case file
fi
# Test case processer routine:
# IF testCase@testable == FALSE (untestable)
  # Check for test corpus packages matching rule and report if test cases found
  # return
# Loop over rules for test case, for each rule
  # store rule error Level
  # Loop over rule corpusPackages, for each package:
    # Check path to see if it exists
    # pass corpus package to test runner

# Test runner:
# Call Python CLI validator on unzipped test case
# Check validation result against the expected result passed with package
# IF package result is unexpected:
  # REPORT failure and print ValidationResult and any validation messages
# ELSE IF package result is consistent
  # IF the single validation error messge matches the expected ValidationResult
    # Report success, print any messages and return
  # ELSE IF there are unexpected error messages
    # Report failure print any messages and return
