import pytest
import itertools
from pathlib import Path

from tests.utils_tests import load_test_case, is_testable
from tests.eark_validator_tests import eark_validator_test_from_test_case

@pytest.fixture
def should_throw_error_on_missing_test_cases(request):
    return request.config.getoption("--errorOnMissing")

tests_path = Path(__file__).parent
csip_path = Path('../corpus/CSIP')
csipstr_path = Path('../corpus/CSIP')
dip_path = Path('../corpus/DIP')
sip_path = Path('../corpus/SIP')

@pytest.mark.parametrize("requirement_number", itertools.chain(range(1, 87), range(88, 115), range(116, 120)))
def test_CSIP(requirement_number: int):
    path = tests_path / csip_path / ("CSIP" + str(requirement_number))
    perform_test(path)

@pytest.mark.parametrize("requirement_number", range(1, 17))
def test_CSIPSTR(requirement_number: int):
    path = tests_path / csipstr_path / ("CSIPSTR" + str(requirement_number))
    perform_test(path)

@pytest.mark.parametrize("requirement_number", range(1, 5))
def test_DIP(requirement_number: int):
    path = tests_path / dip_path / ("DIP" + str(requirement_number))
    perform_test(path)

@pytest.mark.parametrize("requirement_number", range(1, 36))
def test_SIP(requirement_number: int):
    path = tests_path / sip_path / ("SIP" + str(requirement_number))
    perform_test(path)

def perform_test(pathToDir: Path):
    testCase = load_test_case(pathToDir, should_throw_error_on_missing_test_cases)
    if testCase and is_testable(testCase):
        eark_validator_test_from_test_case(testCase, pathToDir)

"""
def test_single_test_case():
    path = tests_path / Path("../corpus/CSIP/CSIP1")
    perform_test(path)
"""