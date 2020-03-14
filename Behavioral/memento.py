#!/usr/bin/env python
# encoding: utf-8
"""
备忘录

在不破坏封装性的前提下, 捕获一个对象的内部状态, 并在该对象之外保存这个状态

这样以后可以将该对象恢复到原先保存的状态

- 将要保存的细节封装到memento中
- 比较适合功能比较复杂, 需要维护或记录属性的历史类, 或者需要保存部分属性
- 例如: 保存历史命令,  并执行撤销操作
- 备忘录可以把复杂的对象内部信息对其他对象屏蔽起来
"""


class Originator(object):
    """
    创建一个备忘录Memento, 用以记录当前时刻的内部状态, 并可以使用备忘录恢复内部状态
    """

    def __init__(self, state):
        self.__state = state

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value

    def create_memento(self):
        return Memento(self.__state)

    def set_memento(self, memento):
        self.__state = memento.state

    def show(self):
        print("State:", self.__state)


class Memento(object):
    """
    负责存储Originator的内部状态, 并可以防止除Originator以外的其他对象访问
    """
    def __init__(self, state):
        self.__state = state

    @property
    def state(self):
        return self.__state


class Caretaker(object):
    """
    负责保存好备忘录Memento
    """
    def __init__(self):
        self.__memento = None

    @property
    def memento(self):
        return self.__memento

    @memento.setter
    def memento(self, value):
        self.__memento = value


if __name__ == '__main__':
    o = Originator("init")
    o.show()
    o.state = "begin"
    o.show()

    mem = o.create_memento()

    # save it
    c = Caretaker()
    c.memento = mem

    o.state = "change"
    o.show()

    # recover
    o.set_memento(c.memento)
    o.show()
