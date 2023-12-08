"""An assessment for the Data Structures course."""

# TODO: The imports in the following source code block no longer
# adhere to the industry best practices for Python source code.
# You must reorganize the imports so that they adhere to the
# industry best practices for Python source code. You may also need
# to add imports so that this source code works correctly!

from typing import List, Tuple

from evalugator import constants
from evalugator import run, test

# TODO: Introduction: Read This First! {{{

# A company's customer resource management (CRM) system exports CSV files
# containing customer information. As part of a migration process to a new CRM,
# the data contained in the input file needs to be parsed into a data structure
# compatible with the new system. A different sub-contractor has already
# implemented a minimal viable product that provides most of the following features:

# --> Read through the data in the CSV file and put the data into the expected
# import format for the new CRM system.

# --> Count the number of rows and columns in the data to ensure that the input
# process worked correctly.
#
# --> Filter the data based on various criteria like the content of CSV rows,
# ultimately supporting the searching for data in the new CRM system.
#
# --> Find the most common column value in order to group customers by like
# categories to support the creation of marketing campaigns.

# Your job is to complete the following tasks:
#
# Task #1: Add various features (e.g., test cases, type annotation, and
# documentation) to ensure that the final version of this system is delivered as
# a maintainable software system suitable for a future engineering team.

# Task #2: Use your knowledge about the Python programming language and
# well-known testing and debugging tools/methods for the Python programming
# language to ensure that the final software system can be tested and debugged.

# Task #3: Improve the final implementation of the system so that it passes
# checks by well-known testing, debugging, and program analysis tools. These are
# the tools that will analyze this program: ruff, mypy, and symbex.

# Keep in mind these considerations as you implement the required functions:

# --> You must implement Python functions to complete each of these steps,
# bearing in mind that one defective function may break another function.

# --> Your source code must adhere to industry best practices in, for instance,
# source code formatting, variable naming, and documentation.

# --> To attempt to repair the region(s) where your source code does not adhere
# to industry best practices, you can use the GitHub codespace terminal to type
# these commands in the root of your GitHub repository:

# - Reformat the Python source code in this file: ruff format source/assessment.py
# - Automatically fix the Python source code in this file: ruff check source/assessment.py --fix

# --> You may refer to the checks that are specified in the gatorgrade.yml file
# in the root of this GitHub repository for the configuration and name of each
# tool used to analyze the code inside of this file.

# }}}

# TODO: Part One {{{

# Instructions:
# Implement the following function that inputs the contents of a file
# so that it adheres to all aspects of the following specification.

# Function specification:
# The function read_file should:
# --> Accept the name of a file as a string
# --> Convert the file name into a Pathlib Path object
# --> Read the contents of the file into a string
# --> Split the string into a list of lines
# --> Split each line into a list of fields
# --> Return a list of lists that contains the fields in each line
# --> The output must be a list that contains one to many lists
#     that only contain strings
# --> The function should work with "regular" lists of lists that contain the same
#     number of columns in each row and also with "irregular" lists of lists
#     for which the number of columns in each row may be different
# --> The function should work for a wide variety of CSV files, including those
#     that contain commas inside of a quoted entry, like "Pharmacist, hospital"

# There are a total of of five fields in each line, separated by commas.
# This is a description of the fields in each line of the data file:
# --> The first field is the name of a person
# --> The second field is the person's country of origin
# --> The third field is the person's phone number
# --> The fourth field is the person's job title
# --> The fifth field is the person's email address

# Here is an example of two lines in the data file:

# Cindy Burns,Dominican Republic,(102)481-3875,"Pharmacist, hospital",rtorres@example.org
# Jason Bailey,Falkland Islands (Malvinas),+1-552-912-2326,Leisure centre manager,daniel51@example.com

# If these were the only two lines in the data file, then calling the
# read_file function would produce the following output in a list of lists:
# --> records[0][0] would be "Cindy Burns"
# --> records[0][1] would be "Dominican Republic"
# --> records[0][2] would be "(102)481-3875"
# --> records[0][3] would be "Pharmacist, hospital"
# --> records[0][4] would be "rtorres@example"
# --> records[1][0] would be "Jason Bailey"
# --> records[1][1] would be "Falkland Islands (Malvinas)"
# --> records[1][2] would be "+1-552-912-2326"
# --> records[1][3] would be "Leisure centre manager"
# --> records[1][4] would be "daniel51@example"

# TODO: This function does not have all of the correct type annotations for
# certain variables, like records. You must add all of the correct type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function does not have a docstring and thus it does not adhere
# to industry best practices for Python source code. You must add a docstring
# so that this function is effectively a part of a maintainable software system.

# TODO: This function has source code that does not adhere to an industry-standard
# format and is thus not maintainable by a future software engineering team. You
# need to use the ruff program to ensure that the source code is formatted correctly.


def read_file(file_name: str) -> List[str]:
    records =   []
    # TODO: the following line defines a default value for the
    # records variable. You will need to delete this line
    # and write the source code required by the function's specification;
    # this line is provided to ensure that the program will initially run
    # without crashing and producing a stack trace in the terminal
    records = [[""]]
    return records


