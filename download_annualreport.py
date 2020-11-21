# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 09:37:17 2017
@author: jluo27
"""
import urllib.request
import re
import os
import pandas as pd
# import tushare as ts

# ts_token='0c98ac2886e4331d7120a91573d3d025ba2eec7c96bfac77f9b7153d'
# ts.set_token(ts_token)
# pro = ts.pro_api()


proxy = 'fmcpr002-p1.nb.ford.com:83'
os.environ['http_proxy'] = proxy 
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy

file_path = 'C:\\Private\\Analysis\\python\\mine\\stock'
if not os.path.exists(file_path):
    os.mkdir(file_path)
os.chdir(file_path)

# stock = []
# f=open('stock_num.txt')
# for line in f.readlines():
    # #print(line,end = '')
    # line = line.replace('\n','')
    # stock.append(line)
# #print(stock)
# f.close()
# #print(stock)

# stock = ['300400']
# df = pro.express(ts_code=stock[0], start_date='20200301', end_date='20200501', fields='ts_code,ann_date,yoy_sales,yoy_tp')  #800积分


# for each in stock:
    # url='http://money.finance.sina.com.cn/corp/go.php/vCB_Bulletin/stockid/'+each+'/page_type/ndbg.phtml'
    # req = urllib.request.Request(url)
    # req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
    # page = urllib.request.urlopen(req)
    # try:
        # html = page.read().decode('gbk')
        # target = r'&id=[_0-9_]{6|7}'
        # target_list = re.findall(target,html)
        # os.mkdir('./'+each)
        # sid = each
        # #print(target_list)
        # for each in target_list:
            # #print(a)
            # #print(each)
            # target_url='http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid='+sid+each
            # #print(target_url)
            # treq = urllib.request.Request(target_url)
            # treq.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
            # tpage = urllib.request.urlopen(treq)
            # try:
                # thtml = tpage.read().decode('gbk')
                # #print(thtml)
                # file_url = re.search('http://file.finance.sina.com.cn/211.154.219.97:9494/.*?PDF',thtml)
                # try:
                    # #print(file_url.group(0))
                    # local = './'+sid+'/'+file_url.group(0).split("/")[-1]+'.pdf'
                    # #调试用作文件占位
                    # #open(local, 'wb').write(b'success')
                    # #print(local)
                    # urllib.request.urlretrieve(file_url.group(0),local,None)
                # except:
                    # print('PDF失效;'+target_url)
            # except:
                # print('年报下载页面编码错误;'+target_url)
    # except:
        # print('年报列表页面编码错误;'+url)

stock = ['300142']
df = pd.read_csv('C:/Private/Analysis/python/mine/stock/2020q1.csv',encoding='utf-8')
df['scode'] = df['scode'].astype('str') #将原本的int数据类型转换为文本
df['scode']  = df['scode'].str.zfill(6) #用的时候必须加上.str前缀
new_df = df[df['scode']==stock[0]]
print(new_df[['scode','sname','ystz','sjltz']].to_string(index=False)) #ystz,sjltz

for each in stock:
    url='http://money.finance.sina.com.cn/corp/go.php/vCB_Bulletin/stockid/'+each+'/page_type/ndbg.phtml'
    if os.path.exists(file_path+'/'+each+'_2019.pdf'):
        os.remove(file_path+'/'+each+'_2019.pdf')
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
    page = urllib.request.urlopen(req)
    try:
        html = page.read().decode('gbk')
        target = r'(?<=&id=)\d+\.?\d*'
        target_list = re.findall(target,html)
        sid = target_list[0]
        target_url='http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid='+each+'&id='+sid
        treq = urllib.request.Request(target_url)
        treq.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
        tpage = urllib.request.urlopen(treq)
        thtml = tpage.read().decode('gbk')
        file_url = re.search('http://file.finance.sina.com.cn/211.154.219.97:9494/.*?PDF',thtml)
        local = './'+each+'_2019.pdf'
        urllib.request.urlretrieve(file_url.group(0),local,None)
        os.startfile(file_path+'/'+each+'_2019.pdf')
        # webbrowser.open_new(file_path)
    except:
        print('年报列表页面编码错误;'+url)