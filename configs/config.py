from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_preconfigured_chrome_driver() -> webdriver.Chrome:
    options = Options()
    options.add_experimental_option('detach', True)
    options.add_argument('--headless')
    #options.add_argument("--start-maximized")
    options.add_argument("--disable-search-engine-choice-screen")
    # options.add_argument('window-position=2000,50')
    # options.add_argument("--lang=hu")
    options.add_argument("--lang=en")
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Allure certificate error esetén
    return webdriver.Chrome(options=options)
