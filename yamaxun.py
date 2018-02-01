import requests
from lxml import etree

r = requests.get('https://www.amazon.cn/%E8%A7%A3%E5%BF%A7%E6%9D%82%E8%B4%A7%E5%BA%97-%E4%B8%9C%E9%87%8E%E5%9C%AD%E5%90%BE/product-reviews/B00JZ96ZI8/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews')
s = etree.HTML(r.text)

comments = s.xpath('//*[@class="a-section celwidget"]')
for comment in comments:
    #获取用户名
    username = comment.xpath('./div[2]/span[1]/a/text()')
    #获取评论内容
    connect = comment.xpath('./div[4]/span[1]/text()')
    # #获取打分星级
    stars = comment.xpath('./div[1]/a[1]/i/span/text()')
    # #获取
    comment_time = comment.xpath('./div[2]/span[3]/text()')
    username ,connect, stars ,comment_time = username[0],connect[0],stars[0],comment_time[0] if comment_time else ''
    # for i in range(len(username)):
    #     print(username[i],connect[i])
    print('\n%s---%s---%s:\n%s'%(username,stars,comment_time,connect))
