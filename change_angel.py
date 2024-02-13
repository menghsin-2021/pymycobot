from pymycobot.mycobot import MyCobot
'''
send_angle(id, degree, speed) : 関節の角度の変更
・id : 関節ID (genre.Angle, int, 1〜6)
・degree : 関節の角度 (float, -170～170)
・speed : 速度 (int, 0~100)
'''

from pymycobot.genre import Angle
from port_setup import setup
import time

mycobot = setup()
mycobot.send_angle(Angle.J1.value, -10, 60)
time.sleep(2)  # 等2秒
mycobot.send_angle(Angle.J2.value, 30, 80)
time.sleep(1)  # 等1秒
mycobot.send_angle(Angle.J2.value, -30, 80)
time.sleep(1)  # 等1秒
mycobot.send_angle(Angle.J2.value, 30, 80)
time.sleep(1)  # 等1秒
mycobot.send_angle(Angle.J2.value, -30, 80)
time.sleep(1)  # 等1秒
mycobot.send_angle(Angle.J3.value, 30, 60)
time.sleep(2)  # 等2秒
mycobot.send_angle(Angle.J4.value, 30, 60)
time.sleep(2)  # 等2秒
mycobot.send_angle(Angle.J5.value, 30, 60)
time.sleep(2)  # 等2秒
mycobot.send_angle(Angle.J6.value, 30, 60)
time.sleep(2)  # 等2秒
mycobot.send_angles([0,0,0,0,0,0], 60)