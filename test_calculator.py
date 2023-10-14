""" Having 'test' in the prefix of the file is important. This is how pytest will know
    it is the unit test module. Also, Flake8 is used to check for PEP8 styling guidelines compliance.
    'flake8 --statistics """

## > Unit tests for the calculator library

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 0 == calculator.subtract(2, 2)
