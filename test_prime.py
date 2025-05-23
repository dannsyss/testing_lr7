import pytest
from is_prime import is_prime
import warnings
import random


# Фикстура для генерации случайного числа от 1 до 100
@pytest.fixture
def random_number():
    # Генерирует случайное число в диапазоне от 1 до 100
    return random.randint(1, 100)


# Параметризованный тест для простых чисел
@pytest.mark.parametrize("number, expected", [
    (2, True),
    (3, True),
    (17, True),
    (7919, True),
    (104729, True)
])
def test_prime_numbers(number, expected):
    #Тест для простых чисел.
    assert is_prime(number) == expected
    print(f"Тест для числа {number} пройден успешно")


# Параметризованный тест для составных чисел
@pytest.mark.parametrize("number, expected", [
    (1, False),
    (4, False),
    (10, False),
    (100, False),
    (1000000, False)
])
def test_non_prime_numbers(number, expected):
    #Тест для составных чисел.
    assert is_prime(number) == expected
    print(f"Тест для числа {number} пройден успешно")


# Параметризованный тест для граничных случаев
@pytest.mark.parametrize("number, expected", [
    (0, False),
    (1, False),
    (-1, False),
    (-2, False),
    (-17, False)
])
def test_edge_cases(number, expected):
    # Тест для граничных случаев.
    assert is_prime(number) == expected
    print(f"Тест для граничного случая {number} пройден успешно")


# Параметризованный тест для проверки исключений
@pytest.mark.parametrize("invalid_input", [
    "string",
    3.14,
    True,
    [2, 3, 5],
    None
])
def test_invalid_input(invalid_input):
    # Тест на возникновение исключения при неверном вводе.
    with pytest.raises(TypeError):
        is_prime(invalid_input)
    print(f"Тест на исключение для {invalid_input} пройден успешно")


def test_large_number_warning():
    # Тест на возникновение предупреждения для больших чисел.
    with pytest.warns(RuntimeWarning):
        is_prime(1_000_001)
    print("Тест на предупреждение для больших чисел пройден успешно")


def test_warning_message():
    # Тест на содержание предупреждающего сообщения.
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        is_prime(2_000_000)

        assert len(w) == 1
        assert issubclass(w[0].category, RuntimeWarning)
        assert "large number" in str(w[0].message)
        assert "2000000" in str(w[0].message)
    print("Тест на содержание предупреждающего сообщения пройден успешно")


# Тесты с использованием фикстуры random_number
def test_random_number_in_range(random_number):
    # Тест, что случайное число попадает в диапазон 1-100.
    assert 1 <= random_number <= 100
    print(f"Случайное число {random_number} находится в диапазоне 1-100")


def test_is_prime_with_random_number(random_number):
    # Тест функции is_prime со случайным числом.
    result = is_prime(random_number)
    assert isinstance(result, bool)
    print(f"Проверка случайного числа {random_number} на простоту: {result}")


# Параметризованный тест с фикстурой, чтобы показать разные случайные числа
@pytest.mark.parametrize("attempt", range(3))
def test_multiple_random_numbers(random_number, attempt):
    # Тест, показывающий разные случайные числа для каждого вызова.
    print(f"Попытка {attempt + 1}: получено случайное число {random_number}")
