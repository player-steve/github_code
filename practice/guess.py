x = 24#预设的数
judgement = False
while judgement == False:
    y = input('来猜一猜吧～')
    y = int(y)
    if y < x:
        print('猜小了哦～')
    elif y == x:
        print('太棒了，你猜对了～')
        judgement = True
    else:
        print('猜大了哦～')