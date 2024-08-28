import time
from configs.general_model import GeneralPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import mysql.connector
from selenium.webdriver.common.keys import Keys
from configs.testdata import TESTDATA


class ProgMusix(GeneralPage):

    def __init__(self,browser):
        super().__init__(browser,"http://localhost:4200")

#Menu buttons:
    def menu_login_btn(self):
        return self.browser.find_element(By.XPATH, '//button[@id="regLogin"]')

    def menu_logout(self):
        return self.browser.find_element(By.XPATH, '//button[@id="button_logOut"]')

    def menu_profile(self):
        return self.browser.find_element(By.XPATH, '//button[@id="profile"]')

    def menu_cart(self):
        return self.browser.find_element(By.XPATH, '//button[@id="button_myCart"]')

    def menu_location(self):
        return self.browser.find_element(By.XPATH, '//button[@id="button_location"]')

    def menu_search(self):
        return self.browser.find_element(By.XPATH, '//button[@id="button_search"]')

    def filter_on(self):
        return self.browser.find_element(By.XPATH, '//div[@id="filter-on"]')

    def filter_off(self):
        return self.browser.find_element(By.XPATH, '//div[@id="filter-off"]')

#Login/Registration page
    def btn_signin(self):
        return self.browser.find_element(By.XPATH, '//button[@class="sign_in"]')

    def btn_createaccount(self):
        return self.browser.find_element(By.XPATH, '//button[@class="create_account"]')

        # Login oldal - Bejelentkezés

    def login_btn(self):
        return self.browser.find_element(By.XPATH, '//button[@type="submit"]')

#Signing in:

    def username_login(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'username_input')))

    def password_login(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'password_input')))

#Signing in, negative:

    def negative_username_login_msg(self):
        return self.browser.find_element(By.ID,'mat-form-field-label-1')

    def negative_password_login_msg(self):
        return self.browser.find_element(By.ID,'mat-form-field-label-3')

    def negative_login_msg(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID,'mat-error-0'))).text

#Regisztráció, pozitív ág:

    def create_btn(self):
        return self.browser.find_element(By.XPATH, '//button[@class="create_account"]')

    def email(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'mat-input-2')))

    def username(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'mat-input-3')))

    def password(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'mat-input-4')))

    def password_again(self):
        return WebDriverWait(self.browser,5).until(EC.visibility_of_element_located((By.ID,'mat-input-5')))

    def register_btn(self):
        return WebDriverWait(self.browser,5).until(EC.visibility_of_element_located((By.XPATH,'//button[@type="submit"]')))

    def succesfull_msg(self):
        return WebDriverWait(self.browser,5).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="success_message ng-star-inserted"]'))).text

    def recaptcha(self):
        return WebDriverWait(self.browser,10).until((EC.visibility_of_element_located((By.ID,'recaptcha-anchor-label'))))

#Regisztráció, negatív ág:

    def enter_email(self):
        return self.browser.find_element(By.ID,'mat-form-field-label-5')

    def invalid_email_msg(self):
        return WebDriverWait(self.browser,5).until(EC.visibility_of_element_located((By.ID,'mat-error-0'))).text

    def enter_username(self):
        return self.browser.find_element(By.ID,'mat-form-field-label-7')

    def invalid_username_msg(self):
        return WebDriverWait(self.browser,5).until(EC.visibility_of_element_located((By.ID,'mat-error-1'))).text

    def enter_password(self):
        return self.browser.find_element(By.ID,'mat-form-field-label-9')

    def invalid_password_msg(self):
        return WebDriverWait(self.browser,5).until(EC.visibility_of_element_located((By.ID,'mat-error-2'))).text

    def enter_password_again(self):
        return self.browser.find_element(By.ID,'mat-form-field-label-11')

    def tab_password_again_msg(self):
        return WebDriverWait(self.browser,5).until(EC.visibility_of_element_located((By.ID,'mat-error-3'))).text

    def dif_password_againg_msg(self):
        return self.browser.find_element(By.ID,'mat-error-3').text

    def disabled_submit_btn(self):
        return self.browser.find_element(By.XPATH,'//button[@type="submit"]').get_attribute("disabled")

    def checkers_password(self):
        return self.browser.find_element(By.ID,'checkers')


# Kapcsolat oldal

    def sendmessage_btn(self):
        return self.browser.find_element(By.XPATH, '//button[@type="submit"]')

    def name_contact(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'mat-input-52')))

    def email_contact(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'mat-input-53')))

    def message_contact(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'mat-input-54')))

