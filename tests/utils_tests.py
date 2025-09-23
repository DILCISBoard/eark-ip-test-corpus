from pathlib import Path

from typing import Optional
from xsdata.formats.dataclass.parsers import XmlParser
from tests import case

test_case_name = "testCase.xml"

def load_test_case(path_to_test_case_directory: Path, should_throw_error_on_missing_test_case: bool) -> Optional[case.TestCase]:
    if not path_to_test_case_directory.exists() or not path_to_test_case_directory.is_dir():
        if not should_throw_error_on_missing_test_case:
            return None
        
        raise ValueError(f"{path_to_test_case_directory} is missing")
    path_to_test_case = Path(path_to_test_case_directory / test_case_name)

    if not path_to_test_case.exists() or not path_to_test_case.is_file():
        if not should_throw_error_on_missing_test_case:
            return None
        
        raise ValueError(f"{path_to_test_case} is missing")

    test_case = parse_test_case(path_to_test_case)
    if test_case.testable == case.TestCaseTestable.FALSE:
        return None
    elif test_case.testable != case.TestCaseTestable.TRUE and should_throw_error_on_missing_test_case:
        raise ValueError(f"Testable attribute is not TRUE or FALSE - have a look if this be adjusted")

    if test_case.rules is None or len(test_case.rules.rule) == 0:
        if not should_throw_error_on_missing_test_case:
            return None
        
        raise ValueError(f"Test rules are not defined")
    
    if should_throw_error_on_missing_test_case:
        for rule in test_case.rules.rule:
            for package in rule.corpus_packages.package:
                if package.is_implemented == case.PackageIsImplemented.FALSE:
                    raise ValueError(f"Package {package.name} is not implemented")
    
    return test_case

def parse_test_case(path_to_test_case: Path) -> case.TestCase:
    return XmlParser().from_path(path_to_test_case, case.TestCase)

def is_testable(test_case: case.TestCase) -> bool:
    return test_case.testable == case.TestCaseTestable.TRUE

def get_path_to_package(path_element: case.Path, path_to_test_case_directory: Path) -> Path:
    path = Path(path_to_test_case_directory / path_element.value)
    
    assert path.is_dir() or path.is_file(), "Path to package is invalid"
    return path
