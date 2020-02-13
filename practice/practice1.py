""" 
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
 """

 # -*- coding: utf-8 -*-

name = input('your name:')
height = input('your height:')
weight = input('your weight:')
height = float(height)
weight = float(weight)
BMI =  weight/height**2
if BMI < 18.5:
    print('%s,you are underweight' % name)
elif BMI < 25:
    print('%s,you are health' % name)
elif BMI < 28:
    print('sorry,%s,you are overweight' % name)
elif BMI < 32:
    print('sorry,%s,you are obese' % name)
else:
    print('sorry,%s,you are severe obese' % name)