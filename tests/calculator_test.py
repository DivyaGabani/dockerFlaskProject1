"""Testing the Calculator"""
# From specifies the namespace
from calculator import Calculator

def test_calculator_is_instance():
    calculator = Calculator()
    assert isinstance(calculator,Calculator)

def test_calculator_add_method():
    """Testing the Calculator"""
    # this is show using the calculator object add method
    tuple_list = (1,2)
    assert Calculator.add(tuple_list) == 3

def test_calculator_subtract_method():
    """Testing the Calculator Subtract"""
    tuple_list = (1,2)
    assert Calculator.subtract(tuple_list) == -3


def test_calculator_multiply_method():
    """Testing the Calculator Subtract"""
    tuple_list = (1,2)
    assert Calculator.multiply(tuple_list) == 2

def test_calculator_divide_method():
    """Testing the Calculator Subtract"""
    tuple_list = (1,2)
    assert Calculator.divide(tuple_list) == 0.5