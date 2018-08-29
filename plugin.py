# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 16:48:31 2018

@author: susan
"""
import os
import sys
import traceback


class spiderplus(object):
    def __init__(self,plugin,disallow=[]): #script 插件目录名
        self.dir_exploit = []  #插件列表
        self.disallow = ['__init__']
        self.disallow.extend(disallow)
        self.plugin = os.getcwd()+'\\'+plugin #插件目录
        sys.path.append(plugin) #添加插件目录地址进环境变量
        
    def list_plusg(self):
        def filter_func(file):
            if not file.endswith(".py"):
                return False
            for disfile in self.disallow:
                if disfile in file:
                    return False
            return True
        dir_exploit = filter(filter_func,os.listdir(self.plugin)) #对插件目录中的文件进行过滤
        return dir_exploit
    
    def work(self,url,html):
        for _plugin in self.list_plusg():
            try:
                m = __import__(_plugin.split('.')[0]) #去除文件后缀并导入模块
                spider = getattr(m,'spider') #m.spider
                p = spider()
                s = p.run(url,html)
            except Exception as e: 
                traceback.print_exc()

#t = spiderplus('scripts')
#for plugin in t.list_plusg():
#    print(plugin)
