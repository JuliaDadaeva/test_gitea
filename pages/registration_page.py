from selenium.webdriver.common.by import By
from base.base_methods import Base


class RegistrationPage(Base):
    # Locators

    REGISTRATION_START_BUTTON = (By.XPATH, "//div[@class='right menu']/a[1]")
    USERNAME_FIELD = (By.XPATH, "//input[@id='user_name']")
    EMAIL_FIELD = (By.XPATH, "//input[@id='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    PASSWORD_REPEAT_FIELD = (By.XPATH, "//input[@id='retype']")
    REGISTRATION_CONFIRM_BUTTON = (By.XPATH, "//button[contains(@class, 'green')]")
    POSITIVE_MESSAGE = (By.XPATH, "//div[contains(@class, 'positive')]")

    # Actions

    def click_registration_start_button(self):
        self.find_element_for_click(self.REGISTRATION_START_BUTTON).click()

    def fill_username_field(self, username):
        self.find_element_for_click(self.USERNAME_FIELD).send_keys(username)

    def fill_email_field(self, email):
        self.find_element_for_click(self.EMAIL_FIELD).send_keys(email)

    def fill_password_field(self, password):
        self.find_element_for_click(self.PASSWORD_FIELD).send_keys(password)

    def fill_password_repeat_field(self, password):
        self.find_element_for_click(self.PASSWORD_REPEAT_FIELD).send_keys(password)

    def click_registration_confirm_button(self):
        self.find_element_for_click(self.REGISTRATION_CONFIRM_BUTTON).click()

    def get_text_positive_message(self):
        return self.find_element_for_click(self.POSITIVE_MESSAGE).text

    # Methods

    def registration(self, username, email, password):
        self.click_registration_start_button()
        self.fill_username_field(username)
        self.fill_email_field(email)
        self.fill_password_field(password)
        self.fill_password_repeat_field(password)
        self.click_registration_confirm_button()


