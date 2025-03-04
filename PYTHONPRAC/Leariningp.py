#simple month_sales pic
'''
import pandas as pd
import matplotlib.pyplot as plt
#a simple dataframe
data = {'Month': ['jan' , 'feb' , 'mar' , 'apr','may','jun'],
        'Sales_data':[1500,2400,3500,1000,2200,300]}
df = pd.DataFrame(data)
#print(df)
plt.plot(df['Month'], df['Sales_data'])
# 添加 x 轴标签
plt.xlabel('Month')
# 添加 y 轴标签
plt.ylabel('Sales_data')
# 添加图表标题
plt.title('Monthly Sales')
# 显示图表
plt.show()'''
#自动化脚本
'''Python在编写自动化脚本方面也非常有优势，其简洁的语法和强大的库支持，使得开发自动化脚本变得简单而高效。
常用库和工具
os：提供了丰富的操作系统功能，如文件和目录操作。
shutil：提供了高级的文件操作功能，如复制和移动文件。
requests：用于发送HTTP请求，适用于Web抓取和API调用。'''


