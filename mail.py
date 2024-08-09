# coding:utf-8
# 发送邮件模块
# 参考https://zhuanlan.zhihu.com/p/24180606


import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os


# 发送邮件
def sentMail(title, content):
    # 加载用户名和密码
    load_dotenv()
    username = "改成你自己的"
    # authcode = os.getenv("AUTHCODE")
    authcode = "改成你自己的"
    senderAddress = username+"@改成你自己的.com"
    #print("测试", username, authcode, senderAddress)
    # 设置服务器所需信息
    mail_host = "改成你自己的"
    # 用户名
    mail_user = username
    # 密码
    mail_pass = authcode
    # 邮件发送方地址
    sender = senderAddress
    # 接收方地址
    receivers = ["改成你自己的@改成你自己的"]
    
    # 设置邮件信息
    # 邮件内容
    message = MIMEText(content, 'plain', 'utf-8')
    # 邮件主题
    message['Subject'] = title
    # 发送方信息
    message['From'] = sender 
    # 接受方信息     
    message['To'] = receivers[0]
    
    # 登陆并发送邮件
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        # 连接到服务器
        # smtpObj.connect(mail_host, 465)
        # 登录到服务器
        smtpObj.login(mail_user,mail_pass) 
        # 发送
        smtpObj.sendmail(
            sender,receivers,message.as_string()) 
        # 退出
        smtpObj.quit() 
        print('发送成功')
    except smtplib.SMTPException as e:
        print('发送错误', e) #打印错误


if __name__ == "__main__":
    sentMail("测试", "这又是一封通过python发送的测试邮件。")
    
