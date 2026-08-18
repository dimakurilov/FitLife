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
            import fit_life
            if hasattr(fit_life, 'main'):
                fit_life.main()
            output = sys.stdout.getvalue()
            yield output
        finally:
            sys.stdin = old_stdin
            sys.stdout = old_stdout
    
    return _run
