#  !/usr/bin/env  python
#  -*- coding:utf-8 -*-
# @Time   :  2019/7/20
# @Author :  xuwei
# @Email  :  mrwaynexue@126.com
# @Note   :
def num2std(num):
    numstr = str(num)
    n = len(numstr)
    numout = ''
    if num>0:
        for i in range(n):

            if (n-i)%3==0 and i>0:
                numout += ','
            numout += numstr[i]
    else:
        for i in range(n):
            if(n-i)%3==0 and i>1:
                numout +=','
            numout += numstr[i]
    print(numout)


if __name__=='__main__':
    raw = input()
    data = raw.split()
    a = int(data[0])
    b = int(data[1])
    c = a+b
    num2std(c)
