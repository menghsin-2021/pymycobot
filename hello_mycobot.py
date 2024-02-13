from pymycobot.mycobot import MyCobot
'''
set_color(r, g, b) : LEDの色の変更。
・r : 赤 (0~255)
・g :緑 0~255)
・b : 青 (0~255)
'''

from port_setup import setup
mycobot = setup()
mycobot.set_color(0, 255, 0)