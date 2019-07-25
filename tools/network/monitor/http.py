#!usr/bin/python
#-*- coding:utf-8 _*-
"""
@author:wubinbin
@file: http.py
@time: 2019/06/26/16:04
"""
import sys, time, os, json,requests
reload(sys)
sys.setdefaultencoding('utf8')


def HttpMonitor(url):
    Hm_Status={}
    try:
        Url_Status = requests.get(url,timeout=1)  #限定超时时间
        Hm_Status['status']=Url_Status.status_code
        Hm_Status['retime']=Url_Status.elapsed.microseconds/1000  # 返回url响应时间，单位毫秒
    except:
        Hm_Status['status'] = 610  #请求超时错误代码
        Hm_Status['retime'] = '请求超时'
    return Hm_Status

print HttpMonitor("https://www.baidu.com")
