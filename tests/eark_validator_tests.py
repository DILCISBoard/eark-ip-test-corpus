from pathlib import Path
import subprocess
import json

from tests import case
from tests.utils_tests import get_path_to_package

def eark_validator_test_from_test_case(test_case: case.TestCase, path_to_test_case_directory: Path):
    version = test_case.id.version
    if version == "2.0.4":
        version = "V2.0.4"
    else:
        version = "V2.1.0"

    for rule in test_case.rules.rule:
        for package in rule.corpus_packages.package:
            if package.is_implemented == case.PackageIsImplemented.FALSE:
                continue

            path_to_package = get_path_to_package(package.path, path_to_test_case_directory)
            output = validate_package_with_eark_validator(path_to_package, version)

            compare_output_with_expected_value_from_test_case(output, package.is_valid, test_case.id.requirement_id, path_to_package)

def validate_package_with_eark_validator(path: Path, version: str) -> str:
    return subprocess.check_output(['eark-validator', path, "--specification_version", version], text=True)

def compare_output_with_expected_value_from_test_case(output: str, is_package_valid: case.PackageIsValid, requirement_id: str, path_to_package: Path):
    return compare_output_with_expected_value(output, not is_package_valid == case.PackageIsValid.TRUE, requirement_id, path_to_package)

def compare_output_with_expected_value(output: str, should_contains_requirement: bool, requirement_id: str, path_to_package: Path):
    json_data = json.loads(output.splitlines()[1])

    structure_results = json_data["structure"]["messages"]
    is_requirement_in_structure_results = any(result['rule_id'] == requirement_id for result in structure_results)
    
    is_structure_well_formed = json_data["structure"]["status"] == 'WellFormed'
    if not is_structure_well_formed:
        if should_contains_requirement:
            assert is_requirement_in_structure_results, f"Structure of package {path_to_package} is not well formed and validation output don't contains requirement: '{requirement_id}'"
        else:
            assert not is_requirement_in_structure_results, f"Structure of package {path_to_package} is not well formed and validation output contains requirement: '{requirement_id}'"
        return

    #Mets.xml is not valid
    if json_data['metadata']['schema_results']['status'] == 'INVALID':
        if not should_contains_requirement:
            raise Exception(f"Schema of package {path_to_package} is not valid")
        return

    schematron_results = json_data['metadata']['schematron_results']['messages']
    file_results = json_data["package"]["mets"]["file_entries"]

    is_requirement_in_schematron_results = any(result['rule_id'] == requirement_id for result in schematron_results)
    is_requirement_in_file_results = any(requirement_id in file["errors"] for file in file_results)

    if should_contains_requirement:
        assert (is_requirement_in_structure_results or is_requirement_in_schematron_results or is_requirement_in_file_results), f"Validation output of package {path_to_package} don't contains requirement: '{requirement_id}'"
    else:
        assert not (is_requirement_in_structure_results or is_requirement_in_schematron_results or is_requirement_in_file_results), f"Validation output of package {path_to_package} contains requirement: '{requirement_id}'"
