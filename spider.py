# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 23:24:34 2018

@author: susan
"""

import UrlManager
import Downloader
import threading
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class main(object):
    def __init__(self,root,threadNum):
        self.urls = UrlManager.UrlManager()
        self.download = Downloader.Downloader()
        self.root = root 
        self.threadNum = threadNum
        

    def _judge(self,domain,url):
        if url.find(domain) != -1:
            return True
        return False
        
    def _parse(self,page_url,content):
        if content is None:
            return 
        soup = BeautifulSoup(content,'html.parser')
        _news = self._get_new_urls(page_url,soup)
        return _news
        
    def _get_new_urls(self,page_url,soup):
        new_urls = set()
        links = soup.find_all('a')
        for link in links:
            new_url = link.get('href')
            new_full_url =urljoin(page_url,new_url)
            if (self._judge(self.root,new_full_url)):
                new_urls.add(new_full_url)
        return new_urls
    
    def craw(self):
        self.urls.add_new_url(self.root)
        while self.urls.has_new_url():
            _content = []
            th = []
            for i in list(range(self.threadNum)):
                if self.urls.has_new_url() is False:    
                    break
                new_url = self.urls.get_new_url()
                
                print("craw:"+ new_url)
                t = threading.Thread(target=self.download.download,args=(new_url,_content))
                t.start()
                th.append(t)
            for t in th :
                t.join()
            for _str in _content:
                if _str is None:
                    continue
                new_urls = self._parse(new_url,_str["html"])
                self.urls.add_new_urls(new_urls)
            
m = main('',1)
m.craw()
