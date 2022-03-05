import pytest
from main import balance


class TestPyTest:
    data = [('(((([{}]))))', True), ('[([])((([[[]]])))]{()}', True),
            ('{{[()]}}', True), ('}{}', False), ('{{[(])]}}', False),
            ('[[{())}]', False)]

    @pytest.mark.parametrize('string_, result', data)
    def test_balance_func(self, string_, result):
        assert balance(string_) is result
