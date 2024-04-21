import pytest
import calc
from calculator import Calculator

class TestCalculator:
    def setup(self):
       self.calc = Calculator

    def test_adding_success(self): #Сложение
        assert self.calc.adding(self, 1, 1) == 2

    def test_adding_unsuccess(self): #Негативный сложение
        assert self.calc.adding(self, 1, 1) == 3

    def test_zero_division(self): #Проверка деления на 0
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def test_subtraction_success(self): #Вычитание
        assert self.calc.subtraction(self, 5, 3) == 2

    def test_multiplication_success(self): #Умножение
        assert self.calc.multiply(self, 2, 3) == 6

    def test_division_success(self): #Деление
        assert self.calc.division(self, 10, 5) == 2

    def teardown(self):
        print('Выполнение метода Teardown')

