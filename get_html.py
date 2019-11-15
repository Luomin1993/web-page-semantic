#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import spider
import re
import sys
from progressbar import *
import datetime

__author__ = 'hanss401'

def html_to_file(URL_ADDR,FILE_NAME):
    HTML_CONTENT = spider.url_get(URL_ADDR,"gb2312").split('\n');
    with open(FILE_NAME,'a+') as FILE_STREAM:
        for LINE in HTML_CONTENT:
            FILE_STREAM.write(LINE);

# ========= T E S T =========        
if __name__ == '__main__':
    html_to_file('http://www.baidu.com','TEST.html');