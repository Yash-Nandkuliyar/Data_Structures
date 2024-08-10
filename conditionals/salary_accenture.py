from os import *
from sys import *
from collections import *
from math import *

def totalSalary(basic, grade):
    if grade == 'A':
        allowance = 1700
    elif grade == 'B':
        allowance = 1500
    elif grade == 'C':
        allowance = 1300
    hra = float(basic)*20/100
    da = float(basic)*50/100
    pf = float(basic)*11/100
    totalsalary = float(basic + hra + da + allowance - pf)
    totalsalary += 1/ (10**7) 
    ans = round(totalsalary)
    return ans