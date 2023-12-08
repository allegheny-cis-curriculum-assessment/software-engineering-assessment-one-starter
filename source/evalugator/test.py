"""Test the functions that are a part of an assessment."""

# ruff: noqa: PLR2004

from typing import Any, List

import assessment
from evalugator import constants, execute

FILE_NAME = constants.files.People_File_Name


def do_tests() -> List[Any]:
    """Test all of the sub-parts of the assessment."""
    # execute all of the test cases defined in this module
    # and then return their output in a list of strings,
    # with each entry in the list the output of one test
    test_output: List[str] = []
    test_output = execute.execute_by_name_filter(
        constants.evalugator.Test_Module, constants.evalugator.Test_Filter
    )
    return test_output


def test_part_one():
    """Test the function defined by part-one of the assessment."""
    # call the function under test
    part_one_output = assessment.read_file(FILE_NAME)
    # calculate the number of rows in the output
    row_count = len(part_one_output)
    # calculate the number of columns in the output
    column_count = len(part_one_output[0])
    try:
        # check: the number of rows in the output should be 100
        assert row_count == 100
        # check: the number of columns in the output should be 5
        assert column_count == 5
        # check: the output should be a list of lists where
        # the inner lists always contain strings
        assert (
            isinstance(part_one_output, list)
            and all(
                isinstance(x, list) and all(isinstance(y, str) for y in x)
                for x in part_one_output
            )
            is True
        )
        # all of the assertions passed
        return True
    except AssertionError:
        # at least one of the test case assertions failed
        return False


def test_part_two():
    """Test the function defined by part-two of the assessment."""
    try:
        # Test 1:
        # --> call the function under test for a list of list with four rows
        part_two_output = assessment.count_rows([["a"], ["b"], ["c"], ["d"]])
        # --> check: the output should be an integer
        assert isinstance(part_two_output, int) is True
        # --> check: confirm the correct output
        assert part_two_output == 4
        # Test 2:
        # --> call the function under test for a list of lists with five rows
        part_two_output = assessment.count_rows([["a"], ["b"], ["c"], ["d"], ["e"]])
        # --> check: the output should be an integer
        assert isinstance(part_two_output, int) is True
        # --> check: confirm the correct output
        assert part_two_output == 5
        # Test 2:
        # --> call the function under test for a list of lists with six rows
        part_two_output = assessment.count_rows([["a"], ["b"], ["c"], ["d"], ["e"]])
        # --> check: the output should be an integer
        assert isinstance(part_two_output, int) is True
        # --> check: confirm the correct output
        assert part_two_output == 5
        # --> confirm that the random generation of the list of lists works correctly
        assert assessment.count_rows(assessment.generate_square_matrix(5)) == 5
        # all of the assertions passed
        return True
    except AssertionError:
        # at least one of the test case assertions failed
        return False


def test_part_three():
    """Test the function defined by part-three of the assessment."""
    try:
        # Test 1:
        # --> call the function under test for a list of list with one column
        part_two_output = assessment.count_columns([["a"], ["b"], ["c"], ["d"]])
        # --> check: the output should be an integer
        assert isinstance(part_two_output, int) is True
        # --> check: confirm the correct output
        assert part_two_output == 1
        # Test 2:
        # --> call the function under test for a list of lists with two columns
        part_two_output = assessment.count_columns(
            [["a"], ["b"], ["c"], ["d"], ["e", "f"]]
        )
        # --> check: the output should be an integer
        assert isinstance(part_two_output, int) is True
        # --> check: confirm the correct output
        assert part_two_output == 2
        # Test 2:
        # --> call the function under test for a list of lists with three columns
        part_two_output = assessment.count_columns(
            [["a"], ["b"], ["c"], ["d", "e", "f"], ["e"]]
        )
        # --> check: the output should be an integer
        assert isinstance(part_two_output, int) is True
        # --> check: confirm the correct output
        assert part_two_output == 3
        # all of the assertions passed
        return True
    except AssertionError:
        # at least one of the test case assertions failed
        return False


