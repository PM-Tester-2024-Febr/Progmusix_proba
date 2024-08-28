from configs.config import get_preconfigured_chrome_driver
from page_model import ProgMusix
from configs.testdata import TESTDATA


class TestProgmusix:
    def setup_method(self):
        page = ProgMusix(get_preconfigured_chrome_driver())
        self.page = page
        page.open()
    def teardown_method(self):
        self.page.close()

    def test_reg_TAB(self):
        self.page.reg_TAB_method()
        assert self.page.invalid_email_msg() == TESTDATA['TAB_email']
        assert self.page.enter_email().is_displayed()
        assert self.page.invalid_username_msg() == TESTDATA['TAB_username']
        assert self.page.enter_username().is_displayed()
        assert self.page.invalid_password_msg() == TESTDATA['TAB_password']
        assert self.page.enter_password().is_displayed()
        assert self.page.tab_password_again_msg() == TESTDATA['TAB_password_again']
        assert self.page.enter_password_again().is_displayed()
        assert self.page.disabled_submit_btn() == 'true'

    def test_reg_negative(self):
        self.page.reg_negative_method()
        #Helytelen formátumra való felszólító üzenetek megjelenése:
        assert self.page.invalid_email_msg() == TESTDATA['negative_email_msg']
        assert self.page.invalid_username_msg() == TESTDATA['negative_username_msg']
        assert self.page.invalid_password_msg() == TESTDATA['negative_password_msg']
        assert self.page.checkers_password().is_displayed()
        assert self.page.dif_password_againg_msg() == TESTDATA['negative_password_again_msg']

    def test_contact(self):
        self.page.contact_method()
        assert TESTDATA['address'] in self.page.address()
        assert self.page.contact_msg_succ() == TESTDATA['contact_msg_succ']
        assert TESTDATA['contact_name'] and TESTDATA['contact_email'] and TESTDATA['contact_field'] in self.page.last_msg()


