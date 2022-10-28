from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_cap = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "app": "/home/minexora/Projects/pg/appium/first_app/apk/Yaay Social Media_3.3.2_apkcombo.com.apk",
    "appPackage": "com.yerli.sosyal",
    "appActivity": "com.yerli.sosyal.activity.sign.SignGraphActivity",
    "noReset": True,
}


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)


el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ImageView")
el1.click()

el2 = driver.find_element(by=AppiumBy.ID, value="com.yerli.sosyal:id/edt_search")
el2.clear()
el2.send_keys("pmon_1")

el5 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[1]")
el5.click()

el6 = driver.find_element(by=AppiumBy.ID, value="com.yerli.sosyal:id/imgBtnUserProfileOtherSettings")
el6.click()

el7 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.cardview.widget.CardView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView")
el7.click()

el8 = driver.find_element(by=AppiumBy.ID, value="com.yerli.sosyal:id/edt_message_reply")
el8.send_keys("asdf")

el9 = driver.find_element(by=AppiumBy.ID, value="com.yerli.sosyal:id/btn_message_send")
el9.click()