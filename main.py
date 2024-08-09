# 定时检测某个网页是否有更新


import requests
import os
from apscheduler.schedulers.blocking import BlockingScheduler
import time
import mail
from fuzzywuzzy import fuzz

t = 0


# 爬取网页
def getSite(url):
    try:
        res = requests.get(url)
        res.raise_for_status()
    except:
        print("爬取网页错误")
        return None
    else:
        return res.text
        
        
    
# 比较网页数据是否一致getSite(url)
def compareData(url):
    global t
    t += 1
    if os.path.exists("data.txt") == False:
        siteData = getSite(url)
        with open("data.txt", 'wt') as file:
            file.write(siteData)
        return False
    else:
        with open("data.txt", "rt") as file:
            siteDataOld = file.read()
            # print("测试",len(siteDataOld), siteDataOld[:100] )
        # 之前抓取过网页，抓取，并比较。
        siteDataNew = getSite(url)
        with open("data.txt", "wt") as file:
            file.write(siteDataNew)
        similarity = fuzz.ratio(siteDataOld, siteDataNew)
        # print("测试:", similarity)
        if similarity < 99:
            return True
        else:
            return False
            
            
            
# 用邮件报告监控情况
def report():
    title = "发现网页更新"
    content = "发现网页有更新，累计监控次数:" + str(t)
    print(title, content)
    mail.sentMail(title, content)
    
    
# 监控过程
def task(url):
    bUpdate = compareData(url)
    if bUpdate == True:
        report()
    now = time.asctime(time.localtime(time.time()))
    print(now + "进行了一次监控")
    
    
# 每隔s分钟运行一次
def run(url, s):
    scheduler = BlockingScheduler(timezone="Asia/Chongqing")
    scheduler.add_job(task, "cron", day_of_week = "mon-sun", hour = "0-23", minute = "*/"+str(s), args = [url])
    scheduler.start()
    

if __name__ == "__main__":
    url = "改成你自己的被监控网址"
    s = 10
    run(url, s)
