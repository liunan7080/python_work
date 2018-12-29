#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# author:liuna
# datetime:2018/12/27 22:17
# software: PyCharm

import os
import time

def deldir(dir, inputtime):
    all = os.listdir(dir)
    tupletime = time.strptime(inputtime, "%Y-%m-%d %H:%M:%S")
    # print(all)
    print("-", end="")
    for a in all:
        a = os.path.join(dir, a)
        ctime = time.localtime(os.path.getctime(a))
        if os.path.isdir(a):
            # print("%-15s %-100s" % ("This is dir:", a))
            deldir(a, inputtime)
            if not os.listdir(a):
                print("\nit's an empty dir,delete    " + a)
                os.rmdir(a)
                with open('log.txt', 'a', encoding='UTF-8') as f:
                    f.write("\n已删除目录：" + a + "\n")

        elif os.path.isfile(a):
            # print("%-15s %-100s" % ("This is file:", a))
            if dir == "D:\python_work\爬虫入门":
                continue
            if ctime > tupletime:
                os.remove(a)
                print("delete file:" + a)
                with open('log.txt', 'a', encoding='UTF-8') as f:
                    f.write("已删除文件：" + a + "\n")

if __name__ == "__main__":
    dir = input("input dir:")
    if dir == "":
        dir = "D:\python_work\爬虫入门"
    inputtime = input("input time:")
    if inputtime == "":
        inputtime = "2018-12-18 15:40:40"
    deldir(dir, inputtime)
