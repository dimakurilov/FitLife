"""
Тесты для проверки структуры кода
"""

import ast
import pytest
from pathlib import Path


def test_file_exists(main_file):
    """Проверяет, что файл fit_life.py существует"""
    assert main_file.exists(), "Файл fit_life.py не найден"


def test_file_not_empty(main_file):
    """Проверяет, что файл не пустой"""
    assert main_file.stat().st_size > 0, "Файл fit_life.py пуст"


def test_syntax_valid(main_file):
    """Проверяет синтаксис Python"""
    try:
        with open(main_file, 'r', encoding='utf-8') as f:
            content = f.read()
        ast.parse(content)
    except SyntaxError as e:
        pytest.fail(f"Синтаксическая ошибка: {e}")


def test_has_constants(main_file):
    """Проверяет наличие констант"""
    with open(main_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    assert "WATER_PER_KG" in content, "Константа WATER_PER_KG не найдена"
    assert "ML_TO_LITERS" in content, "Константа ML_TO_LITERS не найдена"


def test_has_main_function(main_file):
    """Проверяет наличие функции main()"""
    with open(main_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    assert "def main():" in content, "Функция main() не найдена"


def test_has_if_main(main_file):
    """Проверяет наличие __name__ == '__main__'"""
    with open(main_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    assert '__name__ == "__main__"' in content, "Отсутствует блок if __name__ == '__main__'"