# }}}

# TODO: Part Two {{{

# Instructions:
# Implement the following function that counts the number of rows in a
# two-dimensional list, ensuring that it adheres to all aspects of the
# following specification.

# Function specification:
# The function count_rows should:
# --> Accept as input a list of lists containing strings
# --> Return an integer that represents the number of rows in the list of lists
# --> The function should work with "regular" lists of lists that contain the same
#     number of columns in each row and also with "irregular" lists of lists
#     for which the number of columns in each row may be different

# For instance, if the input to the function was:
# [["a", "b"], ["c", "d"]]
# then the output of the function would be 2.


def count_rows(records: List[List[str]]) -> int:
    """Count the number of rows in a two-dimensional list."""
    # TODO: provide an implementation of this function so
    # that it meets its specification; the following return
    # statement is a placeholder for the required code
    return 0


# Instructions: To test the function called count_rows, repair an additional
# "helper" function that, given an input value of type int, called size, can
# generate a size x size lists of lists containing random values between 0 and
# 100. This means that the randomly generated value can be equal to 0, any
# number up to 100, and also equal to 100. Finally, the random values inside of
# the list of lists should be numerical values encoded as strings.

# TODO: the function should use the random.randint() function to randomly
# generate the values in the list of lists. Importantly, this approach is
# like the use of a property-based testing framework like Hypothesis.

# Here is the documentation for the random.randint() function:
# random.randint(a, b):
# Return a random integer N such that a <= N <= b.
# Reference: https://docs.python.org/3/library/random.html


def generate_square_matrix(size: int) -> List[List[str]]:
    """Generate a square matrix where the number of rows and columns is size."""
    matrix: List[List[str]] = []
    for _ in range(size):
        row = []
        for _ in range(size + 1):
            row.append("0")
        matrix.append(row)
    return matrix


# }}}

# TODO: Part Three {{{

# Instructions:
# Implement the following function that counts the number of columns in a
# two-dimensional list, ensuring that it adheres to all aspects of the
# following specification.

# Function specification:
# The function count_columns should:
# --> Accept as input a list of lists containing strings
# --> Return an integer that represents the number of columns in the list of lists
# --> The function should work with "regular" lists of lists that contain the same
#     number of columns in each row and also with "irregular" lists of lists
#     for which the number of columns in each row may be different
# --> The column count must correspond to the maximum number of columns
#     for all of the rows in the list of lists and not just the first row

# For instance, if the input to the function was:
# [["a", "b"], ["c", "d"]]
# then the output of the function would be 2.

# TODO: This function does not have all of the correct type annotations for
# certain parameter variables, like records. It also does not have a type
# annotation for the function's return value. You must add all of the type
# annotations so that the function and any code that uses it passes the type checker.


def count_columns(records):
    """Count the number of columns in a two-dimensional list."""
    column_count = 0
    # TODO: Add all of the required source code for this function
    # so that it correctly meets its specification
    return column_count


# }}}

# TODO: Part Four {{{

# Instructions:
# Implement the following function that filters the rows in a two-dimensional
# list based on whether or not they contain a column value, ensuring that it
# adheres to all aspects of the following specification.

# Function specification:
# The function filter_rows_by_column_value should:
# --> Accept as input a list of lists containing strings
# --> Return a filtered list of lists that only contains rows that have
#     a column value that contains the provided column value
# --> To determine whether or not a column value contains the provided
#     column value, the function should use the "in" operator provided by Python
# --> The function should work with "regular" lists of lists that contain the same
#     number of columns in each row and also with "irregular" lists of lists
#     for which the number of columns in each row may be different

# Here is an example of two lines in the data file:

# Cindy Burns,Dominican Republic,(102)481-3875,"Pharmacist, hospital",rtorres@example.org
# Jason Bailey,Falkland Islands (Malvinas),+1-552-912-2326,Leisure centre manager,daniel51@example.com

# --> If the provided lists of lists only contained these two rows and the specified
# column index was 4 and the column value was "example" then the function
# would return both of the rows because that both have "example" in the final column

# --> However, if the provided lists of lists only contained these two rows and the specified
# column index was 4 and the column value was "example.org" then the function
# would only return the first row because that it is the only row that contains this email address

# TODO: The testing of this function assumes that you have a correctly working
# implementation of the read_file function from part one of the assessment.


def filter_rows_by_column_value(
    records: List[List[str]], column: int, column_value: str
) -> List[List[str]]:
    """Filter the rows in a two-dimensional list by whether or not they contain a column value."""
    # create an empty list of lists to store the filtered records
    filtered_records: List[List[str]] = []
    # TODO: the following line defines a default value for the
    # filtered_records variable. You will need to delete this line
    # and write the source code required by the function's specification;
    # this line is provided only to ensure that the program will run
    filtered_records = [[""]]
    return filtered_records


