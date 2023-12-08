"""Run the functions that are a part of an assessment."""

import sys
from typing import Any, List

import assessment
from evalugator import constants, execute

FILE_NAME = constants.files.People_File_Name


def do_runs() -> List[Any]:
    """Run all of the sub-parts of the assessment."""
    # execute all of the run functions defined in this module
    # and then return their output in a list of strings,
    # with each entry in the list the output of one run
    run_output: List[str] = []
    run_output = execute.execute_by_name_filter(
        constants.evalugator.Run_Module, constants.evalugator.Run_Filter
    )
    return run_output


def run_part_one():
    """Run the function defined by part-one of the assessment."""
    separator = constants.markers.Separator
    part_one_output = assessment.read_file(FILE_NAME)
    # calculate the number of rows in the output
    row_count = len(part_one_output)
    # calculate the number of columns in the output
    column_count = len(part_one_output[0])
    # return the number of rows and columns inside of the list of lists
    return str(row_count) + separator + str(column_count)


def run_part_two():
    """Run the function defined by part-two of the assessment."""
    # note that this run uses artificial data instead of the CSV file's contents
    separator = constants.markers.Separator
    # should output three rows
    part_two_output_zero = assessment.count_rows([["1", "2"], ["a", "b"], ["c", "d"]])
    # should output two rows
    part_two_output_one = assessment.count_rows([["a", "b"], ["c", "d"]])
    # should output two rows
    part_two_output_two = assessment.count_rows([["a", "b", "c"], ["d", "e", "f"]])
    # should output one row
    part_two_output_three = assessment.count_rows([["a", "b", "c", "d"]])
    # should output one row
    part_two_output_four = assessment.count_rows([[]])
    # should output zero rows
    part_two_output_four = assessment.count_rows([])
    # generate a 5 x 5 list of lists and use it as input to the row counter
    part_two_output_five_matrix = assessment.generate_square_matrix(5)
    # should output five rows
    part_two_output_five = assessment.count_rows(part_two_output_five_matrix)
    # return a single line of output that is separated by the separator
    return (
        str(part_two_output_zero)
        + separator
        + str(part_two_output_one)
        + separator
        + str(part_two_output_two)
        + separator
        + str(part_two_output_three)
        + separator
        + str(part_two_output_four)
        + separator
        + str(part_two_output_five)
    )


def run_part_three():
    """Run the function defined by part-three of the assessment."""
    # note that this run uses artificial data instead of the CSV file's contents
    separator = constants.markers.Separator
    # should output four columns
    part_three_output_zero = assessment.count_columns(
        [["1", "2", "3"], ["a", "b", "c", "4"], ["c", "d", "3"]]
    )
    # should output three columns
    part_three_output_one = assessment.count_columns([["a", "b"], ["c", "d", "3"]])
    # should output two columns
    part_three_output_two = assessment.count_columns([["a"], ["d", "e"]])
    # should output one column
    part_three_output_three = assessment.count_columns([["a"], ["a"]])
    # should output zero columns
    part_three_output_four = assessment.count_columns([[], [], []])
    # return a single line of output that is separated by the separator
    return (
        str(part_three_output_zero)
        + separator
        + str(part_three_output_one)
        + separator
        + str(part_three_output_two)
        + separator
        + str(part_three_output_three)
        + separator
        + str(part_three_output_four)
    )


def run_part_four():
    """Run the function defined by part-four of the assessment."""
    separator = constants.markers.Separator
    # synthetic data: create the list of lists that will be used for testing
    synthetic_records = [
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
    # real data: create the list of lists that will be used for testing
    file_records = assessment.read_file(FILE_NAME)
    # synthetic data: filter the records using the specified column index and column value
    filtered_synthetic_records = assessment.filter_rows_by_column_value(
        synthetic_records, constants.columns.Synthetic_Index, "2"
    )
    # real data: filter the records using the specified column index and column
    # value; make sure to use the provided trace function that should not crash
    sys.settrace(assessment.trace_lines)
    filtered_real_records = assessment.filter_rows_by_column_value(
        file_records, constants.columns.Email_Address, "example.org"
    )
    # disable the use of the trace function and extract the function trace
    sys.settrace(None)
    execution_trace = assessment.executed_lines
    # set the found_trace variable to true if the execution trace
    # variable is not empty; meaning some trace content was recorded
    found_trace = bool(execution_trace)
    # return the length of the the synthetic and real filtered records,
    # separated by the separator, ultimately following this format:
    # <length of synthetic filtered records> / <length of real filtered records>
    return (
        str(len(filtered_synthetic_records))
        + separator
        + str(len(filtered_real_records))
        + separator
        + str(found_trace)
    )


def run_part_five():
    """Run the function defined by part-five of the assessment."""
    separator = constants.markers.Separator
    # synthetic data: create the list of lists that will be used for testing
    synthetic_records = [
        ["1", "2", "3"],
        ["a", "b2", "c", "4"],
        ["c", "d", "3"],
        ["a", "b"],
        ["c", "2", "3"],
        ["a"],
        ["d", "e"],
        ["a"],
        ["a"],
        [],
        [],
        [],
    ]
    # real data: create the list of lists that will be used for testing
    file_records = assessment.read_file(FILE_NAME)
    # synthetic data: filter the records using the specified column index and column value
    synthetic_records_tuple = assessment.find_most_common_column_value(
        synthetic_records, constants.columns.Synthetic_Index
    )
    # real data: filter the records using the specified column index and column value
    real_records_tuple = assessment.find_most_common_column_value(
        file_records, constants.columns.Occupation
    )
    # return value and the count of the value for the synthetic and real records,
    # separated by the separator, ultimately following this format:
    # (<synthetic value>, <synthetic count>) / (<real value>, <real count>)
    return str(synthetic_records_tuple) + separator + str(real_records_tuple)
