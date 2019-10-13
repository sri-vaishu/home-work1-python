HOME WORK1


Module: introduction
1 Say “hello world” with python
print("Hello, World!")

2  PYTHON IF ELSE
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip())
if(n % 2 == 0 ):
    if((n >= 2 and n <= 5) or n > 20):
        print("Not Weird")
    else:
3 ARITHMETIC OPERATORS
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

print(a+b)
print(a-b)
print(a*b)

4 PYTHON: DIVISION
if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a//b)
    print(a/b)
    5 LOOPS
if __name__ == '__main__':
    n = int(raw_input())

i = 0

while i<n:
    print(i**2)
    i = i+1
6 WRITE A FUNCTION
def is_leap(year):
    leap = False
    
    if (year % 400 == 0):
        leap = True
    elif ((year % 4 == 0) and (year % 100 != 0)):
        leap = True

    return leap



7 PRINT FUNCTION
if __name__ == '__main__':
    n = int(input())
for i in range(0, n):
    print(i+1, end= '')

MODULE: BASIC DATA TYPES
8 FIND THE RUNNER UP SCORE
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

arr = set(arr)

arr1 = sorted(arr, reverse = True)

print(arr1[1])

9 NEST LISTS

n=int(input())
x=[]
for i in range(n):
    a=input()
    b=float(input())
    x.append([a,b])
x=sorted(x,key=lambda z: z[1])
zm=[]
for i in range(n):
    if x[i][1]<x[i+1][1]:
        c=x[i+1][1]
        for j in range(n-i):
            if x[i+j][1]==c:
                zm.append(x[i+j][0])
        zm=sorted(zm)
        for i in zm:
            print(i)
        break
10 FINDING THE PERCENTAGE
initial_input = int(input())
initial_set = {}
givennames = []
givenmarks = []
while initial_input > 0:
    initial_input = initial_input-1
    p,q,r,s = input().split()
    avg = float((float(q)+float(r)+float(s))/3)
    givennames.append(p)
    givenmarks.append(avg)
initial_set = dict(zip(givennames,givenmarks))
name = input()
if name in initial_set:
    print('%.2f' % (initial_set[name]))
  11 LISTS  
initial_list = []

n = int(input())
for i in range(n):
    t = input().split()
    if len(t) == 2:
        t[1] = int(t[1])
    if len(t) == 3:
        t[1] = int(t[1])
        t[2] = int(t[2])
        
    if t[0] == "append":
        initial_list.append(t[1])
    if t[0] == "insert":
        initial_list.insert(int(t[1]), t[2])
    if t[0] == "remove":
        initial_list.remove(t[1])
    if t[0] == "pop":
        initial_list.pop()
    if t[0] == "index":
        initial_list.index(t[1])
    if t[0] == "count":
        initial_list.count(t[1])
    if t[0] == "sort":
        initial_list.sort()
    if t[0] == "reverse":
        initial_list.reverse()
    if t[0] == "print":
        print(initial_list)




12 TUPLES
n = int(input())
x = input().split(" ")

for i in range(n):
    x[i] = int(x[i])

x = tuple(x)
print(hash(x))

MODULE: MATH

13 FIND ANGLE MBC
import math
AB = int(input())
BC = int(input())
deg = str(round(math.degrees(math.atan2(AB,BC))))
print(deg+'°')
14 TRIANGLE QUEST 2
for i in range(1,int(input())+1): 
    print ((int((10**i - 1) / 9))**2)
15 MOD DIVMOD
a = int(input())
b = int(input())

print(a//b)
print(a%b)
print(divmod(a,b))


16 POWER – MOD POWER
a = input();
b = input();
m = input();

a = int(a);
b = int(b);
m = int (m);

print(a**b);
print(pow(a,b,m));

17 INTEGERS COME IN ALL SIZES

a=int(input())
b=int(input())
c=int(input())
d=int(input())
print(pow(a,b)+pow(c,d))

18 TRIANGLE QUEST
for i in range(1,int(input())): 
    print(i*((10**i)-1)//9)
MODULE: STRING
19 STRING SPLIT AND JOIN
def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return(line)

20 CAPITALIZE
def solve(s):
    lzz = s.split(" ")
    led = []
    for i in range(len(lzz)):
        l1 = lzz[i].capitalize()
        led.append(l1)

    s = " ".join(led)

    return s
MODULE: DATE AND TIME
21TIME DELTA

import datetime as dt

n = int(input())

for i in range(0,n):
    end_time = input()
    start_time = input()
    start_t = dt.datetime.strptime(start_time, "%a %d %b %Y %H:%M:%S %z")
    end_t = dt.datetime.strptime(end_time, "%a %d %b %Y %H:%M:%S %z")
    print (abs(round((end_t - start_t).total_seconds())))

MODULE: ERRORS AND EXCEPTIONS
22 INCORRECT REGEX
import re
for _ in range(int(input())):
    s = input()
    try:
        s = re.compile(s)
        print('True')
    except:
        print('False')



