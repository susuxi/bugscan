# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 23:19:50 2018

@author: susan
"""
import sys
sys.path.append('..')
import Downloader

from urllib.parse import urlparse

DIR_PROBE_EXTS = ['.tar.gz','.zip','.rar','.tar.bz2']
FILE_PROBE_EXTS = ['.bak','.swp','.1']
download = Downloader()

def get_parent_paths(path):
    paths = []
    if not path or path[0] != '/':
        return paths
    paths.append(path)
    tph = path
    if path[-1] == '/':
        tph = path[:-1]
    while tph:
        tph = tph[:tph.rfind('/')+1]  #rfind?
        paths.append(tph)
        tph = tph[:-1]
    return paths

class spider:
    def run(self,url,html):
        pr = urlparse(url)
        paths = get_parent_paths(pr.path)
        web_paths = []
        
        for p in paths:
            if p == '/':
                for ext in DIR_PROBE_EXTS:
                    u = '%s://%s%s%s' % (pr.scheme,pr.netloc,p,pr.netloc+ext)
            else:
                if p[-1] == '/':
                    
