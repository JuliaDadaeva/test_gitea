from selenium.webdriver.common.by import By
from base.base_methods import Base
from tests.data import *
import os


class RepositoryPage(Base):
    # Locators
    ADD_REPOSITORY_BUTTON = (By.XPATH, "//a[@aria-label='Новый репозиторий']")
    REPOSITORY_NAME_FIELD = (By.XPATH, "//input[@id='repo_name']")
    CONFIRM_CREATE_REPOSITORY_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать репозиторий')]")
    NAME_CREATED_REPOSITORY = (By.XPATH, "//div[@class='repo-title']")
    START_UPLOAD_FILE_BUTTON = (By.XPATH, "//div[@class='repo-button-row']/a[2]")
    INPUT_UPLOAD_FILE = (By.XPATH, "//input[@type='file']")
    NAME_JUST_UPLOADED_FILE = (By.XPATH, "//div[@class='dz-filename']")
    CONFIRM_COMMIT_BUTTON = (By.XPATH, "//button[@id='commit-button']")
    TABLE_FILES_IN_REPOSITORY = (By.XPATH, "//table[@id='repo-files-table']")
    OPEN_FILE_BUTTON = (By.XPATH, f"//a[@title='{FILE_NAME}']")
    CONTENT_OF_FILE = (By.XPATH, "//div[contains(@class, 'segment')]")

    # Actions

    def click_add_repository_button(self):
        self.find_element_for_click(self.ADD_REPOSITORY_BUTTON).click()

    def fill_repository_name(self, repository_name):
        self.find_element_for_click(self.REPOSITORY_NAME_FIELD).send_keys(repository_name)

    def click_confirm_create_repository_button(self):
        self.find_element_for_click(self.CONFIRM_CREATE_REPOSITORY_BUTTON).click()

    def get_text_name_created_repository(self):
        return self.find_element_for_click(self.NAME_CREATED_REPOSITORY).text

    def click_start_upload_file_button(self):
        self.find_element_for_click(self.START_UPLOAD_FILE_BUTTON).click()

    def upload_file_from_path(self, file_path):
        input_upload_file = self.driver.find_element(*self.INPUT_UPLOAD_FILE)
        self.driver.execute_script("arguments[0].style.visibility = 'visible'", input_upload_file)
        input_upload_file.send_keys(file_path)

    def click_confirm_commit_button(self):
        self.find_element_for_click(self.CONFIRM_COMMIT_BUTTON).click()

    def get_text_of_files(self):
        return self.find_element_for_click(self.TABLE_FILES_IN_REPOSITORY).text

    def click_open_file_button(self):
        self.find_element_for_click(self.OPEN_FILE_BUTTON).click()

    def get_file_text(self):
        return self.find_element_presence(self.CONTENT_OF_FILE).text

    # Methods

    def create_repository(self, repository_name):
        self.click_add_repository_button()
        self.fill_repository_name(repository_name)
        self.click_confirm_create_repository_button()

    def upload_file(self):
        self.click_start_upload_file_button()
        with open(f'tests/{FILE_NAME}', 'w', encoding='utf-8') as file:
            print(FILE_CONTENT, file=file)
        self.upload_file_from_path(os.path.abspath(f'tests/{FILE_NAME}'))
        self.find_element_for_click(self.NAME_JUST_UPLOADED_FILE)
        self.click_confirm_commit_button()
