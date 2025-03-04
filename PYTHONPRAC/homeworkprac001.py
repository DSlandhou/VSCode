#a,b,c=10.8,12.2,0.2
'''total = 10.8+12.2+0.2
print(total)
print(type(total))
print(int(total))
print(type(int(total)))'''
#a = 4 **( 3 ** 2)
#import math
#print(27 // 2 )

#print('int(5.2)', 'truncates 5.2 to', int(5.2))
'''
print("""This is a lengthy
multiline string containing
a few lines \
of text""")'''

'''
import math

pi = math.pi

n=0xfff

print("Hex=%x, Dec=%d, Oct=%o"%(n,n,n))
print("%3.3d"%pi)
print("%3.3f"%pi)'''

#线性回归
'''
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 生成数据
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # 生成输入特征X，reshape(-1, 1)将数组转换成一列
y = np.array([2, 3, 5, 6, 5])  # 生成目标变量y

# 创建线性回归模型并训练
model = LinearRegression()  # 创建线性回归模型
model.fit(X, y)  # 使用输入特征X和目标变量y训练模型

# 预测
y_pred = model.predict(X)  # 使用训练好的模型预测输出

# 绘制结果
plt.scatter(X, y, color='blue')  # 绘制散点图，用蓝色表示
plt.plot(X, y_pred, color='red')  # 绘制拟合直线，用红色表示
plt.xlabel('X')  # 设置x轴标签
plt.ylabel('y')  # 设置y轴标签
plt.title('Linear Regression Example')  # 设置图表标题
plt.show()  # 显示图表
'''
for i in range(6):
    for j in range(2):
        print("_", end="")
    print()
