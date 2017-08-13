import random
secret = random.randint(1,10);

print("while 的用法演示");
print(secret);
temp = input("请输入你猜测的数字:");
guess = int(temp);
counter = 0;
while guess!=secret and counter<2:
    print("您猜错了");
    temp = input("请重新输入你猜测的数字:");
    guess = int(temp);
    counter = counter+1;
    if guess == secret:
        print("恭喜您猜对了");
    else:
 
        if guess >secret:
            print("猜的数字大了");
        else:
            print("猜的数字小了");

print("游戏结束！");
