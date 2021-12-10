# Test case list
""" => Add (int & float)
- 1 + 2 = 3
- -1 + 1 = 0
- -1 -2 = -3
- 1 + 0 = 1
- 1.2 + 2 = 3.2
- 1.2 + 'a' => raise TypeError
- 'a' + 'b' => raise TypeError
"""
from unittest.mock import patch

import pytest

from math_operators import add, compute


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (-1, -2, -3),
    (1, 0, 1),
    (1.2, 2, 3.2),
])
def test_add_when_arguments_are_of_the_correct_type(a, b, expected):
    # when
    result = add(a, b)

    # then
    assert result == expected


def test_add_should_raise_type_error_when_the_first_argument_is_a_string_old():
    # given
    a, b = "b", 1

    # when
    try:
        result = add(a, b)
        assert False
    except TypeError:
        assert True


@pytest.mark.parametrize("a, b", [("b", 1), ("b", "a")])
def test_add_should_raise_type_error_when_arguments_are_of_string_type(a, b):
    # when
    with pytest.raises(TypeError):
        _ = add(a, b)


# Compute
""" Test case list
* Compute: a, b => c <- add(a, b), d <- multiply(a, c), return d 
- call add with a, b
- call multiply with a, c
- call add & multiple in the correct order
- return d
- compute should report exception if raised and not catch it
"""

TESTED_MODULE = "math_operators"


def test_compute_should_call_add_with_the_correct_arguments_ugly_way():
    # given
    a, b = 3, 2

    # when
    with patch(f"{TESTED_MODULE}.add") as add_mock:
        compute(1, 2)
        add_mock.assert_called_once_with(1, 2)


@patch(f"{TESTED_MODULE}.add")
def test_compute_should_call_add_with_the_correct_arguments(add_mock):
    # when
    compute(1, 2)

    # then
    add_mock.assert_called_once_with(1, 2)


@patch(f"{TESTED_MODULE}.add", return_value=3)
@patch(f"{TESTED_MODULE}.multiply")
def test_compute_should_call_multiply_with_the_correct_arguments(multiply_mock, _):
    # when
    compute(1, 2)

    # then
    multiply_mock.assert_called_once_with(1, 3)


@patch(f"{TESTED_MODULE}.add", return_value=3)
@patch(f"{TESTED_MODULE}.multiply", return_value=3)
def test_compute_should_return_the_result_of_multiply(multiply_mock, add_mock):
    # when
    result = compute(1, 2)

    # then
    assert result == 3


## TODO:
"""
- test orchestrator call order
- mock function from package
- mock function from package in a specific file
"""
