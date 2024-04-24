import time
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_scroll(self) -> None:
        el1 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                       value='new UiSelector().className("android.widget.ImageView").instance(4)')
        el2 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                       value='new UiSelector().className("android.widget.ImageView").instance(5)')
        self.driver.scroll(el1, el2)

    def test_drag_and_drop(self) -> None:
        self.driver.tap([(505, 725)])
        time.sleep(2)
        el1 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                       value='new UiSelector().resourceId("com.google.android.youtube:id/watch_while_time_bar_view")')

        el2 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                       value='new UiSelector().resourceId("android:id/navigationBarBackground")')

        self.driver.drag_and_drop(el1, el2)

    def test_tap(self) -> None:
        self.driver.tap([(133, 2276)])

    def test_swipe(self) -> None:
        self.driver.tap([(505, 725)])
        time.sleep(2)
        self.driver.swipe(18, 1014, 307, 1014)

    def test_flick(self) -> None:
        self.driver.flick(537, 1285, 537, 537)
        self.driver.flick(537, 1285, 537, 537)
        self.driver.flick(537, 1285, 537, 537)
        self.driver.flick(537, 1285, 537, 537)
        self.driver.flick(537, 1285, 537, 537)


if __name__ == '__main__':
    unittest.main()
