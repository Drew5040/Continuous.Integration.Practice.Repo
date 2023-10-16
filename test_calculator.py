# Unit tests for the calculator library
# Test Driven Development: adding test code before function
# Allows you to think about code before writing it out
import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 0 == calculator.subtract(2, 2)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)
