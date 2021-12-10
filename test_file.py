from unittest.mock import MagicMock, patch
import file

"""
def test_f_calls_sum():
    # Given
    sum_mock = MagicMock()
    file.sum = sum_mock

    # When
    file.f(1, 2)

    # Then
    sum_mock.assert_called_once_with(1, 2)
    #assert sum_mock.call_count == 2
"""


def test_f_calls_sum_patch():
    # Given
    with patch('file.sum') as sum_mock:
        # When
        file.f(1, 2)

    # Then
    sum_mock.assert_called_once_with(1, 2)
    # assert sum_mock.call_count == 2


"""
def test_f_calls_square_with_correct_args():
    # Given
    sum_mock = MagicMock(); file.sum = sum_mock
    square_mock = MagicMock(); file.square = square_mock

    # When
    file.f(1, 2)

    # Then
    square_mock.assert_called_once_with(3) 
"""


def test_f_calls_square_with_correct_args_patch():
    # Given
    with patch('file.sum', return_value=3) as sum_mock:
        with patch('file.square') as square_mock:
            # When
            file.f(1, 2)

    # Then
    square_mock.assert_called_once_with(3)


@patch('file.sum', return_value=3)
@patch('file.square')
def test_f_calls_square_with_correct_args_patch_decorator(square_mock, sum_mock):
    # When
    file.f(1, 2)

    # Then
    square_mock.assert_called_once_with(3)


def test_sum_should_return_3_when_given_1_and_2_as_parameters():
    # when
    result = file.sum(1, 2)

    # then
    assert result == 3


def test_square_should_return_9_when_given_3_as_parameter():
    # when
    result = file.square(3)

    # then
    assert result == 9


@patch('file.sum', return_value=4)
@patch('file.square', return_value=16)
def test_f_orchestrator(square_mock, sum_mock):
    # when
    result = file.f(2, 2)

    # then
    sum_mock.assert_called_once_with(2, 2)
    square_mock.assert_called_once_with(4)
    assert result == 16
