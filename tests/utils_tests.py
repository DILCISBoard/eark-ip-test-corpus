from pathlib import Path

from xsdata.formats.dataclass.parsers import XmlParser
from tests import case

test_case_name = "testCase.xml"

def load_test_case(path_to_test_case_directory: Path) -> case.TestCase:
    path_to_test_case = get_test_case_path(path_to_test_case_directory)
    test_case = parse_test_case(path_to_test_case)

    if is_testable(test_case):
        check_if_rules_are_defined(test_case)

    return test_case

def get_test_case_path(path_to_test_case_directory: Path) -> Path:    
    assert path_to_test_case_directory.is_dir()
    path_to_test_case = Path(path_to_test_case_directory / test_case_name)
    assert path_to_test_case.is_file()

    return path_to_test_case

def parse_test_case(path_to_test_case: Path) -> case.TestCase:
    return XmlParser().from_path(path_to_test_case, case.TestCase)

def is_testable(test_case: case.TestCase) -> bool:
    return test_case.testable != case.TestCaseTestable.FALSE

def check_if_rules_are_defined(test_case: case.TestCase):
    assert test_case.rules is not None
    assert len(test_case.rules.rule) > 0

def get_path_to_package(path_element: case.Path, path_to_test_case_directory: Path) -> Path:
    path = Path(path_to_test_case_directory / path_element.value)
    
    assert path.is_dir() or path.is_file()
    return path
