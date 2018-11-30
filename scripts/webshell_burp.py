# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 19:59:43 2018

@author: susan
"""

import os 
import sys
sys.path.append('..')
import Downloader

filename = os.path.join(os.getcwd(),"data","webshell.dic")
payload = []
f = open(filename)

a = 0
for i in f:
    payload.append(i.strip())
    a += 1
    if a == 999:#单次post的参数数量
        break

class spider:
    def run (self,url,html):
        if not url.endswith(".php"):
            return False
        print("[webshell check]:",url)
        post_data = {}
        for _payload in payload:
            post_data[_payload] = 'echo "password is %s";'%_payload
        download = Downloader.Downloader()
        r = download.post(url,post_data)
        if r.find("password is") != -1:
            print("webshell:%s"%r)
            return True
            