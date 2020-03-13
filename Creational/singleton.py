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
    def __init__(self, *args, **kwargs):
        self.__instance = None

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance=super().__call__(*args,**kwargs)
            return self.__instance
        else:
            return self.__instance


# Python3
class MyClass(metaclass=Singleton):
    pass


if __name__ == '__main__':
    a = MyClass()
    b = MyClass()
    print(a == b)
    print(a is b)
    print(a,b)

