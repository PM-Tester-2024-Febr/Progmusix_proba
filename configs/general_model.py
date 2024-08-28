from datetime import datetime
from selenium.webdriver import Chrome


class GeneralPage:
    def __init__(self, browser: Chrome, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
        self.browser.set_window_size(1024,800)

    def close(self):
        self.browser.close()

    def refresh(self):
        self.browser.refresh()

    def back(self):
        self.browser.back()

    def current_url(self):
        return self.browser.current_url

    def save_screen(self, path):      #saját időbélyeg formátum:
        filename = f'{self.browser.title} - {datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}'
        print(rf'Screenshot attempt: {path}\{filename}')   #r kiveszi a \ aláhúzását
        if self.browser.save_screenshot(f'{path}\\{filename}'): #True / False-szal tér vissza.
            print("Screenshot saved")
        else:
            print("Screenshot failed")

