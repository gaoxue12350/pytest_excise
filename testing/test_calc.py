import pytest

from pythoncode.calculator import Calculator


class TestCalc:
    def setup_class(self):
        print('计算开始')
        self.calc = Calculator()

    def teardown_class(self):
        print('计算结束')

    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 2], [100, 100, 200], [0.1, 0.1, 0.2], [-1, -1, -2], [0, 100, 100], [1 / 2, 1 / 4, 3 / 4],
        [1 / 3, 1 / 4, 7 / 12], [1 / 5, 1 / 7, 12 / 35]
    ], ids=['int', 'bigint', 'float', 'minus', 'zero', 'fraction1', 'fraction2', 'fraction3'])
    def test_add(self, a, b, expect):
        # calc=Calculator()
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 1], [1, 2, 0.5], [0.1, 0.2, 0.5], [1, 3, 1 / 3], [7, 12, 1 / 12], [2, 1, 2], [0, 1, 0], [-1, -1, 1],
        [-1, 100, -0.01], [100, -1, -100], [1 / 2, 1 / 3, 3 / 2], [1 / 3, 1 / 4, 4 / 3]
    ], ids=['int1', 'smallint', 'float1', 'int2', 'int3', 'bugint', '0/', 'same_minus', 'minus/int', 'int/minus',
            'fraction1', 'fraction2'])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert result == expect
