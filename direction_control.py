from microbit import *
import robotbit

# 方向控制序列：前、后、左、右、左旋、右旋
directions = [
    (Image.ARROW_S, 150, 150),   # 前进
    (Image.ARROW_N, -150, -150), # 后退  
    (Image.ARROW_E, 150, 50),    # 左转
    (Image.ARROW_W, 50, 150),    # 右转
    (Image.ARROW_SE, -150, 150), # 左旋
    (Image.ARROW_SW, 150, -150)  # 右旋
]

while True:
    for direction_img, left_speed, right_speed in directions:
        display.show(direction_img)
        robotbit.motor(1, left_speed)
        robotbit.motor(2, right_speed)
        sleep(1000)
    
    # 停止1秒后重新开始
    robotbit.motor_stop()
    sleep(1000)
