#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# **********************************************************************
#
# Description: 测试云短信sdk接口
#
# Author: Peter Hu
#
# Created Date:2017/5/12
#
# Copyright (c) ShenZhen Montnets Technology, Inc. All rights reserved.
#
# **********************************************************************
import sys
from smsclient import *

def menu():
    print("""
usage:
1: singleSend
2: batchSend
3: multiSend
4: getMo
5: getRpt
6: getBalance
7: getRemain
x: exit
?: help

IMPORTANT:
If you wish the other pepole are able to recieve call or text,
Please change mobile(s) into their phone number by editting 'smsclient.py'
""")


class SmsApiDemo():
    def run(self, args):
        # 短信实例
        smsClient = SmsClient()

        menu()
        c = None
        while c != 'x':
            try:
                sys.stdout.write("==> ")
                sys.stdout.flush()
                c = sys.stdin.readline().strip()
                if c == '1':
                    # 请求提交短信(上行)
                    smsClient.singleSend()
                elif c == '2':
                    # 相同内容群发(短信)
                    smsClient.batchSend()
                elif c == '3':
                    # 个性化群发(短信)
                    smsClient.multiSend()
                elif c == '4':
                    # 获取上行(短信)
                    smsClient.getMo()
                elif  c == '5':
                    # 获取状态报告(短信)
                    smsClient.getRpt()
                elif c == '6':
                    # 查询剩余条数
                    smsClient.getBalance()
                elif c == '7':
                    # 查询剩余金额或条数
                    smsClient.getRemain()
                elif c == 'x':
                    pass # Nothing to do
                elif c == '?':
                    menu()
                else:
                    print("unknown command `" + c + "'")
                    menu()
            except EOFError:
                break
            except KeyboardInterrupt:
                break
        return

if __name__ == "__main__":
    app = SmsApiDemo()
    sys.exit(app.run(sys.argv))