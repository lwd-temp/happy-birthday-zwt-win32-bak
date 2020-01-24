#coding:utf-8
# main.py
# happy-birthday-zwt-win32 项目的主程序代码
# https://github.com/lwd-temp/happy-birthday-zwt-win32
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
logname="hbzwin32log-"+strstcuti+".txt"
actstat=0 # 布尔 是否激活操作

def get_desktop():
    # 获取桌面路径
    key =win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',0,win32con.KEY_READ)
    return win32api.RegQueryValueEx(key,'Desktop')[0]
desktop=get_desktop()

def logit(msg):
    # 日志函数
    if info.debug==1:
        print(str(msg))
    if info.log==1:
        with open(os.path.join(desktop,logname),"a") as logfile:
            content="["+str(datetime.datetime.now())+"]"+str(msg)+"\n"
            logfile.write(content)

logit("日志开始")
logit("hbzwin32"+"版本"+version)
logit("日志文件"+logname)

logit("桌面路径"+desktop)

def msgbox(title,content):
    # win32api弹窗
    win32api.MessageBox(0,str(content),str(title),win32con.MB_OK)

#生成资源文件目录访问路径
def resource_path(relative_path):
    if getattr(sys, 'frozen', False): #是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def donothing():
    # 什么都不做
    logit("什么都不做")

def actmsg():
    # 行动 弹窗
    logit("弹窗5次")
    for i in range(1,6):
        msgbox(info.title,info.msg)

def actpop():
    # 行动 气泡
    logit("持续60s气泡")
    bubble=popup.MainWindow()
    for i in range(1,21):
        bubble.startBubble(info.title,info.msg)

def actwp():
    # 行动 壁纸
    logit("更改壁纸")
    chwp(resource_path(os.path.join("res","wp.jpg")))

# 确定日期时间是否符合info
nowtime=datetime.datetime.now()
nowmon=nowtime.month
nowday=nowtime.day
nowye=nowtime.year
# 逻辑不严密 需要重写 暂时符合需求
if nowmon==info.actm:
    if nowday>=info.actd:
        actstat=1
if nowmon==info.month:
    if nowday<=info.day:
        actstat=1
if nowmon==info.dism:
    if nowday<=info.disd:
        actstat=1
if nowmon>info.actm:
    if nowmon<info.dism:
        actstat=1
if actstat==1:
    logit("行动开始")
else:
    logit("日期未到，程序退出")
    sys.exit()

# 计算剩余秒
strthe=str(nowye)+"-"+str(nowmon)+"-"+str(nowday)+" "+str(info.ah)+":"+str(info.am)+":"+"0.0"
thetime=datetime.datetime.strptime(strthe,"%Y-%m-%d %H:%M:%S.%f")
logit("预计行动时间"+str(thetime)+"，若已过则推迟至明日")
delta=(thetime-nowtime).seconds
logit("倒计时"+str(delta)+"秒")
time.sleep(delta)
logit("开始行动")

num=random.randint(0,100)
# 随机方案
if num==0:
    donothing()
if num>=1:
    if num<=20:
        actmsg()
        msgboxact=1
if num>=21:
    if num<=70:
        actpop()
        popact=1
if num>=71:
    if num<=100:
        actwp()
        wpact=1

#写说明
if info.readme==1:
    logit("写入说明文件")
    with open(resource_path(os.path.join("res","LICENSE")),"r",encoding="utf-8") as licensefile:
        license=licensefile.read()
    readmepath=os.path.join(desktop,"HBZWin32说明文件.txt")
    with open(readmepath,"a",encoding="utf-8") as fileobj:
        fileobj.write(info.usercontent+"\n")
        fileobj.write(info.copyright+"\n")
        fileobj.write(info.aboutpy+"\n")
        if wpact==1:
            fileobj.write(info.aboutwp+"\n")
        fileobj.write(license+"\n")
