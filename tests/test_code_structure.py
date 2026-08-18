import os
import ast

def test_1_fit_life_exists():
    assert os.path.exists('fit_life.py'), "Файл fit_life.py не найден"

def test_2_syntax_errors():
    # Проверяем синтаксис без проблем с кодировкой
    with open('fit_life.py', 'r', encoding='utf-8') as f:
        code = f.read()
    try:
        ast.parse(code)
    except SyntaxError as e:
        raise AssertionError(f"Синтаксическая ошибка: {e}")
