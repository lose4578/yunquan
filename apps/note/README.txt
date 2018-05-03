操作系统：windows
python版本:2.7
第3方开源库:requests 2.14.1(相邻低版本也可以)


Step1: 安装python2.7
Step2: 安装requests
Step3: 按注释提示修改smsclient.py中的发送者帐号，密码和接收者的手机号码，体验demo。


//////////////////////////////////////////////////////////////////
安装requests 
方法一、
直接在PyCharm中安装requests,File-->Settings-->Project:Project Interpreter-->点击右侧'+'号，
在弹出的窗口界面中输入:requests，按提示自动安装。

方法二、
源代码安装requests
1) 网上下载并解压requests源码。
2）进入解压目录。
$ python setup.py install

具体请参照：https://pypi.python.org/pypi/requests


//////////////////////////////////////////////////////////////////
运行demo:
$ python test.py




