import xml.etree.ElementTree as ET 
import subprocess
import os 
import json
import sys

if len(sys.argv) == 1:
    print("Path(s) to testCase.xml file(s) must be specified!")
    exit(1)

total_test_cases = 0
total_rules = 0
total_validations = 0
failed_validations = 0
failed_parsings = 0
misssing_packages = 0
skipped_validations = 0
inconsistent_outputs = 0
correct_valid_validatons = 0
correct_invalid_validatons = 0

for test_case_path in sys.argv[1:]:
    total_test_cases += 1
    dir_path = os.path.dirname(test_case_path)

    try:
        tree = ET.parse(test_case_path)
    except Exception as e:
        failed_parsings += 1
        print(f"Parsing failed: {test_case_path}")
        print(e)
        continue

    root = tree.getroot()
    testcase_id = root.find('id').get('requirementId')

    if root.get('testable') != 'TRUE':
        print(f"{test_case_path} is not testable")
        skipped_validations += 1
        continue

    for rule in root.iter('rule'):
        total_rules += 1
        rule_id = rule.get('id')

        for package in rule.find('corpusPackages'):
            total_validations += 1

            relative_path = package.find('path').text
            if relative_path == '' or relative_path is None:
                print(f'Path in {test_case_path}, rule id: {rule_id} is misssing.')
                misssing_packages += 1
                continue

            package_path = os.path.join(dir_path, relative_path)

            try:
                jsonText = subprocess.check_output(['eark-validator', package_path], text=True).splitlines()[1]
                data = json.loads(jsonText)
                schematron_results = data['metadata']['schematron_results']
                if package.get('isValid') == 'TRUE':
                    if len(schematron_results) != 0:
                        print(f"Package {package_path} should be valid but output contains validation message.")
                        inconsistent_outputs += 1
                    else:
                        correct_valid_validatons += 1
                else:
                    if any(x['rule_id'] == testcase_id for x in schematron_results):
                        correct_invalid_validatons += 1
                    else:
                        print(f"Package {package_path} should contains validation message described in testCase.xml.")
                        inconsistent_outputs += 1

            except Exception as e: 
                failed_validations += 1
                print(f"Validation failed: {package_path}")
                print(e)
                
print()
print(f"Tried to validate {total_validations} packages from {total_rules} rules from {total_test_cases} test cases.")
print(f"{correct_valid_validatons} validations gave output that matches with expected valid value from testCase.xml")
print(f"{correct_invalid_validatons} validations gave output that matches with expected invalid value from testCase.xml")
if failed_validations != 0:
    print(f"{failed_validations} validations failed.")
if failed_parsings != 0:
    print(f"{failed_parsings} testCase.xml parsings failed.")
if skipped_validations != 0:
    print(f"{skipped_validations} test cases were skipped due to testable attribue not set to 'TRUE'.")
if misssing_packages != 0:
    print(f"{misssing_packages} validations were skipped due to missing path to package.")
if inconsistent_outputs != 0:
    print(f"{inconsistent_outputs} validations gave output that doesn't match with expected value from testCase.xml.")