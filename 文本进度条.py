import time
scale = 3    #进度条精度，简单看就是中间小圆点的个数
print("--------执行开始---------")
for i in range(scale + 1):
    a, b = '.' * i, ' ' * (scale - i)
    print("\rStarting {}{} Done!".format(a, b),end = '')
    time.sleep(0.1)  #增大挂起时间，看着有模拟效果
print()
print("--------执行结束----------")
