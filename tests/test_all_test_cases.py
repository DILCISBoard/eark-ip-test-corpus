import pytest
import itertools
from pathlib import Path
from typing import Optional

from tests.utils_tests import load_test_case, is_testable
from tests.eark_validator_tests import eark_validator_test_from_test_case

@pytest.fixture
def should_throw_error_on_missing_test_cases(request) -> bool:
    return request.config.getoption("--errorOnMissing")

tests_path = Path(__file__).parent
csip_path = Path('../corpus/CSIP')
csipstr_path = Path('../corpus/CSIP')
dip_path = Path('../corpus/DIP')
sip_path = Path('../corpus/SIP')

@pytest.mark.parametrize("requirement_number", itertools.chain(range(1, 87), range(88, 115), range(116, 120)))
def test_CSIP(requirement_number: int, should_throw_error_on_missing_test_cases: bool):
    path = tests_path / csip_path / ("CSIP" + str(requirement_number))
    perform_test(path, should_throw_error_on_missing_test_cases)

@pytest.mark.parametrize("requirement_number", range(1, 17))
def test_CSIPSTR(requirement_number: int, should_throw_error_on_missing_test_cases: bool):
    path = tests_path / csipstr_path / ("CSIPSTR" + str(requirement_number))
    perform_test(path, should_throw_error_on_missing_test_cases)

@pytest.mark.parametrize("requirement_number", range(1, 5))
def test_DIP(requirement_number: int, should_throw_error_on_missing_test_cases: bool):
    path = tests_path / dip_path / ("DIP" + str(requirement_number))
    perform_test(path, should_throw_error_on_missing_test_cases, "DIP")

@pytest.mark.parametrize("requirement_number", range(1, 36))
def test_SIP(requirement_number: int, should_throw_error_on_missing_test_cases: bool):
    path = tests_path / sip_path / ("SIP" + str(requirement_number))
    perform_test(path, should_throw_error_on_missing_test_cases, "SIP")

def perform_test(pathToDir: Path, should_throw_error_on_missing_test_case: bool, specification_type: Optional[str] = None):
    testCase = load_test_case(pathToDir, should_throw_error_on_missing_test_case)
    if testCase and is_testable(testCase):
        eark_validator_test_from_test_case(testCase, pathToDir, specification_type)

"""
def test_single_test_case(should_throw_error_on_missing_test_cases: bool):
    path = tests_path / Path("../corpus/CSIP/CSIP1")
    perform_test(path, should_throw_error_on_missing_test_cases)
"""