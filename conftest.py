import pytest

from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--headless", action="store_true")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("browser")
    headless = request.config.getoption("headless")  # True - False

    if browser_name in ["chrome", "ch"]:
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
    elif browser_name in ["firefox", "ff"]:
        options = FFOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    elif browser_name in ["yandex", "ya"]:
        service = ChromiumService(
            executable_path="/home/mikhail/Downloads/drivers/yandexdriver"
        )
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.binary_location = "/usr/bin/yandex-browser"
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name in ["safari", "sf"]:
        driver = webdriver.Safari()

    driver.maximize_window()

    yield driver

    driver.quit()
