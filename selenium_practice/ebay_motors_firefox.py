from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

services = Service(GeckoDriverManager().install())
browser = webdriver.Firefox(service=services)
browser.maximize_window()

browser.get('http://www.ebay.com/')
browser.find_element(By.LINK_TEXT, "Motors").click()


def wait_for_the_dropdown_and_select_value(time, name, value):
    dropdown = WebDriverWait(browser, timeout=time).until(EC.element_to_be_clickable((By.NAME, name)))
    Select(dropdown).select_by_visible_text(value)


def wait_and_select_by_xpath(time, xpath, value):
    dropdown = WebDriverWait(browser, timeout=time).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    Select(dropdown).select_by_visible_text(value)


wait_for_the_dropdown_and_select_value(1, "Year", "2020")
wait_for_the_dropdown_and_select_value(1, "Make", "BMW")
wait_for_the_dropdown_and_select_value(1, "Model", "X5")
wait_for_the_dropdown_and_select_value(1, "Trim", "M Sport Utility 4-Door")
wait_for_the_dropdown_and_select_value(1, "Engine", "4.4L 4395CC V8 GAS DOHC Turbocharged")
browser.find_element(By.CLASS_NAME, "motors-finder__find-btn").click()
browser.quit()
