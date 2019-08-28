"""
为元组中每个元素命名提高可读性（三种方式）
"""

# 方式一：为索引定义变量名方式
from collections import namedtuple
from enum import IntEnum

NAME, AGE, ADDRESS = range(0, 3)
person = ("tom", "18", "china")
# 用别名代替索引（0,1,2），提高代码可读性
print(person[NAME] + "__" + person[AGE] + "__" + person[ADDRESS])


# 方式二：枚举

# 定义枚举类
class PersionEmun(IntEnum):
    NAME = 0
    AGE = 1
    ADDRESS = 2


# 使用枚举类
print(person[PersionEmun.NAME])

# 其中PersionEmun.NAME为数字0，验证如下：返回true,则为int类型
print(isinstance(PersionEmun.NAME, int))

# 方式三：使用标准库中的命名元组(推荐)
# 命名元组，就是为元组的每个元素起别名，命名元组是一个类的工厂，用来创建一个元组的子类
# 创建命名元组（参数1：要创建的子类元组类名；参数2：每个元素的名称列表）
Friend = namedtuple("Friend", ["name", "age", "addresss"])
# 用创建出的元组子类存储数据
friend_ = Friend("jack", "18", "US")
print(friend_)
# 命名元组仍然是元组类型
print(isinstance(friend_, tuple))
