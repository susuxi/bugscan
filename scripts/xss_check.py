# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 20:44:01 2018

@author: susan
"""
import os
import sys
sys.path.append('..')
import PublicFunc
import Downloader

payload = []
filename = os.path.join(os.getcwd(),"data","xss_payload.txt")

f = open(filename)
for i in f:
    payload.append(i.strip())

class spider:
    def run(self,url,html):
        download = Downloader.Downloader()
        urls = PublicFunc.urlsplit(url)
        
        if urls is None:
            return False
        for _urlp in urls:
            for _payload in payload:
                _url = _urlp.replace("my_Payload",_payload)
                print("[xss test]:"+_url)
                _str = download.get(_url)
                
                if _str is None:
                    return False
                if _str.find(_payload)!= -1:
                    print("xss found:" + url)
        return False