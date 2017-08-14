bingo = "结束了"
example = input("请输入一句话以结束游戏：");

while True:
    if example == bingo:
        break
    else:
        example = input("输入错误，请重新输入:");
print("游戏结束");
