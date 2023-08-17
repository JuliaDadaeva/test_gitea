import pytest
import docker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.start_page import StartPage
from tests.data import *


@pytest.fixture(scope='session')
def docker_container():
    docker_client = docker.from_env()
    container = docker_client.containers.run("gitea/gitea:latest", detach=True,
                                             publish_all_ports=True, ports={'3000/tcp': 3000, '22/tcp': 222})
    yield
    container.stop()
    container.remove()


@pytest.fixture()
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.close()


@pytest.fixture
def enter_in_profile(browser, login=EMAIL, password=PASSWORD):
    start_page = StartPage(browser)
    start_page.go_to_site(start_page.basic_url)
    start_page.click_enter_in_profile_button()
    start_page.get_login_field().send_keys(login)
    start_page.get_password_field().send_keys(password)
    start_page.get_confirm_enter_button().click()
