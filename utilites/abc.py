from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def wait_for_element(driver, by, value, timeout=10):
    """
    Ожидает появления элемента на странице в течение заданного времени (timeout).
    
    :param driver: Экземпляр драйвера (ChromeDriver или любой другой).
    :param by: Тип локатора (например, By.ID, By.XPATH и т.д.).
    :param value: Значение локатора (например, 'button', '//div[@class="class_name"]' и т.д.).
    :param timeout: Время ожидания в секундах (по умолчанию 10 секунд).
    :return: Найденный элемент или вызов TimeoutException, если элемент не был найден.
    """
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return element
    except TimeoutException:
        print(f"Элемент с локатором {by} и значением {value} не был найден за {timeout} секунд.")
        return None
