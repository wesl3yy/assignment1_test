import io
import sys
from unittest import mock
import pytest

from assignment1 import show_square

DATA1 = [
    ("case1:test1", {"output": {}, "input": []}, "", False),
    (
        "case2:test2",
        {
            "output": {"key": "value"},
            "input": [{"number": 1}, {"number": 2}, {"number": 3}, {"number": 4}],
        },
        """1
Found
4
9
16
""",
        True,
    ),
    (
        "case3:test3",
        {
            "output": {"key": "value"},
            "input": [{"number": 4}, {"number": 5}, {"number": 6}, {"number": 7}],
        },
        """16
25
36
49
""",
        True,
    ),
]


def get_data():
    return {"key": "value"}


def get_data_list():
    return [{"number": 1}, {"number": 2}, {"number": 3}, {"number": 4}]


@pytest.mark.parametrize(["case", "data", "output_params", "expect"], DATA1)
def test_show_square(case, data, output_params, expect):
    mock.patch("assignment1.get_data", return_value=data.get("output")).start()
    mock.patch("assignment1.get_data_list", return_value=data.get("input")).start()
    output = io.StringIO()
    sys.stdout = output
    return_value = show_square()
    sys.stdout = sys.__stdout__
    if len(data.get("output")) != 0:
        assert output.getvalue() == output_params
        assert return_value == expect
    else:
        assert return_value == expect
