#!/usr/bin/env python
# encoding: utf-8
"""
外观模式(门面模式)

为子系统中的一组接口提供一个一致的界面.
定义了一个高层接口, 是的这一子系统更加容易使用

- 统一接口人
- 减少依赖
"""


class SystemA(object):
    def call_a(self):
        print("call a")


class SystemB(object):
    def call_b(self):
        print("call b")


class SystemC(object):
    def call_c(self):
        print("call c")


class Facade(object):
    def __init__(self):
        self.sys_a = SystemA()
        self.sys_b = SystemB()
        self.sys_c = SystemC()

    def action_a(self):
        self.sys_a.call_a()
        self.sys_b.call_b()

    def action_b(self):
        self.sys_b.call_b()
        self.sys_c.call_c()


if __name__ == '__main__':
    facade = Facade()
    facade.action_a()
