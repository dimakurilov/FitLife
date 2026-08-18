import os, ast

def test_1_fit_life_exists():
    assert os.path.exists('fit_life.py')

def test_2_syntax_errors():
    with open('fit_life.py') as f:
        ast.parse(f.read())
