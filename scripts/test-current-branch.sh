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
# Pick up Travis' PR branch if it exists
if [[ -v TRAVIS_BRANCH ]]; then
    currentBranch=$TRAVIS_BRANCH
fi
# IF integration then test find and run all test cases
if [[ "$currentBranch" == "integration" ]]; then
  echo $currentBranch": processing all test cases..."
  # Loop through all testCase.xml files under a filtered subset and call the test case processor
  finalStatus=0
  while IFS= read -r -d '' CASE
  do
    ip-check -t "$CASE"
    exitStatus=$?
    if [[ $exitStatus != 0 ]]; then
      echo "FAILED CASE:" $CASE
      finalStatus=$exitStatus
    fi
  done <    <(find ./corp* -type f -iname "testcase.xml" -print0)
  echo "Exit Status:"$finalStatus
  exit $finalStatus
  # ELSE assume a single test case
else
  # Parse test case ID from branch
  testCase="$(echo $currentBranch | awk -F/ '{print $NF}')"
  echo "Processing test case:" $testCase
  # Locate test case files via find
  while IFS= read -r -d '' CASE
  do
    # call test case runner on single test case file
    ip-check -t "$CASE"
    exitStatus=$?
    echo "Exit Status:"$exitStatus
    exit $exitStatus
  done <    <(find . -path \*/${testCase^^}/\* -iname "testcase.xml" -print0)
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
