import sys
import time
import uiautomator2 as u2

if __name__ == '__main__':

    d = u2.connect('emulator-5554')

    print(d.info)

    d.app_start('org.tasks')
    d.implicitly_wait(10)

    d(resourceId="org.tasks:id/fab").click()
    d.swipe_ext("up", 1.0)
    d.swipe_ext("up", 1.0)
    d.click(0.435, 0.312)

    d.click(0.082, 0.898)
d.click(0.068, 0.823)
d.click(0.69, 0.833)
d.click(0.053, 0.894)
d.click(0.09, 0.834)

d.click(0.401, 0.77)
d.click(0.746, 0.695)
d.click(0.885, 0.76)
d.click(0.255, 0.7)

d.click(0.082, 0.898)#最左下角
d.click(0.068, 0.823)#=\<
d.click(0.802, 0.828)

d.click(0.072, 0.83)
d.click(0.756, 0.768)
d.click(0.072, 0.897)

d.click(0.401, 0.77)#f
d.click(0.746, 0.695)#i
d.click(0.885, 0.76)#l
d.click(0.255, 0.7)#e

d.click(0.053, 0.894)
d.click(0.491, 0.824)

d.click(0.931, 0.76)#/
d.click(0.931, 0.76)#/
d.click(0.931, 0.76)#/

d.click(0.082, 0.898)#最左下角
d.click(0.206, 0.762)#s
d.click(0.454, 0.699)#t
d.click(0.851, 0.691)#o
d.click(0.345, 0.686)#r
d.click(0.104, 0.752)#a
d.click(0.498, 0.749)#g
d.click(0.255, 0.7)#e

d.click(0.082, 0.898)#最左下
d.click(0.931, 0.76)#/
d.click(0.082, 0.898)#最左下角
d.click(0.255, 0.7)#e
d.click(0.798, 0.843)#m
d.click(0.644, 0.702)#u
d.click(0.885, 0.76)#l
d.click(0.104, 0.752)#a
d.click(0.454, 0.699)#t
d.click(0.255, 0.7)#e
d.click(0.301, 0.768)#d
d.click(0.082, 0.898)#最左下
d.click(0.931, 0.76)#/
d.click(0.944, 0.684)#0
d.click(0.931, 0.76)#/
d.click(0.082, 0.898)#最左下
d.click(0.454, 0.699)#t
d.click(0.255, 0.7)#e
d.click(0.206, 0.762)#s
d.click(0.454, 0.699)#t
d.click(0.746, 0.695)#i
d.click(0.705, 0.822)#n
d.click(0.498, 0.749)#g
d.click(0.8, 0.906)#.
d.click(0.454, 0.699)#t
d.click(0.309, 0.833)#x
d.click(0.454, 0.699)#t
d.click(0.082, 0.898)#最左
d.click(0.829, 0.76)#)

d(description="Save").click()
d(resourceId="org.tasks:id/description", text="File").click()
d(resourceId="android:id/text1", text="Open").click()

   # d.app_stop('org.tasks')