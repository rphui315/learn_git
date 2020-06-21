# 需求获取 豆瓣电影Top250 内容
# https://movie.douban.com/top250?start=0
# 要求： 
#     获取电影名称，上映时间，评分
#     写入文本文件

# 加载各种包
import requests 
from bs4 import BeautifulSoup as bs


# 设置浏览器
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'

# 设置header
header = {'user-agent':user_agent}

# 设置地址
myurl = 'https://movie.douban.com/top250?start'

# 获取请求
response = requests.get(myurl,headers=header)

# 打印请求内容/状态码
# print(response.text)
# print(f'返回码是：{response.status_code}')

# 解析——效率低下方式
bs_info = bs(response.text,'html.parser')

# python 使用 for in 形式的循环
for tags in bs_info.find_all('div',attrs={'class':'hd'}):
    for atag in tags.find_all('a',):
        print(atag.get('href'))
        # 获取所以链接
        print(atag.find('span',).text)
        # 获取电影名字 

help(bs4)