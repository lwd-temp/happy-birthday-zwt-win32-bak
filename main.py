#coding:utf-8
# main.py
# happy-birthday-zwt-win32 项目的主程序代码
# Copyright © 2020 lwd-temp@Github.com. All rights reserved.
import time
import datetime
import os
import popup
from chwp import chwp
import info
import sys
import win32api,win32con,win32gui
import random

# 版本号发布之前改掉
version="beta"
stcuti=datetime.datetime.now()
strstcuti=str(stcuti.year)+"-"+str(stcuti.month)+"-"+str(stcuti.day)+"-"+str(stcuti.hour)+"-"+str(stcuti.minute)+"-"+str(stcuti.second)
logname="hbzwin32log-"+strstcuti
actstat=0 # 布尔 是否激活操作

def logit(msg):
    # 日志函数
    if info.log==1:
        with open(os.path.join(desktop,"logname"),"a") as logfile:
            content="["str(datetime.datetime.now())+"]"+str(msg)+"\n"
            logfile.write(content)

logit("日志开始")
logit("hbzwin32"+"版本"+version)
logit("日志文件"+logname)

def get_desktop():
    # 获取桌面路径
    key =win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',0,win32con.KEY_READ)
    return win32api.RegQueryValueEx(key,'Desktop')[0]
desktop=get_desktop()
logit("桌面路径"+desktop)

def msgbox(title,content):
    # win32api弹窗
    win32api.MessageBox(0,str(content),str(title),win32con.MB_OK | win32con.MB_ICONWARNING)
logit("弹窗函数定义完成")

#生成资源文件目录访问路径
def resource_path(relative_path):
    if getattr(sys, 'frozen', False): #是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
logit("资源文件路径处理完成")

# 确定日期时间是否符合info
nowtime=datetime.datetime.now()
nowmon=nowtime.month
nowday=nowtime.day
nowye=nowtime.year
if nowmon==info.actm:
    if nowday>=info.actd:
        actstat=1
if nowmon==info.month:
    if nowday<=info.day:
        actstat=1
if nowmon==info.dism:
    if nowday<=info.disd:
        actstat=1
if actstat=1:
    logit("行动开始")
else:
    logit("时辰未到，程序退出")
    exit()

# 计算剩余秒
strthe=str(nowye)+"-"+str(nowmon)+"-"+str(nowday)+" "+str(info.ah)+":"+str(info.am)+":"+"0.0"
thetime=datetime.datetime.strptime(strthe,"%Y-%m-%d %H:%M:%S.%f")
logit("行动时间"+str(thetime))
delta=(thetime-nowtime).seconds
logit("倒计时秒"+str(delta))
if delta<0:
    logit("负秒 重试 推迟24h")
    delta=delta+86400
    logit(str(delta))
logit("开始等待"+str(delta)+"秒")
time.sleep(delta)
logit("开始行动")









#访问res文件夹下defwp.jpg的内容
filename = resource_path(os.path.join("res","defwp.jpg"))
# https://www.cnblogs.com/darcymei/p/9397173.html