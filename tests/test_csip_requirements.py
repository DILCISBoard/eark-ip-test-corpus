from pathlib import Path

from tests.eark_validator_tests import validate_package_with_eark_validator, compare_output_with_expected_value

tests_path = Path(__file__).parent

def test_csip_1_1():
    path_to_package = tests_path / Path("../corpus/CSIP/CSIP1/valid/minimal_IP_with_1_representation")
    requirement_id = 'CSIP1'
    should_contains_requirement = False

    output = validate_package_with_eark_validator(path_to_package)
    compare_output_with_expected_value(output, should_contains_requirement, requirement_id)

def test_csip_1_2():
    path_to_package = tests_path / Path("../corpus/CSIP/CSIP1/invalid/mets-xml_mets_OBJID_attribute_not_exist")
    requirement_id = 'CSIP1'
    should_contains_requirement = True

    output = validate_package_with_eark_validator(path_to_package)
    compare_output_with_expected_value(output, should_contains_requirement, requirement_id)

def test_csip_1_3():
    path_to_package = tests_path / Path("../corpus/CSIP/CSIP1/invalid/mets-xml_mets_OBJID_attribute_value_empty")
    requirement_id = 'CSIP1'
    should_contains_requirement = True

    output = validate_package_with_eark_validator(path_to_package)
    compare_output_with_expected_value(output, should_contains_requirement, requirement_id)

def test_csip_1_4():
    path_to_package = tests_path / Path("../corpus/CSIP/CSIP1/invalid/root_mets_file_mets-xml_mets_OBJID_not_equal_to_package_ID")
    requirement_id = 'CSIP1'
    should_contains_requirement = True

    output = validate_package_with_eark_validator(path_to_package)
    compare_output_with_expected_value(output, should_contains_requirement, requirement_id)

def test_csip_1_5():
    path_to_package = tests_path / Path("../corpus/CSIP/CSIP1/invalid/rep_mets_file_mets-xml_mets_OBJID_not_equal_to_rep_ID")
    requirement_id = 'CSIP1'
    should_contains_requirement = True

    output = validate_package_with_eark_validator(path_to_package)
    compare_output_with_expected_value(output, should_contains_requirement, requirement_id)

def test_csip_2_1():
    path_to_package = tests_path / Path("../corpus/CSIP/CSIP2/valid/minimal_IP_with_1_representation")
    requirement_id = 'CSIP2'
    should_contains_requirement = False

    output = validate_package_with_eark_validator(path_to_package)
    compare_output_with_expected_value(output, should_contains_requirement, requirement_id)

def test_csip_2_2():
    path_to_package = tests_path / Path("../corpus/CSIP/CSIP2/invalid/mets-xml_mets_TYPE_attribute_not_exist")
    requirement_id = 'CSIP2'
    should_contains_requirement = True

    output = validate_package_with_eark_validator(path_to_package)
    compare_output_with_expected_value(output, should_contains_requirement, requirement_id)

def test_csip_2_3():
    path_to_package = tests_path / Path("../corpus/CSIP/CSIP2/invalid/mets-xml_mets_TYPE_attribute_value_incorrect")
    requirement_id = 'CSIP2'
    should_contains_requirement = True

    output = validate_package_with_eark_validator(path_to_package)
    compare_output_with_expected_value(output, should_contains_requirement, requirement_id)

def test_csip_2_4():
    path_to_package = tests_path / Path("../corpus/CSIP/CSIP2/invalid/mets-xml_mets_TYPE_attribute_value_OTHER_and_csip-OTHERTYPE_attribute_not_exist")
    requirement_id = 'CSIP2'
    should_contains_requirement = True

    output = validate_package_with_eark_validator(path_to_package)
    compare_output_with_expected_value(output, should_contains_requirement, requirement_id)

def test_csip_2_5():
    path_to_package = tests_path / Path("../corpus/CSIP/CSIP2/invalid/mets-xml_mets_TYPE_attribute_value_OTHER_and_csip-OTHERTYPE_attribute_has_no_value")
    requirement_id = 'CSIP2'
    should_contains_requirement = True

    output = validate_package_with_eark_validator(path_to_package)
    compare_output_with_expected_value(output, should_contains_requirement, requirement_id)
