from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time

class CitylinkSearchTest(unittest.TestCase):
    def setUp(self):
        """
        Настройка перед каждым тестом:
        - Инициализация драйвера Chrome.
        - Открытие главной страницы Ситилинк.
        - Максимизация окна браузера.
        - Ожидание загрузки страницы (2 секунды).
        """
        self.driver = webdriver.Chrome()  # Инициализация драйвера Chrome
        self.driver.get("https://www.citilink.ru/")  # Открытие сайта Ситилинк
        self.driver.maximize_window()  # Максимизация окна браузера
        time.sleep(2)  # Ожидание загрузки страницы

    def test_search_product(self):
        """
        Тест для проверки поиска товара на сайте Ситилинк:
        - Поиск товара по запросу "Ноутбук ASUS".
        - Проверка, что результаты поиска отображаются на странице.
        """
        # Поиск товара
        search_box = self.driver.find_element(By.NAME, "text")  # Находим поле поиска
        search_box.send_keys("Ноутбук ASUS")  # Вводим запрос "Ноутбук ASUS"
        search_box.send_keys(Keys.RETURN)  # Нажимаем Enter для поиска
        time.sleep(3)  # Ожидание загрузки результатов поиска

        # Проверка, что результаты поиска отображаются
        results = self.driver.find_elements(By.CLASS_NAME, "ProductCardHorizontal__title")  # Находим все результаты поиска
        self.assertGreater(len(results), 0, "Результаты поиска не найдены")  # Проверяем, что результаты есть

    def tearDown(self):
        """
        Завершение теста:
        - Закрытие браузера после выполнения теста.
        """
        self.driver.quit()  # Закрытие браузера

if __name__ == "__main__":
    unittest.main()  # Запуск теста
