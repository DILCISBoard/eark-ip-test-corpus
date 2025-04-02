from pathlib import Path

from xsdata.formats.dataclass.parsers import XmlParser
from tests import case

test_case_name = "testCase.xml"

def load_test_case(path_to_test_case_directory: Path, should_throw_error_on_missing_test_case: bool) -> case.TestCase:
    path_to_test_case = get_test_case_path(path_to_test_case_directory)

    if not path_to_test_case.is_file():
        if not should_throw_error_on_missing_test_case:
            return
        
        raise ValueError(f"{path_to_test_case} is missing")

    test_case = parse_test_case(path_to_test_case)

    if is_testable(test_case) and (test_case.rules is None or len(test_case.rules.rule) == 0):
        if not should_throw_error_on_missing_test_case:
            return
        
        raise ValueError(f"Test rules are not defined")

    return test_case

def get_test_case_path(path_to_test_case_directory: Path) -> Path:    
    assert path_to_test_case_directory.is_dir(), f"{path_to_test_case_directory} is missing"
    path_to_test_case = Path(path_to_test_case_directory / test_case_name)

    return path_to_test_case

def parse_test_case(path_to_test_case: Path) -> case.TestCase:
    return XmlParser().from_path(path_to_test_case, case.TestCase)

def is_testable(test_case: case.TestCase) -> bool:
    return test_case.testable == case.TestCaseTestable.TRUE

def get_path_to_package(path_element: case.Path, path_to_test_case_directory: Path) -> Path:
    path = Path(path_to_test_case_directory / path_element.value)
    
    assert path.is_dir() or path.is_file(), "Path to package is invalid"
    return path