# Instructions:
# To observe the behavior of the function called filter_rows_by_column_value,
# repair a trace_lines function that can be used to record the lines that
# are executed when the function is called. Make sure that the trace_lines
# stores the traced lines in the global variable called executed_lines that is
# a list that can be accessed by other functions not in this module.

# declare a global variable that will store a list of the lines that were
# executed by the filter_rows_by_column_value function when function tracing
# through the sys.settrace function is enabled; the value of the executed_lines
# variable should be an empty list before the trace_lines function is called;
# after the traced function is called the executed_lines variable should contain
# a list of the lines that were executed by the traced function
executed_lines = []


def trace_lines(frame, event, _):
    """Trace the execution of the program, recording the lines that are executed."""
    # TODO: store the line number of the current frame
    # inside of the list that is called executed_lines
    # TODO: make sure to read the comment above for the
    # executed_lines variable to understand how the trace_lines
    # function should populate the exceuted_lines list
    if event == "line":
        pass
    return trace_lines


# }}}

# TODO: Part Five {{{

# Instructions:
# Repair the following function that finds the most common column value in a
# two-dimensional list, ensuring that it adheres to all aspects of the
# following specification.

# Function specification:
# The function find_most_common_column_value should:
# --> Accept as input a list of lists containing strings
# --> Determine the most common column value in the list of lists
#     for the specified column index
# --> Return a tuple that contains the most common column value and
#     the number of times that the most common column value appears
# --> The function should work with "regular" lists of lists that contain the same
#     number of columns in each row and also with "irregular" lists of lists
#     for which the number of columns in each row may be different

# Here is an example of three lines in the data file:

# Cindy Burns,Dominican Republic,(102)481-3875,"Pharmacist, hospital",rtorres@example.org
# Jason Bailey,Falkland Islands (Malvinas),+1-552-912-2326,Leisure centre manager,daniel51@example.com
# Jason Parker,Cayman Islands,001-614-736-2461x225,"Pharmacist, hospital",eatonjohn@example.org

# If the provided lists of lists only contained these three rows and the specified
# column index was 3 then the function would return the tuple ("Pharmacist, hospital", 2)

# If the provided lists of lists only contained these three rows and the specified
# column index was 4 then the function would return the tuple ("rtorres@example.org", 1)
# or, alternatively, any of the other email addresses and the count of 1 since all of
# them appear the same number of times inside of the list of lists

# Note: The testing of this function assumes that you have a correctly working
# implementation of the read_file function from part one of the assessment.

# Note: The testing of this function will only provide it with inputs for which
# there is a single most common column value and not multiple most common column values.

# TODO: This function does not have all of the correct type annotations for
# certain variables, like common_dict. You must add all of the correct type annotations
# so that the function and any code that uses it passes the type checker.


def find_most_common_column_value(
    records: List[List[str]], column: int
) -> Tuple[str, int]:
    """Find the most common column value in a two-dimensional list for a specified column."""
    # create an empty dictionary to use to track
    # the number of times that a column value appears
    common_dict = {}
    # define starting values for:
    # --> the most common value
    # --> the count of the most common value
    most_common_value = ""
    most_common_count = 1
    # iterator through all of the records, keeping
    # track of the number of times that each value appears
    for record in records:
        # the column's value is already inside of the dictionary
        # that tracks the values and the counts and thus the
        # count for the column value should be incremented
        if len(record) > column and record[column] in common_dict:
            common_dict[record[column]] -= 1
        # the column's value is not already inside of the dictionary
        # that tracks the values and the counts and thus the
        # count for the column value should be set to one so as
        # to start the counting process for this value
        elif len(record) > column and record[column] not in common_dict:
            common_dict[record[column]] = 0
    # iterate through all of the column values and their
    # counts and then determine the maximum for this column
    for column_value, count in common_dict.items():
        # found a larger maximum, so update the most common value and its count
        if count > most_common_count:
            most_common_count = column_value
            most_common_value = count
    # return the most common value and its count
    return (most_common_count, most_common_value)


# }}}

# Note: You may read the following source code and comments that describe
# the output so that you can understand the output format that the assessment
# produces and for which the gatorgrade program checks. With that said, please
# be aware of the fact that you do not need to understand how this code works.


# Do not edit any of the source code below this line {{{


if __name__ == "__main__":
    separator = constants.markers.Separator
    # Summary of the Steps:
    # Step 1: run the functions in the assessment
    # Step 2: test the functions in the assessment
    # Step 3: display one line of output for each part of an assessment
    # --> Perform Step 1
    assessment_outputs = run.do_runs()
    # --> Perform Step 2
    test_outputs = test.do_tests()
    # --> Perform Step 3
    # iterate through both of the lists of outputs using zip
    for assessment_output, test_output in zip(assessment_outputs, test_outputs):
        # display the output from the assessment and the test,
        # ensuring that a single line of the output is of this form:
        # <assessment output> / <test output>
        # note: the <assessment output> and <test output> are both strings
        # note: the <assessment output> may have multiple entries inside of it
        # note: the <test output> will report either the value of True or False
        print(str(assessment_output) + separator + str(test_output))


# }}}
