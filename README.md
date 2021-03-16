# AI Stock
Web Crawling the house information from stock website

1，查sina \
https://www.google.com/search?rlz=1C1CHBD_en&ei=ae2CXqvmJMbb9QPOhqawBQ&q=site%3Afile.finance.sina.com.cn++%E2%80%9C%E8%85%BE%E8%AE%AF%E2%80%9D&oq=site%3Afile.finance.sina.com.cn++%E2%80%9C%E8%85%BE%E8%AE%AF%E2%80%9D&gs_lcp=CgZwc3ktYWIQA1DSV1jSV2DGWmgAcAB4AIABd4gByQKSAQMxLjKYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwjrvoLZlMToAhXGbX0KHU6DCVYQ4dUDCAs&uact=5 \
2, 搜东财 \
https://www.google.com/search?rlz=1C1CHBD_en&ei=DfKCXvCrO4T0rQGxiaXYDA&q=site%3Adata.eastmoney.com+%22%E9%BB%84%E5%85%89%E8%A3%95%22&oq=site%3Adata.eastmoney.com+%22%E9%BB%84%E5%85%89%E8%A3%95%22&gs_lcp=CgZwc3ktYWIQA1DrOVixwQhg7sMIaBRwAHgAgAF6iAHREpIBBDkuMTSYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwiw5taPmcToAhUEeisKHbFECcsQ4dUDCAs&uact=5 \
3, 深股查 \
https://www.google.com/search?source=hp&ei=UMFUXpmAMcK1rQHjxZjABA&q=site%3Acninfo.com.cn+%E5%A4%A7%E5%9F%BA%E9%87%91%E4%BA%8C%E6%9C%9F&oq=site%3Acninfo.com.cn+%E5%A4%A7%E5%9F%BA%E9%87%91%E4%BA%8C%E6%9C%9F&gs_l=psy-ab.3...826.30811..31112...9.0..0.186.2837.0j25......0....1j2..gws-wiz.....0..0i131j0j0i10j0i131i10.A0EP-LBR8mg&ved=0ahUKEwiZ6IyWjOznAhXCWisKHeMiBkgQ4dUDCAY&uact=5 \
4, 招股说明书 \
https://www.google.com/search?q=site%3Acsrc.gov.cn+%E4%B8%A4%E4%BC%9A&rlz=1C1CHBD_en&oq=site%3Acsrc.gov.cn+%E4%B8%A4%E4%BC%9A&aqs=chrome..69i57j69i58.20877j0j8&sourceid=chrome&ie=UTF-8 \
5, 年度报告 \
https://money.finance.sina.com.cn/corp/go.php/vCB_Bulletin/stockid/300694/page_type/ndbg.phtml \
6, 可转债 \
http://data.eastmoney.com/kzz/default.html \
7, 大基金 \
https://www.qixin.com/related/428d1493-9584-422d-8f45-11e0b17e06c6?section=investment \
8, 裁判文书 \
https://wenshu.court.gov.cn/ \
9, 看准网 \
https://m.kanzhun.com/wap/search \
10, 百度指数 \
http://index.baidu.com/v2/index.html# \
11, 通达信官网提供了所有券商行情的历史数据下载地址 \
https://www.tdx.com.cn/article/alldata.html \
可以使用pytdx打开，具体参考一下：\
https://pytdx-docs.readthedocs.io/zh_CN/latest/pytdx_reader/ \
12, 利用通达信软件导出所有股票历史行情 \
https://my.oschina.net/huhaicool/blog/3010947 \

```
import os 
from pytdx.reader import TdxMinBarReader, TdxFileNotFoundException 
mypath = 'C:\\new_tdx\\vipdoc\\5fz\\' 
os.chdir(mypath) 
reader = TdxMinBarReader() 
df = reader.get_df("sh600876.5") 
print(df)
```
```
if(len(df)>10):  #计算每只股票 10天以来的涨跌幅（大约2周）
        df['close2']  = df['close'].shift(10)
```

