# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 13:48:28 2017
作者: 星空飘飘
平台：Anaconda 3-5.1.0
语言版本：Python 3.6.4
编辑器：Spyder 3.2.6
分析器：Pandas: 0.22.0
解析器：lxml: 4.1.1
数据库：MongoDB 2.6.12
程序名：whatday.py
"""


import time
import datetime

if __name__ == '__main__':
    today = time.strftime("%w")  # 获取今天星期几
    anyday = datetime.datetime(2008, 8, 8).strftime("%w")  # 获取指定那天星期几
    print('今天星期:{0};星期:{1}' .format(today, anyday))
