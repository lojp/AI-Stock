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

```
\import os 
\from pytdx.reader import TdxMinBarReader, TdxFileNotFoundException 
\mypath = 'C:\\new_tdx\\vipdoc\\5fz\\' 
\os.chdir(mypath) 
\reader = TdxMinBarReader() 
\df = reader.get_df("sh600876.5") 
\print(df)
```

12, 利用通达信软件导出所有股票历史行情 \
https://my.oschina.net/huhaicool/blog/3010947 \


