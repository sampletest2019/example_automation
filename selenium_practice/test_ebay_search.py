import pytest
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("item",
                         [
                             "macbook pro",
                             "puma sneakers",
                             "sony playstation 5"
                         ])
@pytest.mark.smoketest
def test_ebay_search(browser, item):
    browser.get("https://www.ebay.com/")
    browser.find_element(By.ID, "gh-ac").send_keys(item)
    browser.find_element(By.ID, "gh-btn").click()
    assert item in browser.title

