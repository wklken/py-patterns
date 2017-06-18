#!/usr/bin/env python
# encoding: utf-8
"""
单例模式

保证一个类仅有一个实例, 并提供一个访问他的全局访问点

- 确保任何情况下绝对只有一个实例

坑:

- 多进程, 要考虑加锁
- web时, 往往是多进程起
- web时, 扩容时还往往是多机器多实例
"""


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# Python2
class MyClass(object):
    __metaclass__ = Singleton


if __name__ == '__main__':
    a = MyClass()
    b = MyClass()
    print a == b
    print a is b
