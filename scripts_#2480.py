import sys
import time
import uiautomator2 as u2

if __name__ == '__main__':

    d = u2.connect('emulator-5554')

    print(d.info)

    d.app_start('org.tasks')
    d.implicitly_wait(10)

    d(resourceId="org.tasks:id/fab").click()
    d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_0_4"]/android.widget.TextView[1]').click()
    d.xpath('//*[@resource-id="org.tasks:id/compose_view"]/android.view.View[1]/android.view.ViewGroup[2]').click()
    d(resourceId="android:id/text1", text="Custom…").click()


   # d.app_stop('org.tasks')