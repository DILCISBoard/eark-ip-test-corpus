from pathlib import Path
import subprocess
import json

from tests import case
from tests.utils_tests import get_path_to_package

def eark_validator_test_from_test_case(test_case: case.TestCase, path_to_test_case_directory: Path):
    for rule in test_case.rules.rule:
        for package in rule.corpus_packages.package:
            if package.is_implemented == case.PackageIsImplemented.FALSE:
                continue

            path_to_package = get_path_to_package(package.path, path_to_test_case_directory)
            output = validate_package_with_eark_validator(path_to_package)

            compare_output_with_expected_value_from_test_case(output, package.is_valid, test_case.id.requirement_id, path_to_package)

def validate_package_with_eark_validator(path: Path) -> str:
    return subprocess.check_output(['eark-validator', path], text=True)

def compare_output_with_expected_value_from_test_case(output: str, is_package_valid: case.PackageIsValid, requirement_id: str, path_to_package: Path):
    return compare_output_with_expected_value(output, is_package_valid == case.PackageIsValid.TRUE, requirement_id, path_to_package)

def compare_output_with_expected_value(output: str, should_contains_requirement: bool, requirement_id: str, path_to_package: Path):
    json_data = json.loads(output.splitlines()[1])

    is_structure_well_formed = json_data["structure"]["status"] == 'WellFormed'
    if should_contains_requirement:
        assert is_structure_well_formed, f"Structure of package {path_to_package} is not well formed"
    else:
        if not is_structure_well_formed:
            assert any(result['rule_id'] == requirement_id for result in json_data["structure"]["messages"]), f"Structure of package {path_to_package} is not well formed and validation output don't contains requirement: '{requirement_id}'"
            return

    structure_results = json_data["structure"]["messages"]
    schematron_results = json_data['metadata']['schematron_results']['messages']
    file_results = json_data["package"]["mets"]["file_entries"]

    is_requirement_in_structure_results = any(result['rule_id'] == requirement_id for result in structure_results)
    is_requirement_in_schematron_results = any(result['rule_id'] == requirement_id for result in schematron_results)
    is_requirement_in_file_results = any(requirement_id in file["errors"] for file in file_results)

    if should_contains_requirement:
        assert not (is_requirement_in_structure_results and is_requirement_in_schematron_results and is_requirement_in_file_results), f"Validation output of package {path_to_package} don't contains requirement: '{requirement_id}'"
    else:
        assert (is_requirement_in_structure_results or is_requirement_in_schematron_results or is_requirement_in_file_results), f"Validation output of package {path_to_package} contains requirement: '{requirement_id}'"