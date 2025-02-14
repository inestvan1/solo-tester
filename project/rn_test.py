import unittest
import os
import sys

# Добавляем корневую папку в sys.path, чтобы можно было импортировать модули
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.discover("tests")  # Загружает все тесты из папки tests

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
