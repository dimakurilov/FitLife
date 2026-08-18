<<<<<<< HEAD
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
=======
import subprocess
import sys
from pathlib import Path

import pytest


BASE_DIR = Path(__file__).resolve().parent.parent
SCRIPT_PATH = BASE_DIR / "fit_life.py"


@pytest.fixture(scope="session")
def file_path():
    return SCRIPT_PATH


@pytest.fixture(scope="session")
def source_code(file_path):
    assert file_path.exists(), (
        "Не найден файл `fit_life.py`.\n"
        "Проверьте, что основной файл проекта называется `fit_life.py` "
        "и находится в корне проекта."
    )
    return file_path.read_text(encoding="utf-8")


@pytest.fixture(scope="session")
def ast_tree(source_code):
    import ast
    return ast.parse(source_code)


@pytest.fixture
def run_program(file_path):
    def _run(user_input):
        result = subprocess.run(
            [sys.executable, str(file_path)],
            input=user_input,
            text=True,
            capture_output=True,
            encoding="utf-8",
            timeout=2,
        )

        assert result.returncode == 0, (
            "Программа завершилась с ошибкой.\n"
            f"STDOUT:\n{result.stdout}\n"
            f"STDERR:\n{result.stderr}"
        )
        return result.stdout

    return _run
>>>>>>> 4c93f03424e5aaf78d76f566ff305e0f7cec4073
