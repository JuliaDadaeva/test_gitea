from selenium.common import TimeoutException
from pages.start_page import StartPage
from pages.registration_page import RegistrationPage
from tests.data import *


def test_check_starting_page(docker_container, browser):
    start_page = StartPage(browser)
    start_page.go_to_site(start_page.basic_url)
    try:
        start_page.click_install_button()
    except TimeoutException:
        browser.refresh()
        start_page.click_install_button()
    assert start_page.get_text_title() == START_PAGE_TEXT_TITLE
    assert start_page.get_login_field().is_displayed()
    assert start_page.get_password_field().is_displayed()
    assert start_page.get_confirm_enter_button().is_displayed()


def test_user_registration(browser):
    registration_page = RegistrationPage(browser)
    registration_page.go_to_site(registration_page.basic_url)
    registration_page.registration(USER_NAME, EMAIL, PASSWORD)
    assert registration_page.get_text_positive_message() == REGISTRATION_POSITIVE_MESSAGE
