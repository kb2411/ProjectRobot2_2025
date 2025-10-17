from microbit import *
import robotbit

# 速度级别：0%, 20%, 40%, 60%, 80%, 100%
speed_levels = [0, 50, 100, 150, 200, 255]

display.show(Image.HAPPY)  # 显示笑脸表示程序启动

while True:
    for speed in speed_levels:
        # 设置左右电机速度
        robotbit.motor(1, speed)
        robotbit.motor(2, speed)
        sleep(1000)  # 每个速度运行1秒
    
    # 循环结束后重新开始
    robotbit.motor_stop()
    sleep(500)