#Contact
    def contact_btn(self):
        return self.browser.find_element(By.ID,'button_location')

    def contact_name(self):
        return self.browser.find_element(By.ID,'mat-input-0')
    def contact_email(self):
        return self.browser.find_element(By.ID,'mat-input-1')
    def contact_field(self):
        return self.browser.find_element(By.ID,'mat-input-2')
    def contact_send_btn(self):
        return self.browser.find_element(By.XPATH,'//button[@type="submit"]')
    def contact_msg_succ(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="mat-dialog-content"]'))).text

    def map_icon(self):
        return self.browser.find_element(By.XPATH,'//div[@class="leaflet-pane leaflet-marker-pane"]/img[@role="button"]')

    def address(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="leaflet-popup-content"]'))).text

    def contact_sent_btn(self):
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, '//button[@class="mat-focus-indicator mat-raised-button mat-button-base mat-accent"]')))

    #Megerősítő email:

    def email_link_last_email(self):
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_any_elements_located((By.XPATH,'//div[@class="email_item"]')))[0]

    def email_confirm_link(self):
        return WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH,'//a[@href="http://localhost:8080/api/users/confirm?token=8edfef0e-b6aa-498e-990c-469198a1ae2d"]')))


#Database:

    def last_msg(self):
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="test1234",
            database="webshop"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM message ORDER BY id DESC LIMIT 1")
        return cursor.fetchone()


    def last_user_sql(self):
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="test1234",
            database="webshop"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT email, username FROM custom_user ORDER BY id DESC LIMIT 1")
        return cursor.fetchone()

    def contact_method(self):
        self.contact_btn().click()
        self.map_icon().click()
        self.contact_name().send_keys(TESTDATA['contact_name'])
        self.contact_email().send_keys(TESTDATA['contact_email'])
        self.contact_field().send_keys(TESTDATA['contact_field'])
        self.contact_send_btn().click()
        time.sleep(2)
        self.contact_sent_btn().click()


    def registration_method(self):
        self.menu_login_btn().click()
        self.create_btn().click()
        self.email().send_keys(TESTDATA['email_p'])
        self.username().send_keys(TESTDATA['username_p'])
        self.password().send_keys(TESTDATA['password_p'])
        self.password_again().send_keys(TESTDATA['password_p'])
        self.browser.switch_to.active_element.send_keys(Keys.TAB)
        self.browser.switch_to.active_element.send_keys(Keys.TAB)
        self.browser.switch_to.active_element.send_keys(Keys.ENTER)
        time.sleep(5)
        self.register_btn().click()

    def reg_TAB_method(self):
        self.menu_login_btn().click()
        self.create_btn().click()
        self.email().send_keys(Keys.TAB)
        self.username().send_keys(Keys.TAB)
        self.password().send_keys(Keys.TAB)
        self.password_again().send_keys(Keys.TAB)

    def reg_negative_method(self):
        self.menu_login_btn().click()
        self.create_btn().click()
        self.email().send_keys(TESTDATA['negative_email'])
        self.username().send_keys(TESTDATA['negative_username'])
        self.password().send_keys(TESTDATA['negative_password'])
        self.password_again().send_keys(TESTDATA['negative_password_again'])
        self.password_again().send_keys(Keys.TAB)

    def login_method_p(self):
        self.menu_login_btn().click()
        self.username_login().send_keys(TESTDATA['Login_username_p'])
        self.password_login().send_keys(TESTDATA['Login_password_p'])
        self.login_btn().click()

    def login_method_TAB_n(self):
        self.menu_login_btn().click()
        self.username_login().send_keys(Keys.TAB)
        self.password_login().send_keys(Keys.TAB)


    def login_method_n(self):
        self.browser.refresh()
        self.username_login().send_keys(TESTDATA['negative_login_username'])
        self.password_login().send_keys(TESTDATA['negative_login_password'])
        self.login_btn().click()

    def new_tab_email(self):
        self.browser.switch_to.new_window()
        self.browser.get('https://app.endtest.io/mailbox?email=progmasterstn@endtest-mail.io')
        time.sleep(5)
        self.email_link_last_email().click()
        self.email_confirm_link().click()
        self.browser.switch_to.window(self.browser.window_handles[-1])
        self.username_login().send_keys(TESTDATA['Login_username_p'])
        self.password_login().send_keys(TESTDATA['Login_password_p'])
        self.login_btn().click()




