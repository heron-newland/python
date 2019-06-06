#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests, sys

class DownLoader:


    def __init__(self):
        self.server = "https://www.biqukan.com"  #服务器地址
        self.url = "https://www.biqukan.com/0_790/" #目录地址
        self.names = [] #章节名称
        self.urls = []  #章节链接
        self.nums = 0   #章节数


    """
    获取所有章节的目录和链接
    """
    def getDownloadUrls(self):
        req = requests.get(self.url)
        bs = BeautifulSoup(req.text, 'html.parser')
        div_bf = bs.find_all('div', class_='listmain')
        bs_a = BeautifulSoup(str(div_bf[0]), 'html.parser')
        a = bs_a.find_all('a')
        for each in a:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))



    """
    获取章节内容
    """
    def getContent(self,url):
            req = requests.get(url)
            bs = BeautifulSoup(req.text, 'html.parser')
            html = bs.find_all('div', class_='showtxt')
            # 过滤结果中的br,等标签
            text = html[0].text
            # print(text)
            noblanktext = text.replace('\xa0' * 8, '\n\n')
            # print(noblanktext)
            return noblanktext

    """
    将内容写入磁盘
    """
    def writeDisc(self, name, path, content):
            with open(path, 'a', encoding='utf-8') as f:
                f.write(name + '\n')
                f.write(content + '\n')
                f.write('\n\n')



if __name__ == "__main__":
    downloader = DownLoader()
    downloader.getDownloadUrls()
    print('开始下载：')
    for i in range(len(downloader.urls)):
        downloader.writeDisc(downloader.names[i], '云尊.txt', downloader.getContent(downloader.urls[i]))
        sys.stdout.flush()
    print('下载完成')


"""
知识点:
    1.python的语法没有括号, 使用:, 代码块的结束位置通过代码的对齐方式确定, 所以在代码对齐缩进上要严谨
    2.学会使用requets框架进行http网络请求的基本使用
    3.学会使用Beautifulsoup对html字符串进行基本整理操作
    4.文件的I/O, 打开文件使用如下两种方式的区别:
        1> f = open(...)
        2> with open(...) as f:
        第一种方式要处理文件打开失败的异常,导致文件关闭的代码不执行, 所以要使用try ... finally确保文件关闭,代码比较繁琐
        第二种方式不需要处理异常, 会自动处理
    5.模块的导入方式
    6.类的基本使用
"""