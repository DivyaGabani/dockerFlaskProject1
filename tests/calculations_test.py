"""Testing the Calculator"""
# From specifies the namespace
from calculator.calculations import Addition, Subtraction, Multiplication, Divison


def test_calculation_multiplication_instance():
    """Testing the Calculator Subtract"""
    tuple_list = (1, 2)
    calculation = Multiplication.create(tuple_list)
    assert isinstance(calculation, Multiplication)

def test_calculation_subtraction_instance():
    """Testing the Calculator Subtract"""
    tuple_list = (1, 2)
    calculation = Subtraction.create(tuple_list)
    assert isinstance(calculation, Subtraction)

def test_calculation_addition_instance():
    """Testing the Calculator Subtract"""
    tuple_list = (1, 2)
    calculation = Addition.create(tuple_list)
    assert isinstance(calculation, Addition)


def test_calculation_add_get_result_method():
    """Testing the Calculator Addition"""
    # this is show using the calculator object add method
    tuple_list = (1, 2)
    calculation = Addition.create(tuple_list)
    assert calculation.get_result() == 3


def test_calculation_subtract_get_result_method():
    """Testing the Calculator Subtract"""
    tuple_list = (1, 2)
    calculation = Subtraction.create(tuple_list)
    assert calculation.get_result() == -3


def test_calculation_multiply_get_result_method():
    """Testing the Calculator Multiplication"""
    tuple_list = (1, 2)
    calculation = Multiplication.create(tuple_list)
    assert calculation.get_result() == 2

def test_calculation_divide_get_result_method():
    """Testing the Calculator Divison"""
    tuple_list = (1, 2)
    calculation = Divison.create(tuple_list)
    assert calculation.get_result() == 0.5