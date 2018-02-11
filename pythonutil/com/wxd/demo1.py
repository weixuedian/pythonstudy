#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# if

def ifdemo1():
    num = 6
    if num == 3:
        print('num3')
    elif num == 4:
        print('num4')
    elif num == 5:
        print('num5')
    elif num == 6:
        print('num6')
    elif num == 7:
        print('num7')
    else:
        print('else')


# 例3：if语句多个条件

def demoif3():
    num3 = 123
    if num3 > 0 and num3 <= 10:
        print('3 and 10')
    else:
        print('else')


def demoif4():
    num4 = 'a'
    if num4 == 'a' and num4 == 'b':
        print('hello')
    else:
        print('undefine')


def while4test():
    count = 0
    while (count <= 9):
        print('The count is:', count)
        count = count + 1
    print
    "Good bye!"


def continueBreak():
    i = 0
    while i < 10:
        i += 1;
        if (i % 2 == 1):
            continue
        print(i)


def foreverfor():
    var = 1
    while var == 1:  # 该条件永远为true，循环将无限执行下去
        num = input("Enter a number  :")
        print("You entered: ", num)

    print
    "Good bye!"


def for1():
    for letter in 'python':
        print('当前字母 :', letter)


def for2():
    fruits = ['banana', 'apple', 'mango']
    for fruit in fruits:
        print('当前水果 :', fruit)


def for3():
    fruits = ['banana', 'apple', 'mango']
    for index in range(len(fruits)):
        print(':', index)
        print(':::', fruits[index])


def sushu():
    i = 1;
    while (i < 100):
        j = 2
        while (j <= (i / j)):
            if not (i % j): break
            j = j + 1
        if (j > i / j):
            print('素数:', i)
        i = i + 1
    print('goods by ')


def xingta():
    # *字塔
    i = 1
    # j=1
    while i <= 9:
        if i <= 5:
            print("*" * i)

        elif i <= 9:
            j = i - 2 * (i - 5)
            print("*" * j)
        i += 1
    else:
        print("")
def maopao():
    array = [9, 2, 7, 4, 5, 6, 3, 8, 1, 10]
    L = len(array)
    for i in range(L):
        for j in range(L - i):
            if array[L - j - 1] < array[L - j - 2]:
                array[L - j - 1], array[L - j - 2] = array[L - j - 2], array[L - j - 1]
    for i in range(L):
        print(array[i])
# ifdemo1();
# demoif3()
# demoif4()
# while4test()
# continueBreak()
# foreverfor()
# for1()
# for2()
# for3()
#sushu()
#xingta();
maopao();

