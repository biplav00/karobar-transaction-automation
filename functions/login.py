from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# credentials = {"phoneNumber": "9869696969", "otp": "123456"}
# credentials = {"phoneNumber": "9988776655", "otp": "000000"}
credentials = {"phoneNumber": "9988776644", "otp": "000000"}

locaters = {
    "phoneNumberField": "//input[@placeholder='9XXXXXXXXX']",
    "continueButton": "//button[@type='submit']",
    "otpField": "//label[normalize-space(text())='Enter Code']/following::input",
    "dashboardTitle": "//h2[normalize-space(text())='Dashboard']",
}


def login(driver):
    driver.get("https://pilot.karobarapp.com")
    driver.find_element(By.XPATH, locaters["phoneNumberField"]).send_keys(
        credentials["phoneNumber"]
    )
    driver.find_element(By.XPATH, locaters["continueButton"]).click()
    otp_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, locaters["otpField"]))
    )
    otp_field.send_keys(credentials["otp"])
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, locaters["dashboardTitle"]))
    )
