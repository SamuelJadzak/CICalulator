"""
tests for calculator
"""
import Calculator


class Test_CalculatorApp:
    def test_add(self):
        assert 5 == Calculator.add(2, 3)

    def test_subtract(self):
        assert 2 == Calculator.subtract(4, 2)

    def test_divide(self):
        assert 2 == Calculator.divide(4, 2)

    def test_multiply(self):
        assert 6 == Calculator.multiply(2, 3)
