print("while 的用法演示");

temp = input("请输入你猜测的数字:");
guess = int(temp); 
while guess!=8:
    
    if guess >8 :
        print("猜的数字大了");
        temp = input("请重新输入你猜测的数字:");
        guess = int(temp); 
    else:
        print("猜的数字小了");
        temp = input("请重新输入你猜测的数字:");
        guess = int(temp); 
print("恭喜您猜对了！");
