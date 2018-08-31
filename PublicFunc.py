# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 23:54:26 2018
公共函数
@author: susan
"""

"""
取出url中的参数
"""
def urlsplit(url):
    domain = url.split("?")[0]
    _url = url.split("?")[-1] #所有参数
    param = {}
    for val in _url.split("&"):
        param[val.split("=")[0]] = val.split("=")[-1]
        
    urls = []
    for val in param.values():
        new_url = domain + _url.replace(val,"my_Payload")
        urls.append(new_url)
    return urls
    