import pytest

input_value = (input("Enter a string: "))

def unitesting(string):
    palin = "".join(reversed(string))
    return palin

def test_answer():
    # for n in ["xox", "malayalam", "rishab"]:
    #     test_plai = n
    #     assert unitesting(test_plai) == n
    assert unitesting(input_value) == input_value, "should be same string"
