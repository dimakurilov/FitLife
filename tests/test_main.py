import pytest

def test_1_has_input(run_program):
    try:
        with run_program("test\n25\n70\n1.75\n"):
            pass
    except Exception:
        raise AssertionError("Нет вызовов input()")

def test_2_has_int(run_program):
    with run_program("test\n25\n70\n1.75\n"):
        pass

def test_3_has_float(run_program):
    with run_program("test\n25\n70.5\n1.75\n"):
        pass

def test_4_has_round_or_float_formatting(run_program):
    with run_program("test\n25\n70.5\n1.75\n") as output:
        assert '23.02' in output or '23.0' in output

def test_5_has_f_string_in_print(run_program):
    with open('fit_life.py') as f:
        assert 'f"' in f.read() or "f'" in f.read()

def test_6_result(run_program):
    output = run_program("Анна\n25\n75.5\n1.8\n")
    assert output and output.strip()
