tempstr = input('请输入带有符号的温度值：')
temp = int(tempstr[0:-1])
if tempstr[-1] in ['f','F']:
    c = (temp - 32)/1.8
    print('转换后的温度是%dC' % c)
elif tempstr[-1] in ['c','C']:
    f = 1.8*temp+32
    print('转换后的温度是%dF' % f)
else:
    print('你是大傻子')