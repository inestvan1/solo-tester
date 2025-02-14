import configparser

class Config:
    def __init__(self, config_file):
        # Инициализация конфигурации
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get_driver_path(self):
        # Получение пути к драйверу для Selenium
        return self.config['Settings']['driver_path']
    
    def get_url(self):
        # Получение URL-адреса сайта с играми
        return self.config['Settings']['url']
    
    def get_api_key(self):
        # Получение API-ключа для работы с GPT (OpenAI)
        return self.config['Settings']['api_key']

    def get_game_timeout(self):
        # Получение времени ожидания для загрузки игр или ожидания шагов в тестах
        return int(self.config['Settings']['game_timeout'])
