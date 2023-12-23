import sys
import time
import uiautomator2 as u2

if __name__ == '__main__':

    d = u2.connect('emulator-5554')

    print(d.info)

    d.app_start('org.tasks')
    d.implicitly_wait(10)

    d.click(0.072, 0.952)
    d.swipe_ext("up", 1.0)
    d.swipe_ext("up", 1.0)
    d.swipe_ext("up", 1.0)
    d.swipe_ext("up", 1.0)

    d.xpath('//*[@resource-id="android:id/content"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[15]').click()
    d(resourceId="android:id/title", text="Date and time").click()
    d(resourceId="android:id/title", text="Time picker mode").click()
    d(resourceId="android:id/text1", text="Text").click()
    d.click(0.065, 0.094)
    # d(resourceId="android:id/button2").click()
    d.click(0.063, 0.097)
    d.click(0.063, 0.097)
    d(resourceId="org.tasks:id/fab").click()
    d(text="No start date").click()
    d.implicitly_wait(3)
    d(resourceId="org.tasks:id/cancel_button").click()
    d(description="Save").click()
    d.click(0.072, 0.952)
    d.swipe_ext("up", 1.0)
    d.swipe_ext("up", 1.0)
    d.swipe_ext("up", 1.0)
    d.swipe_ext("up", 1.0)
    d.xpath('//*[@resource-id="android:id/content"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[15]').click()
    d(resourceId="android:id/title", text="Date and time").click()
    d(resourceId="android:id/title", text="Time picker mode").click()
    d(resourceId="android:id/text1", text="Clock").click()
    d.click(0.065, 0.094)
    # d(resourceId="android:id/button2").click()
    d.click(0.063, 0.097)
    d.click(0.063, 0.097)
    d(resourceId="org.tasks:id/fab").click()
    d(text="No start date").click()
    d.implicitly_wait(3)
    d(resourceId="org.tasks:id/cancel_button").click()
    # d.app_stop('org.tasks')