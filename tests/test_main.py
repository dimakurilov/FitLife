"""
Основные тесты функциональности FitLife
"""

import pytest
import sys
from io import StringIO
from pathlib import Path

# Добавляем корневую папку в путь для импорта
sys.path.insert(0, str(Path(__file__).parent.parent))


def test_import_main():
    """Проверяет, что файл можно импортировать"""
    try:
        import fit_life
    except ImportError as e:
        pytest.fail(f"Не удалось импортировать fit_life: {e}")


def test_constants_values():
    """Проверяет значения констант"""
    import fit_life
    assert fit_life.WATER_PER_KG == 30, "WATER_PER_KG должно быть 30"
    assert fit_life.ML_TO_LITERS == 1000, "ML_TO_LITERS должно быть 1000"


def test_main_function_exists():
    """Проверяет наличие функции main"""
    import fit_life
    assert hasattr(fit_life, 'main'), "Функция main не найдена"
    assert callable(fit_life.main), "main должна быть вызываемой функцией"


def test_input_and_output(monkeypatch, capsys):
    """Тестирует ввод и вывод программы"""
    import fit_life
    
    # Подготовка входных данных
    inputs = ['Анна', '25', '68', '1.72']
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    
    # Запуск программы
    fit_life.main()
    
    # Получение вывода
    captured = capsys.readouterr()
    output = captured.out
    
    # Проверки
    assert 'FitLife' in output, "Приветствие не содержит 'FitLife'"
    assert 'Анна' in output, "Имя пользователя не выведено"
    assert '25' in output, "Возраст пользователя не выведен"
    assert '23.0' in output or '23' in output, "ИМТ не выведен или неверный"
    assert 'л. в день' in output, "Норма воды не выведена"
    assert 'Будьте здоровы' in output, "Финальное сообщение отсутствует"