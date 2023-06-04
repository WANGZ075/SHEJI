import time

def timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print(f"倒计时时间还有 {seconds} 秒")
        time.sleep(1)
        seconds -= 1
    print("时间到！")

minutes = int(input("请输入专注时间（分钟）："))
timer(minutes)
