'''
Calculate a+b and output the sum in standard format -- that is, the digits must be separated into groups of three by commas (unless there are less than four digits).

Input Specification:
Each input file contains one test case. Each case contains a pair of integers a and b where −10
​6
​​ ≤a,b≤10
​6
​​ . The numbers are separated by a space.

Output Specification:
For each test case, you should output the sum of a and b in one line. The sum must be written in the standard format.

Sample Input:
-1000000 9
Sample Output:
-999,991
'''

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
