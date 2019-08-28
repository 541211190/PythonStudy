"""python 数据过滤
    列表数据过滤
    --------
           filter data from list

    字典数据过滤
    ---------
           filter data from dict

    集合数据过滤
    ---------
           filter data from collection
"""

from random import randint

# 列表数据过滤：生成一个长度为10的列表，每个数字在-10到10之间 (在循环体中，没有用到的变量，起名为“_”)
list1 = [randint(-10, 10) for _ in range(10)]

# 方式1：过滤列表，保留正数
res_list1 = [x for x in list1 if x >= 0]
print(res_list1)

# 方式2：filter方式
# filter 在python3中会返回一个生成器对象，将此对象传递给list的构造器，则可生成一个过滤后的列表
res_list2 = list(filter(lambda x: x >= 0, list1))
print(res_list2)

# 字典方式

# 创建字典
student_dict = {'student%d' % i: randint(50, 100) for i in range(1, 21)}
print(student_dict)

# 方式1：for循环筛选
res_dict = {k: v for k, v in student_dict.items() if v > 80}
print(res_dict)
# 方式2：filter方式筛选
dict_res2 = dict(filter(lambda item: item[1] > 80, student_dict.items()))
print(dict_res2)

# 集合过滤
collection = {randint(0, 20) for _ in range(20)}
res_collection = {x for x in collection if x % 3 == 0}
print(res_collection)
