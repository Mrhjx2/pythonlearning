#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Author: Hejx
#邮箱发送实例
def sendmail(r_user, content):
	try:
		import smtplib
		from email.mime.text import MIMEText
		from email.utils import formataddr

		msg = MIMEText(content, 'plain', 'utf-8')
		msg['From'] = formataddr(["Hejianxiong"], 'hjxhainan@163.com')
		msg['To'] = formataddr(["Hejx", '936971463@qq.com'])
		msg['Subject'] = "主题"

		server = smtplib.SMTP("smtp.163.com", 25)
		server.login("hjxhainan@163.com", "password")
		server.sendmail('hjxhainan@163.com', [r_user, ], msg.as_string())
		server.quit()
	except:   #发送失败执行
		return False
	else:   #发送成功执行
		return True

sendmail(r_user='936971463@qq.com', content='this is a text demo for python sendmail')