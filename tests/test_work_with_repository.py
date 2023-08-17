from pages.repository_page import RepositoryPage
from tests.data import *


def test_create_repository(browser, enter_in_profile):
    rep_page = RepositoryPage(browser)
    rep_page.create_repository(REPOSITORY_NAME)
    assert REPOSITORY_NAME in rep_page.get_text_name_created_repository()


def test_upload_file_to_repository(browser, enter_in_profile):
    rep_page = RepositoryPage(browser)
    rep_page.go_to_site(url=f'{rep_page.basic_url}/{USER_NAME}/{REPOSITORY_NAME}')
    rep_page.upload_file()
    assert FILE_NAME in rep_page.get_text_of_files()


def test_open_uploaded_file(browser, enter_in_profile):
    rep_page = RepositoryPage(browser)
    rep_page.go_to_site(url=f'{rep_page.basic_url}/{USER_NAME}/{REPOSITORY_NAME}')
    rep_page.click_open_file_button()
    assert FILE_CONTENT == rep_page.get_file_text()
