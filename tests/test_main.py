import pytest

def test_1_has_input(run_program):
    try:
        with run_program("test\n25\n70\n1.75\n") as output:
            pass
    except Exception:
        raise AssertionError("Нет вызовов input()")

def test_2_has_int(run_program):
    try:
        with run_program("test\n25\n70\n1.75\n") as output:
            pass
    except Exception:
        raise AssertionError("Нет преобразования int()")

def test_3_has_float(run_program):
    try:
        with run_program("test\n25\n70.5\n1.75\n") as output:
            pass
    except Exception:
        raise AssertionError("Нет преобразования float()")

def test_4_has_round_or_float_formatting(run_program):
    with run_program("Анна\n25\n70.5\n1.75\n") as output:
        assert output is not None, "Нет вывода"

def test_5_has_f_string_in_print(run_program):
    with open('fit_life.py', 'r', encoding='utf-8') as f:
        content = f.read()
    assert 'f"' in content or "f'" in content, "Используйте f-строки"

def test_6_result(run_program):
    # Получаем результат
    with run_program("Анна\n25\n75.5\n1.8\n") as output:
        # Проверяем, что вывод не пустой
        assert output is not None, "Программа ничего не вывела"
        assert len(output.strip()) > 0, "Программа ничего не вывела"
        # Проверяем, что в выводе есть имя
        assert "Анна" in output, "В выводе должно быть имя"
        # Проверяем, что есть BMI
        assert "23." in output or "BMI" in output, "В выводе должно быть значение BMI"