def test_part_four():
    """Test the function defined by part-four of the assessment."""
    # create the list of lists that will be used for testing
    try:
        records = [
            ["1", "2", "3"],
            ["a", "b2", "c", "4"],
            ["c", "d", "3"],
            ["a", "b"],
            ["c", "d2", "3"],
            ["a"],
            ["d", "e"],
            ["a"],
            ["a"],
            [],
            [],
            [],
        ]
        # Test 1: filter column 1 for the value of "2"
        filtered_records = assessment.filter_rows_by_column_value(records, 1, "2")
        # --> check: the output should be a int value
        assert isinstance(filtered_records, list) is True
        # --> check: confirm the correct number of matching rows
        assert len(filtered_records) == 3
        # Test 2: filter column 0 for the value of "a"
        filtered_records = assessment.filter_rows_by_column_value(records, 0, "a")
        # --> check: the output should be a int value
        assert isinstance(filtered_records, list) is True
        # --> check: confirm the correct number of matching rows
        assert len(filtered_records) == 5
        # Test 3: filter column 0 for the value of "x"
        filtered_records = assessment.filter_rows_by_column_value(records, 0, "x")
        # --> check: the output should be a int value
        assert isinstance(filtered_records, list) is True
        # --> check: confirm the correct number of matching rows
        assert len(filtered_records) == 0
        # Test 4: filter column 2 for the value of "3"
        filtered_records = assessment.filter_rows_by_column_value(records, 2, "3")
        # --> check: the output should be a int value
        assert isinstance(filtered_records, list) is True
        # --> check: confirm the correct number of matching rows
        assert len(filtered_records) == 3
        # Test 5: filter column 2 for the value of "x"
        filtered_records = assessment.filter_rows_by_column_value(records, 2, "x")
        # --> check: the output should be a int value
        assert isinstance(filtered_records, list) is True
        # --> check: confirm the correct number of matching rows
        assert len(filtered_records) == 0
        return True
    except AssertionError:
        return False


def test_part_five():
    """Test the function defined by part-five of the assessment."""
    # create the list of lists that will be used for testing
    try:
        records = [
            ["1", "2", "3"],
            ["a", "b2", "c", "4"],
            ["c", "d", "3"],
            ["a", "b"],
            ["c", "b2", "3"],
            ["a"],
            ["d", "e"],
            ["a"],
            ["a"],
            [],
            [],
            [],
        ]
        # Test 1: find the most common value of the first column
        found_records_tuple = assessment.find_most_common_column_value(records, 0)
        # --> check: the output should be a tuple value
        assert isinstance(found_records_tuple, tuple) is True
        # --> check: there should be two entries in the tuple
        assert len(found_records_tuple) == 2
        # --> check: the first entry in the tuple should be a string
        # --> check: the second entry in the tuple should be an int
        assert isinstance(found_records_tuple[0], str) is True
        assert isinstance(found_records_tuple[1], int) is True
        # --> check: confirm the correct most common value
        assert found_records_tuple[0] == "a"
        # --> check: confirm the correct number of matching rows
        assert found_records_tuple[1] == 5
        # Test 2: find the most common value of the second column
        found_records_tuple = assessment.find_most_common_column_value(records, 1)
        # --> check: the output should be a tuple value
        assert isinstance(found_records_tuple, tuple) is True
        # --> check: there should be two entries in the tuple
        assert len(found_records_tuple) == 2
        # --> check: the first entry in the tuple should be a string
        # --> check: the second entry in the tuple should be an int
        assert isinstance(found_records_tuple[0], str) is True
        assert isinstance(found_records_tuple[1], int) is True
        # --> check: confirm the correct most common value
        assert found_records_tuple[0] == "b2"
        # --> check: confirm the correct number of matching rows
        assert found_records_tuple[1] == 2
        # Test 3: find the most common value of the third column
        found_records_tuple = assessment.find_most_common_column_value(records, 2)
        # --> check: the output should be a tuple value
        assert isinstance(found_records_tuple, tuple) is True
        # --> check: there should be two entries in the tuple
        assert len(found_records_tuple) == 2
        # --> check: the first entry in the tuple should be a string
        # --> check: the second entry in the tuple should be an int
        assert isinstance(found_records_tuple[0], str) is True
        assert isinstance(found_records_tuple[1], int) is True
        # --> check: confirm the correct most common value
        assert found_records_tuple[0] == "3"
        # --> check: confirm the correct number of matching rows
        assert found_records_tuple[1] == 3
        # Test 4: find the most common value of the fourth column
        found_records_tuple = assessment.find_most_common_column_value(records, 3)
        # --> check: the output should be a tuple value
        assert isinstance(found_records_tuple, tuple) is True
        # --> check: there should be two entries in the tuple
        assert len(found_records_tuple) == 2
        # --> check: the first entry in the tuple should be a string
        # --> check: the second entry in the tuple should be an int
        assert isinstance(found_records_tuple[0], str) is True
        assert isinstance(found_records_tuple[1], int) is True
        # --> check: confirm the correct most common value
        assert found_records_tuple[0] == "4"
        # --> check: confirm the correct number of matching rows
        assert found_records_tuple[1] == 1
        return True
    except AssertionError:
        return False
