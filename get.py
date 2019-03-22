#!/usr/bin/python
# -*-coding:utf8;-*-
import requests,re,sys
from bs4 import BeautifulSoup
# set encoding --------------- :
if (sys.getdefaultencoding != 'UTF-8') :
    reload(sys)
    sys.setdefaultencoding('UTF-8')
# set encoding --------------- ./

url = raw_input("请复制粘贴教程url:\n")
html = requests.get(url)
html.encoding = 'UTF-8'
soup = BeautifulSoup(html.text,'lxml')
links = soup.findAll('a',target="_top")
teachs = {}

for link in links :
    try :
        title = re.sub(r'\s',"",link.get_text())
        if (re.match(r'^/.$',link['href'])) :
            pass
        else :
            link['href'] = '/' + link['href']
        teachs[title] = requests.get('http://www.runoob.com'+link['href'])
        print '"'+title+'" 已解析'
    except :
        print '"'+title+'" 解析失败'
# write to file --------------------------------- :(
for title,got in teachs.items() :
#   set file name ----------------- :
    txtname = "%s.txt"%(title)
#   set file name ----------------- ./

#   load web page html ------------ :
    got.encoding = 'UTF-8'
    desc = BeautifulSoup(got.text,'lxml')
#   load web page html ------------ ./

#   read html --------------------- :
    contents = desc.find(class_='article-intro')
#   read html --------------------- ./

#   write ------------------------- :(

    try : 
        txt = open(txtname,'w')
        txt.write(contents.text)
        print '"'+title+'" 已保存'
    except :
        print '"'+title+'" 保存失败'
    txt.close()

#   write ------------------------- ./
# write to file --------------------------------- ./
