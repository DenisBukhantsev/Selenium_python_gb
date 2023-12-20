import pytest
import yaml

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


with open("testdata.yaml") as f:
    test_data = yaml.safe_load(f)
    browser_type = test_data["browser"]




@pytest.fixture(scope="session")
def browser():
    if browser_type == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)

    yield driver
    driver.quit()


