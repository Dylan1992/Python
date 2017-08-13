str = input("请输入您猜测的数字:");
stmp = int(str);

if(stmp == 8):
    print("恭喜您猜对了");
else:
    if(stmp>8):
        print("您猜的数字大了");
    else:
        print("您猜的数字小了");
print("游戏结束");
