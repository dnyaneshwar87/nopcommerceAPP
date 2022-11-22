from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(
        executable_path="C:\\Users\\Admin\\PycharmProjects\\pythonProject1\\nopcommerceApp\\chromedriver.exe")
    return driver