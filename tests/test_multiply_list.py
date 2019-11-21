import pytest
from python_exercises import multiply_list

def test_multiply_list():
    assert multiply_list.product([6]) == 6


def test_multiply_list():
    assert multiply_list.product([6,6]) == 36
    


