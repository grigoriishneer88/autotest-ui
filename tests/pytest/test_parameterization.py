import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize('number1, number2',
                         [
                             (1,2),
                             (3,4),
                             (5,6),
                             (7,7348),
                             (1,-2),
                             (1,33),
                             (4,5)
                         ]
                         )
def test_numbers(number1:int, number2:int):
    print(number1)
    print(number2)
    number2 = 3
    assert number1 > number2

@pytest.mark.parametrize('num1',[1,2,4,67,8,4])
def test_number_1(num1:int):
    print(num1)

@pytest.mark.parametrize('num1',[1,2,3,4,5,6])
@pytest.mark.parametrize('num2',[11,12,13,14,15,16])

def test_multiple_numbers(num1:int, num2:int):
    print(num1)
    print(num2)

@pytest.fixture(params=['chromium','webkit','firefox'])
def browser(request:SubRequest):
    return request.param

def test_open_browser(browser:str):
    print(f"Running test on browser {browser}")


@pytest.mark.parametrize('user',['alice','zara'])
class TestOperations:
    @pytest.mark.parametrize('account',['credit','debit'])
    def test_user_with_operations(self,user:str, account:str):
        ...

    def test_user_without_operations(self, user:str):
        ...



users = {
    '34523452345':'user with money on bank account',
    '12341234123':'user without money on bank account',
    '12345675467456':'user operations on bank account'
}

def format_phone_number(phone:str):
    return f'{phone}:{users[phone]}'

@pytest.mark.parametrize(
    'phone',
    users.keys(),
    ids=format_phone_number
    #ids=lambda phone: f'{phone}: {users[phone]}'
)
def test_identifiers(phone:str):
    ...

