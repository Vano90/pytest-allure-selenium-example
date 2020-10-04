import pytest
import allure
from selenium import webdriver
from time import sleep

URL_FOR_ALLURE = 'https://github.com/Vano90/selenide-pdf-check-example'
URL = 'https://github.com/Vano90'
SCREENSHOT_NAME = "screenshot.png"
ASSERT_TEXT = "selenide-pdf-check-example"


@pytest.yield_fixture()
@allure.title("setUp and tearDown driver")
def driver():
    driver_chrome = webdriver.Chrome(executable_path="./chromedriver")
    driver_chrome.maximize_window()
    yield driver_chrome
    driver_chrome.quit()


@allure.title("This test check gitHub repo")
@allure.link(URL)
@allure.severity(allure.severity_level.CRITICAL)
def test_github_repo(driver):
    with allure.step('Open Github'):
        driver.get(URL)
    with allure.step("Click on repo selenide-pdf-check-example"):
        repo_selenide = driver.find_element_by_css_selector(
            ".d-flex.width-full.flex-items-center.position-relative > a")
        repo_selenide.click()
    with allure.step("Make screenshot and attach it to allure report"):
        driver.save_screenshot(SCREENSHOT_NAME)
        allure.attach.file('./' + SCREENSHOT_NAME, 'Repo page', allure.attachment_type.PNG)
    with allure.step("Scrolling to bottom page"):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    with allure.step("Check README.md text on the page"):
        find_text = driver.find_element_by_xpath("//a[@id='user-content-selenide-pdf-check-example']/..")
        assert ASSERT_TEXT in find_text.text
    sleep(3)
