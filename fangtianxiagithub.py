# -*- coding: utf-8 -*-
"""
Created on Sep 01 09:37:17 2017

@author: lojp
"""

import os
import re
import time
import requests
import random
from bs4 import BeautifulSoup
import pandas

proxy = '***:***'
os.environ['http_proxy'] = proxy 
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy
sleeptime=random.randint(0, 3)

# res = requests.get('http://esf.suzhou.fang.com/')
# res = requests.get('http://esf.suzhou.fang.com/', timeout=random())
# soup = BeautifulSoup(res.text,'html.parser')


def getHouseDetil(url):
    info = {}
    import numpy as np
    res = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(res.text,'html.parser')
    info['标题'] = soup.select('title')[0].text.strip().replace(' - 房天下','')
    info['总价万'] = re.findall(r'\d+',soup.find_all("div", { "class" : "trl-item sty1" })[0].text.strip())[0]
    info['小区'] = re.sub(r'\<.*?\>', ' ',str(soup.find(id='agantesfxq_C03_05')))
    info['区域'] = re.sub(r'\n{2,}','\n',(re.sub(r'\n\s*\n+','',re.sub(r'\<.*?\>', ' ',str(soup.find(id='agantesfxq_C03_07'))).strip()).replace(' ','')))
    info['urls'] = url
    try:
        comA = soup.find_all("div", { "class" : ["trl-item1","text-item clearfix"]})
        comB = re.sub(r'\n{2,}','\n',(re.sub(r'\n\s*\n+','',re.sub(r'\<.*?\>', ' ',str(comA)).strip()).replace(' ','').replace(',','')))
        comC =comB.split('\n')
        comment = np.array(comC)
        j = len(comment)

        info['楼层'] = re.findall(r'\d+',comment[9])[0]
        info['位置'] = comment[8]

        suffix = ['户型','面积','单价','朝向','装修']
        prefix = ['有无电梯','产权性质','建筑结构','类别','挂牌时间','参考价格','同比去年','环比上月','物业类别','物业费','建筑类别','产权','建筑年代','绿化率','容积率','人车分流','总栋数']
        for k in range(len(comment)):
            if comment[k] in suffix:
                key = comment[k] 
                value = comment[k-1]
                info[key] = value
            elif comment[k] in prefix:
                key = comment[k] 
                value = comment[k+1]
                info[key] = value	
            else:	
                pass			
    except:
        pass
    return info


domain = 'http://esf.suzhou.fang.com'
url1 = 'http://esf.suzhou.fang.com/house/i3'
houslist = []
counter = 1
for i in range(1,2):
    res = requests.get(url1 + str(i))
    soup = BeautifulSoup(res.text,'html.parser')
    for house in soup.select('.houseList dl'):
        if len(house.select('.title')) > 0:
            link = house.select('.title a')[0]['href']
            url = domain + link 
            houslist.append(getHouseDetil(url))
            time.sleep(sleeptime)
            print(counter)
            counter = counter + 1


df = pandas.DataFrame(houslist)
df.to_excel('/house/house.xlsx')
