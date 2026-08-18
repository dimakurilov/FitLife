import sys
import io
from contextlib import contextmanager
import pytest

@pytest.fixture
def run_program():
    @contextmanager
    def _run(input_data):
        old_stdin = sys.stdin
        old_stdout = sys.stdout
        
        sys.stdin = io.StringIO(input_data)
        sys.stdout = io.StringIO()
        
        try:
            # Импортируем и выполняем код
            import fit_life
            # Если есть функция main - вызываем её
            if hasattr(fit_life, 'main'):
                fit_life.main()
            # Получаем вывод
            output = sys.stdout.getvalue()
            yield output
        except Exception as e:
            # Если ошибка - передаем её в тест
            yield str(e)
        finally:
            sys.stdin = old_stdin
            sys.stdout = old_stdout
    
    return _run
