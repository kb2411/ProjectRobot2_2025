from microbit import *
import robotbit

display.show(Image.ARROW_S)

# 设置电机速度前进（速度值150）
robotbit.motor(1, 150)  # 电机1前进
robotbit.motor(2, 150)  # 电机2前进

# 运行2秒
sleep(2000)

# 停止电机
robotbit.motor_stop()
