#!/usr/bin/env python
# encoding: utf-8
"""
适配器模式,也称为wrapper模式, 包装的意思

将一个类的接口转换成客户希望的另一个接口.
使得原本由于接口不兼容而不能work的那些类可以work. 用于填补'现有功能'和'所需功能'之间差异

- 适用: 系统的数据和行为都正确, 但是接口不符时. (已存在, 但是其接口和需要的不同)
- 适用: 当前现有的已经被充分测试, 并且已经被其他很多系统调用, 此时不宜修改, 但是又必须加入新功能用于满足某些需求
- 主要用于, 希望复用一些现存的类, 但接口又与复用环境要求不一致的情况
- 客户代码可以统一调用同一接口, 简单直接紧凑
- 可以再完全不改变现有代码的前提下, 使现有代码适配于新的接口

比喻:
    - 笔记本使用的是12V, 而外部电源有100-220v 不同的, 此时需要一个电源适配器, 对电源进行适配

实现:
- 类适配模式(使用继承)
- 对象适配模式(使用委托)

在重构中的应用:
调用了第三方系统, 例如redis/elasticsearch/requests库等, 都有自己独立的库,
但是, 基本封装并不足以满足现有的业务需求
此时, 可以封装一个 XXClient, 将原来接口再封装, 实现依赖相关的业务逻辑
最终, 外部系统只需要调用 XXClient 即可, 业务逻辑都被封装(也有点facade模式的意思)
"""

# 基于继承的

from abc import ABCMeta, abstractmethod


class Adaptee(object):
    """
    需要适配的类, 需要被被适配的
    """

    def special_request(self):
        print("I am special")


class Target(metaclass=ABCMeta):
    """
    客户锁期待的接口, 目标可以使具体或抽象的类, 也可以是接口
    """
    @abstractmethod
    def request(self):
        pass


class Adapter(Target):
    """
    适配器, 通过在内部包装一个adapter对象, 把源接口转换成目标接口
    """

    def __init__(self):
        self.adaptee = Adaptee()

    def request(self):
        self.adaptee.special_request()


if __name__ == '__main__':
    a = Adapter()

    a.request()
