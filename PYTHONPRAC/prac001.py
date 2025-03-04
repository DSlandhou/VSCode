'''
print("HEllo,world")

import math 
for i in range(1,19):
    b = math.sqrt(i)
    print(b**2)'''
#复数会有括号
#print(2+3j,type(1+2j))
#print('python'in 'i love python')
#print(len('i love python'))
'''
str1 = 'i love python'
print(str1.upper())
print(str1.lower())'''

#格式化字符串
'''
name = 'ALICE WANG'
I_Welcome_statement = f'hello,{name}!!!!'
print(I_Welcome_statement)'''

#print(type((1,2,3,4,'six')))#元组tuple里的元素不可变

'''
my_tuple = (1, 2, 3, 'Python', 3.14)
# 元组解包
a, b, c, d, e = my_tuple
print(a, b, c, d, e)  # 输出: 1 2 3 Python 3.14
'''
#字典
'''
my_dict = {'name':'python',
           'version':'3.12',
           'control':'conda',
           'platform':'jupyter notebook'}
#print(my_dict,type(my_dict))
#print(my_dict['version'])
my_dict['friend'] = 'c'
del my_dict['friend'] #删除元素在字典里的

print(my_dict.keys())#获取所有键
print(my_dict.values())#获取所有值
print(my_dict.items())#获取所有键值对
'''
#集合
'''
print({1,2,3,4,5},type({1,2,3,4}))
lst = [1,2,2,3]
my_set01=set(lst)#集合具有去重性
print(my_set01)
char_set01 = set("fuck you")

char_set01.add('123')
print(char_set01)
char_set01.remove(' ')
print(char_set01)

# 集合运算
print(my_set01 & char_set01)  # 交集
print(my_set01 | char_set01)  # 并集
print(my_set01 - char_set01)  # 差集
print(my_set01 ^ char_set01)  # 对称差集
'''
"""Sum = sum([1,2,3,4,54])
print(Sum)"""
