from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config.config import Config

class WebDriverManager:
    def __init__(self):
        # Инициализация конфигурации, где хранится путь к драйверу
        self.config = Config('config/config.ini')
        self.driver = None

    def initialize_driver(self):
        # Получаем путь к драйверу из конфигурации
        driver_path = self.config.get_driver_path()

        # Устанавливаем опции для Chrome
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Фоновый режим

        # Создаём сервис для веб-драйвера с указанием пути к драйверу
        service = Service(driver_path)

        # Инициализация веб-драйвера с опциями и сервисом
        self.driver = webdriver.Chrome(service=service, options=options)

    def get_driver(self):
        # Возвращаем текущий экземпляр драйвера
        return self.driver

    def quit_driver(self):
        # Закрываем драйвер, если он был инициализирован
        if self.driver:
            self.driver.quit()