```
import pandas as pd
import tushare as ts
import os
import numpy as np
import operator
import time
import datetime
import baostock as bs
from opendatatools import stock
from dateutil.relativedelta import relativedelta

mypath = 'C:\\MyData\\Previous Analysis\\stock\\minsline\\'
os.chdir(mypath)

calendar_df = pd.read_hdf('calendar.h5', key='s')
common_type ={'预增':1, '续盈':1, '略增':1, '略减':1, '预减':0.5, '续亏':-1, '首亏':-1, '扭亏':0.5}
common_type_df = pd.DataFrame(common_type.items(), columns=['profitForcastType', 'epsTTM'])

date_df = pd.to_datetime(calendar_df.tail(2)['cal_date'], format = '%Y%m%d')
today = date_df.max().strftime('%Y%m%d')
today_ymd = date_df.max().strftime('%Y-%m-%d')
t = datetime.datetime.strptime(today,'%Y%m%d').date()
yesterday = date_df.min().strftime('%Y%m%d')
yesterday_ymd = date_df.min().strftime('%Y-%m-%d')
tomorrow_ymd = (t+relativedelta(days=1)).strftime('%Y-%m-%d')

def check_eps(code_name):
    rs_profit = bs.query_profit_data(code=code_name, year=2020, quarter=3)
    profit_report = rs_profit.get_data()
    b = profit_report[['statDate','epsTTM']]

    rs_forecast = bs.query_forecast_report(code_name, start_date="2019-01-01", end_date = yesterday_ymd)
    rs_forecast_list = []
    while (rs_forecast.error_code == '0') & rs_forecast.next():
        # 分页查询，将每页信息合并在一起
        rs_forecast_list.append(rs_forecast.get_row_data())
    result_forecast = pd.DataFrame(rs_forecast_list, columns=rs_forecast.fields)
    result_forecast_new = result_forecast.merge(common_type_df, on='profitForcastType')
    a = result_forecast_new[['profitForcastExpPubDate','epsTTM']]
    a.columns=['statDate','epsTTM']

    df = b.append(a)
    df['statDate'] = pd.to_datetime(df['statDate'], format = '%Y-%m-%d', errors = 'ignore')
    df['epsTTM'] = pd.DataFrame(df['epsTTM'], dtype=np.float)

    latest_eps = float(df[df['statDate']==df['statDate'].max()]['epsTTM'])
    return latest_eps

def bscodemaker(code):
    bs_code = 'sh.' + code if code[:1] == '6' else 'sz.' + code
    return bs_code

def stcodemaker(code):
    st_code =  code + '.SH' if code[:1] == '6' else  code + '.SZ'
    return st_code

TOKEN = '0c98ac2886e4331d7120a91573d3d025ba2eec7c96bfac77f9b7153d'
ts.set_token(TOKEN)
pro = ts.pro_api()
cons = ts.get_apis()

df_tscode = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')

# # jihe_df = ts.tick('002316', conn=cons, date=today_ymd)

data = pro.daily(trade_date=today)
data['code'] = data['ts_code'].str.split('.').str[0]
# data_3 = data[(data['high'] > data['pre_close']*1.092)& (data['open'] < data['close']) & (data['close'] > data['pre_close']*1.05) & (data['pct_chg'] < 21)]
data_3 = data[(data['high'] > data['pre_close']*1.092)& (data['open'] < data['close']) & (data['pct_chg'] < 21) & (data['pct_chg'] >6)]
# # # 0ts_code,1trade_date,2open,3high,4low,5close,6pre_close,7change,8pct_chg,9vol,10amount
print("昨日涨幅大于9%的股票共有{}只".format(data_3.shape[0]))

code_list = data_3['code'].tolist()
a=[]
b=[]
lg = bs.login()


# for i in range(len(code_list)):
    # if i >= len(code_list):
        # break
    # try:
        # code = code_list[i]
        # highvalue = float(data_3[data_3['code']==code]['high'])        
        # bs_code = bscodemaker(code)
        # rs = bs.query_history_k_data_plus(bs_code,"time,date,code,open,high,low,close,volume,amount",start_date=today_ymd, end_date=tomorrow_ymd,frequency="5", adjustflag="3")
        # df = rs.get_data()     #获取股票5分钟数据
        # df['time'] = pd.to_datetime(df['time'], format = '%Y%m%d%H%M%S%f', errors = 'ignore')
        # df['date'] = pd.to_datetime(df['date'], format = '%Y-%m-%d', errors = 'ignore')
        # df.iloc[:,6:] = pd.DataFrame(df.iloc[:,6:], dtype=np.float)#这个需要调整
        # df_group = df.nlargest(2,'volume',keep='first')
        # df_group_max = float(df_group['high'].max())
        # df_group_maxvolume = round(float(df_group['volume'].max())/100,0)
        # diff = (df_group['time'].max()-df_group['time'].min()).total_seconds()
        # open1 =float(df_group.iloc[:1]['open'])
        # open2 =float(df_group.iloc[-1:]['open'])
        # close1=float(df_group.iloc[:1]['close'])
        # close2=float(df_group.iloc[-1:]['close'])
        
        # if diff != 300 or open1 > close1 or open2 > close2 or highvalue != df_group_max:
            # code_list.pop(i)  
        # elif check_eps(bs_code)<0:  
            # code_list.pop(i) 
        # else:
            # a.append(code_list[i])
            # b.append(df_group_maxvolume)
    # except:
        # pass    




for i in range(len(code_list)):
    if i >= len(code_list):
        break
    try:
        code = code_list[i]
        bs_code = bscodemaker(code)
        highvalue = float(data_3[data_3['code']==code]['high'])
        df = ts.get_hist_data(code, ktype='5', start=today_ymd, end=tomorrow_ymd)
        df['time'] = pd.to_datetime(df.index)
        df_group = df.nlargest(2,'volume',keep='first')
        df_group_max = float(df_group['high'].max())
        df_group_maxvolume = float(df_group['volume'].max())
        diff = (df_group['time'].max()-df_group['time'].min()).total_seconds()
        open1 =float(df_group.iloc[:1]['open'])
        open2 =float(df_group.iloc[-1:]['open'])
        close1=float(df_group.iloc[:1]['close'])
        close2=float(df_group.iloc[-1:]['close'])
        
        if diff != 300 or open1 > close1 or open2 > close2 or highvalue != df_group_max:
            code_list.pop(i)  
        elif check_eps(bs_code)<0:  
            code_list.pop(i) 
        else:
            a.append(code_list[i])
            b.append(df_group_maxvolume)
    except:
        pass    

bs.logout()
code_volume = pd.DataFrame(list(zip(a, b)), columns=['symbol', '5min_volume_max'])
df_final = code_volume.merge(df_tscode, on='symbol').merge(data_3[['code','pct_chg']],left_on='symbol', right_on='code').sort_values(by=['pct_chg'], ascending=False)
ts.close_apis(cons)

ori_name_list = df_final['code'].apply(lambda x : stcodemaker(x)).str.cat(sep=',')
df_st, msg = stock.get_quote(ori_name_list)
df_st['volume']=df_st['volume']/100
df_st['code'] = df_st['symbol'].str.split('.').str[0]
csv_df = df_final[['code', 'name', 'area', 'industry','5min_volume_max','pct_chg']].merge(df_st[['code','volume','percent']], on='code')
csv_df['volumevs']=csv_df['volume']/csv_df['5min_volume_max']
print(csv_df.sort_values(by=['volumevs'], ascending=False))
csv_df.to_excel("output.xlsx",sheet_name='niugu') 
```
