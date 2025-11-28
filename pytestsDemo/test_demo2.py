import pytest


def test_secondProgram(setup):
    print("Good Evening")

@pytest.mark.smoke
@pytest.mark.skip

def test_maths(setup):
    a = 4
    b = 6
    assert a+b == 6, "Addition did not match"