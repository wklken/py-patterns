#!/usr/bin/env python
# encoding: utf-8
"""
单例模式

保证一个类仅有一个实例, 并提供一个访问他的全局访问点

TODO: 如果是多线程, 要考虑加锁
"""


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **
                                                                 kwargs)
        return cls._instances[cls]


#Python2
class MyClass(object):
    __metaclass__ = Singleton

if __name__ == '__main__':
    a = MyClass()
    b = MyClass()
    print a == b
    print a is b
