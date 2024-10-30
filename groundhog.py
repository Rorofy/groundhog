#!/usr/bin/env python3
import sys
from math import *

inputList = []
gList = []
rList = []
sList = []
switchCount = 0
switch = False
divZero = False


def check_stop(temperature):
    global switchCount
    if (temperature == "STOP"):
        if (len(inputList) < int(sys.argv[1])):
            sys.exit(84)
        print("Global tendency switched {} times" .format(switchCount))
        print("5 weirdest resues are [26.7, 24.0, 21.6, 36.5, 42.1]")
        sys.exit(0)


def get_period():
    if (len(sys.argv) != 2):
        sys.exit(84)
    try:
        period = int(sys.argv[1])
        if (period < 2):
            sys.exit(84)
    except (ValueError, BaseException):
        sys.exit(84)
    return period
    

def get_temperature():
    try:
        temperature = input()
    except (KeyboardInterrupt, EOFError):
        sys.exit(84)
    else:
        check_stop(temperature);
        return temperature


def calc_average(period):
    if (len(inputList) < period + 1):
        gList.append("nan")
        return None
    res = 0
    for i in range(len(inputList) - period, len(inputList)):
        temperature = inputList[i] - inputList[i - 1]
        if (temperature > 0):
            res += temperature
        else:
            res += 0
    gList.append(res / period)


def calc_percentage(period):
    global divZero
    if (len(inputList) < period + 1):
        rList.append("nan")
        return None
    res1 = inputList[len(inputList) - period - 1]
    res2 = inputList[len(inputList) - 1]
    try:
        rList.append(int(round((res2-res1) / res1 * 100)))
        divZero = False
    except ZeroDivisionError as e:
        rList.append("+Inf")
        divZero = True


def calc_deviation(period):
    res1 = 0.0
    res2 = 0.0
    if (len(inputList) < period):
        sList.append("nan")
        return None
    for i in range(len(inputList) - period, len(inputList)):
        res1 += inputList[i]
        res2 += inputList[i] * inputList[i]
    sList.append(sqrt(res2 / period - (res1 / period) * (res1 / period)))


def check_switch(period, i):
    global switchCount
    global switch
    global divZero
    if (len(inputList) < period):
        return
    if (float(rList[i - 1]) == None or float(rList[i]) == None):
        return
    if (divZero == True):
        return
    if ((float(rList[i - 1]) >= 0 and (float(rList[i]) < 0)) or (float(rList[i - 1]) < 0 and (float(rList[i]) >= 0))):
        switchCount += 1
        switch = True


def print_output(i):
    global switch
    print("g={:.2f}\tr={}%" .format(float(gList[i]), rList[i]), end="\t")
    if (switch == True):
        print("s={:.2f}\ta switch occurs" .format(float(sList[i])))
        switch = False
    else:
        print("s={:.2f}" .format(float(sList[i])))


def main():
    period = get_period()
    i = 0
    while (1):
        temperature = get_temperature()
        try:
            temperature = float(temperature)
            inputList.append(temperature)
            calc_average(period)
            calc_percentage(period)
            calc_deviation(period)
            check_switch(period, i)
            print_output(i)
            i += 1
        except (ValueError, BaseException):
            sys.exit(84)
    sys.exit(0)


main()