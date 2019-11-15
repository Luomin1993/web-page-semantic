#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import re
import sys
import jieba
import jieba.posseg as pseg
import unicodecsv

__author__ = 'hanss401';

def cut_and_flag(HAN_SENTENCE):
    WORDS_AND_FLAGS = pseg.cut(HAN_SENTENCE);
    return WORDS_AND_FLAGS;

def write_flags_to_file(WORDS_AND_FLAGS,FILE_NAME):
    with open(FILE_NAME,'a+') as FILE_STREAM:
        #WRITER = unicodecsv.writer(FILE_STREAM,encoding = 'gbk');
        for WORD,FLAG in WORDS_AND_FLAGS:
            #WRITER.writerows(WORD+';'+FLAG);
            #FILE_STREAM.write(WORD.encode('utf-8')+';'+FLAG);
            FILE_STREAM.write(WORD.encode('utf-8'));
            FILE_STREAM.write(';'+FLAG);
            FILE_STREAM.write('\n');

# ========= T E S T =========        
if __name__ == '__main__':
    HAN_SENTENCE_LIST =['小明硕士毕业于中国科学院计算所',
                        '后在日本京都大学深造',
                        '匹配到二进制文件',
                        '数据文件',];
    FILE_NAME = 'TEST_TOKEN.txt';
    for HAN_SENTENCE in HAN_SENTENCE_LIST:
        WORDS_AND_FLAGS = cut_and_flag(HAN_SENTENCE);
        write_flags_to_file(WORDS_AND_FLAGS,FILE_NAME);
