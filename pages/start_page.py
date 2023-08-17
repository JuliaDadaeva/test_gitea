from selenium.webdriver.common.by import By
from base.base_methods import Base


class StartPage(Base):

    # Locators

    INSTALL_GITEA_BUTTON = (By.XPATH, "//button[@class='ui primary button']")
    ENTER_IN_PROFILE_BUTTON = (By.XPATH, "//div[@class='right menu']/a[2]")
    ENTER_TEXT_TITLE = (By.XPATH, "//div[contains(@class, 'container')]/h4")
    LOGIN_FIELD = (By.XPATH, "//input[@id='user_name']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    CONFIRM_ENTER_BUTTON = (By.XPATH, "//button[contains(@class, 'green button')]")

    # Actions

    def click_install_button(self):
        self.find_element_for_click(self.INSTALL_GITEA_BUTTON).click()

    def click_enter_in_profile_button(self):
        self.find_element_for_click(self.ENTER_IN_PROFILE_BUTTON).click()

    def get_text_title(self):
        return self.find_element_for_click(self.ENTER_TEXT_TITLE).text

    def get_login_field(self):
        return self.find_element_for_click(self.LOGIN_FIELD)

    def get_password_field(self):
        return self.find_element_for_click(self.PASSWORD_FIELD)

    def get_confirm_enter_button(self):
        return self.find_element_for_click(self.CONFIRM_ENTER_BUTTON)






