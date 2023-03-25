def fizzbuzz(arg):
    if arg % 3 == 0 and arg % 4 == 0:
        return 'fizzbuzz'
    if arg % 3 == 0:
        return 'fizz'
    if arg  % 5 == 0:
        return 'buzz'
    return str(arg)

import pytest

@pytest.mark.parametrize('number', [1, 2, 4, 7, 11])
def test_fizzbuzz_number_returns_number(number):
    assert fizzbuzz(number) == str(number)

@pytest.mark.parametrize('number', [3, 33, 9, 99])
def test_fizzbuzz_number_returns_fizz(number):
    assert fizzbuzz(number) == 'fizz'

@pytest.mark.parametrize('number', [5, 55, 2600])
def test_fizzbuzz_number_returns_buzz(number):
    assert fizzbuzz(number) == 'buzz'

@pytest.mark.parametrize('number', [0, 15, 150])
def test_fizzbuzz_number_returns_fizzbuzz(number):
    assert fizzbuzz(number) == 'fizzbuzz'




def test_fizzbuzz_exists():
    fizzbuzz

def test_fizzbuzz_can_be_called_with_arg():
    fizzbuzz(0)

def test_fizzbuzz_returns_something():
    assert fizzbuzz(0) is not None

def test_fizzbuzz_returns_str():
    assert isinstance(fizzbuzz(0), str)



