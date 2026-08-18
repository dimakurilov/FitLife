import sys, io
from contextlib import contextmanager
import pytest

@pytest.fixture
def run_program():
    @contextmanager
    def _run(input_data):
        old_stdin, old_stdout = sys.stdin, sys.stdout
        sys.stdin = io.StringIO(input_data)
        sys.stdout = io.StringIO()
        try:
            import fit_life
            if hasattr(fit_life, 'main'):
                fit_life.main()
            yield sys.stdout.getvalue()
        finally:
            sys.stdin, sys.stdout = old_stdin, old_stdout
    return _run
