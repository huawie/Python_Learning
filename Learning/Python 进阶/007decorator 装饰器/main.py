#!/usr/bin/python
#-*-coding:utf-8-*-
# import sys
# reload(sys)   #python3 不支持这种
# sys.setdefaultencoding('utf8')
from functools import wraps
import time

def test_demo1():#函数的嵌套
    print("test_demo1() function")
    def greet():
        return "test_demo1——greet() function"
    def welcome():
        return "test_demo1——welcome() function"
    print(greet())
    print(welcome())
    print("test_demo1() function")

def test_demo2(name=""):#从函数中返回
    def greet():
        return "greet() function"

    def welcome():
        return "welcome() function"

    if name == "greet":
        return greet
    else:
        return welcome

def function1():
    print("I am function1()")
    return "hihi haha"

def test_demo3(func):#函数作为参数传递
    print(func())

def test_decorator_demo1(function):
    def wrapTheFunction():
        print("--in--")
        function()
        print("--out--")
    return wrapTheFunction


def test_decorator_demo2(function):
    @wraps(function)
    def wrapTheFunction():
        print("--in--")
        function()
        print("--out--")
    return wrapTheFunction

def decorator_calc_cost_time(func):
    start_time = time.time()
    @wraps(func)
    def decorated(*args,**kwargs):
        res = func(*args,**kwargs)
        print("%.3fs"%(time.time()-start_time))
        return res
    return decorated


#这就是一个装饰器
@test_decorator_demo1
def function2():
    print("I am function2()")

#这就是一个装饰器
@test_decorator_demo2
def function3():
    print("I am function3()")


#这就是一个装饰器
@decorator_calc_cost_time
def function3(a,b):
    print("I am function3()")
    time.sleep(a*b)




def main():
    # test_demo1()

    # for x in ["greet","welcome"]:
    #     f = test_demo2(x)
    #     print("{0}: {1} vs {2}".format(x,f(),test_demo2(x)()))

    # test_demo3(function1)

    # f = test_decorator_demo1(function1)#执行外围的函数
    # f()#执行function1函数
    # f()

    # function2()
    # print(function2.__name__) #发现这里的输出为wrapTheFunction 而不是funciton2,即wrapTheFunction替换了原有的函数名字和注释文档(docstring)
    # print(function1.__name__)
    #
    # #解决上面的的问题，可以采用functools.wraps来实现
    # function3()
    # print(function3.__name__) #发现这里的输出为wrapTheFunction 而不是funciton2,即wrapTheFunction替换了原有的函数名字和注释文档(docstring)
    # print(function2.__name__)
    #
    #
    function3(2,1)


if __name__ == "__main__":
    main()

