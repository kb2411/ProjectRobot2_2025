from microbit import *
import robotbit

# 字母路径定义
letter_paths = {
    'L': ['forward', 'left'],
    'O': ['forward', 'right', 'backward', 'left'], 
    'D': ['forward', 'right', 'backward'],
    'Z': ['forward', 'right', 'forward', 'left']
}

current_letter = 'L'

def execute_path(letter):
    if letter not in letter_paths:
        return
    
    display.show(letter)
    sleep(1000)
    
    for action in letter_paths[letter]:
        if action == 'forward':
            display.show(Image.ARROW_S)
            robotbit.motor(1, 150)
            robotbit.motor(2, 150)
        elif action == 'backward':
            display.show(Image.ARROW_N) 
            robotbit.motor(1, -150)
            robotbit.motor(2, -150)
        elif action == 'left':
            display.show(Image.ARROW_E)
            robotbit.motor(1, 50)
            robotbit.motor(2, 150)
        elif action == 'right':
            display.show(Image.ARROW_W)
            robotbit.motor(1, 150)
            robotbit.motor(2, 50)
        
        sleep(1000)  # 每个动作执行1秒
        robotbit.motor_stop()
        sleep(200)   # 动作间短暂停顿

# 主程序循环
display.show(Image.HAPPY)

while True:
    # 按钮A切换字母
    if button_a.was_pressed():
        letters = list(letter_paths.keys())
        current_index = letters.index(current_letter)
        current_letter = letters[(current_index + 1) % len(letters)]
        display.show(current_letter)
        sleep(500)
    
    # 按钮B执行当前字母路径
    if button_b.was_pressed():
        execute_path(current_letter)
        display.show(current_letter)
    
    sleep(100)
