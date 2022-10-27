# dumpsys window | grep -iE "mCurrentFocus=Window{"   ---> Activity
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
desired_cap = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "app": "/home/minexora/Projects/pg/appium/first_app/apk/7ca1c5e0_e318_4859_a646_2a4e5ec300f9_nabiz.apk",
    "appPackage": "com.waveline.nabiz",
    "appWaitActivity": "com.waveline.nabd.client.activities.WelcomeActivity"
}


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)


el4 = driver.find_element(by='id', value='com.waveline.nabiz:id/select_sources')
el4.click()
driver.execute_script()