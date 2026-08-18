"""
Конфигурация для pytest
Содержит фикстуры и настройки для тестирования
"""

import pytest
from pathlib import Path


@pytest.fixture
def project_root():
    """Возвращает корневую директорию проекта"""
    return Path(__file__).parent.parent


@pytest.fixture
def main_file(project_root):
    """Возвращает путь к основному файлу проекта"""
    return project_root / "fit_life.py"