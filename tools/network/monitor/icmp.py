#!usr/bin/python
#-*- coding:utf-8 _*-
"""
@author:wubinbin
@file: icmp.py
@time: 2019/06/26/16:04
"""
import sys, time, os, json,threading,pyping

reload(sys)
sys.setdefaultencoding('utf8')

def IcmpMonitor(ImIp): # tcp请求的函数 返回最大rtt值
    try:
        Im_MaxRtt=str(pyping.ping(ImIp).max_rtt)
        if Im_MaxRtt == 'timeout':
            return 0
        else:
            return Im_MaxRtt
    except:
        return 'timeout'

print  IcmpMonitor('192.168.2.1')
