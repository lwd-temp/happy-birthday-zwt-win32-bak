#coding:utf-8
# info.py
# happy-birthday-zwt-win32 的配置文件和字符串常量
# https://github.com/lwd-temp/happy-birthday-zwt-win32
# Copyright © 2020 lwd-temp@Github.com. All rights reserved.
# 注意 所有变量修改后保持原变量类型
# 日志
log=1
# 调试选项 用于pyinstaller测试
debug=0
# 字符串常量 见下文
name="ZWT"
# 信息内容
msg="Happy Birthday "+name+"!"
# 标题 若可能
title="happy-birthday-zwt-win32"
# 月
month=5
# 日
day=5
# 提前生效月
activemonth=4
# 提前生效日
activeday=20
# 结束月
disactmonth=5
# 结束日
disactday=10
# 行动时 每日
acthour=14
# 行动分 每日
actmin=20
# 注意 生效日为闭区间
# 注意 提前生效月和结束月在程序中视为同一月 配置时必须注意必须填写同一月
# 这是一个逻辑错误但暂时不具备修改必要
# 用户附加内容 输出于说明文件 见下文
usercontent='''这是 happy-birthday-zwt-win32 项目的默认用户附加内容。
在构建发布版前更改 info.py 以修改此文本。
https://github.com/lwd-temp/happy-birthday-zwt-win32
Copyright © 2020 lwd-temp@Github.com. All rights reserved.'''
# 是否生成说明文件
createreadme=1




# 简化变量名 便于调用
actm=activemonth
actd=activeday
dism=disactmonth
disd=disactday
ah=acthour
am=actmin
# 字符串常量和其他说明文本 无需改动
copyright='''Copyright © 2020 lwd-temp@Github.com. All rights reserved.'''