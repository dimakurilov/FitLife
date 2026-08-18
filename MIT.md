
---

### 7. **pytest.ini** (настройки тестов)

```ini
[pytest]
# Путь к папке с тестами
testpaths = tests

# Паттерны для поиска тестов
python_files = test_*.py
python_classes = Test*
python_functions = test_*

# Опции
addopts = 
    -v
    --tb=short
    --strict-markers

# Маркеры
markers =
    slow: тесты, требующие много времени
    unit: юнит-тесты
    integration: интеграционные тесты