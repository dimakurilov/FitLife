import pytest

def test_1_has_input(run_program):
    try:
        with run_program("test\n25\n70\n1.75\n") as output:
            pass
    except Exception:
        raise AssertionError("Ожидается минимум 4 вызова `input()` для имени, возраста, веса и роста.")

def test_2_has_int(run_program):
    with run_program("test\n25\n70\n1.75\n") as output:
        pass
    try:
        with run_program("test\n25\n70\n1.75\n") as output:
            pass
    except TypeError:
        raise AssertionError("Проверьте, что для возраста используется преобразование типа `int()`.")

def test_3_has_float(run_program):
    try:
        with run_program("test\n25\n70.5\n1.75\n") as output:
            pass
    except ValueError:
        raise AssertionError("Проверьте, что для веса и роста используется преобразование типа `float()`.")

def test_4_has_round_or_float_formatting(run_program):
    with run_program("test\n25\n70.5\n1.75\n") as output:
        assert '23.02' in output or '23.0' in output, "Проверьте, что результат округлен до 2 знаков"

def test_5_has_f_string_in_print(run_program):
    with run_program("test\n25\n70\n1.75\n") as output:
        assert 'f' in open('fit_life.py').read(), "Используйте f-строки для вывода"

def test_6_result(run_program):
    output = run_program("Анна\n25\n75.5\n1.8\n")
    assert output and output.strip(), "Программа должна выводить результат"
