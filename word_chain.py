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
        #-^-  WRITER = unicodecsv.writer(FILE_STREAM,encoding = 'gbk');
        for WORD,FLAG in WORDS_AND_FLAGS:
            #-^-  WRITER.writerows(WORD+';'+FLAG);
            #-^-  FILE_STREAM.write(WORD.encode('utf-8')+';'+FLAG);
            FILE_STREAM.write(WORD.encode('utf-8'));
            FILE_STREAM.write(';'+FLAG);
            FILE_STREAM.write('\n');

def generator_to_list(GENERATOR_DATA):
    LIST_DATA = [];
    for DATA in GENERATOR_DATA:
        LIST_DATA.append(DATA);
    return DATA;    

def patter_classify(FLAG_A,FLAG_B):
    if FLAG_A[0]=='n' and FLAG_B=='v':
        return 'R1';
    if (FLAG_A=='v' or FLAG_A=='p')and FLAG_B[0]=='n':
        return 'R2';
    if FLAG_A[0]=='n' and FLAG_B=='ul':
        return 'R3';
    if (FLAG_A[0]=='a') or (FLAG_B=='uj'):
        return 'R4';
    return 'R5'                

def make_word_chain(WORDS_AND_FLAGS):
    WORD_CHAIN = [];
    WORDS_AND_FLAGS = list(WORDS_AND_FLAGS);
    for INDEX in range(len( WORDS_AND_FLAGS )-1):
        WORD_A,FLAG_A = WORDS_AND_FLAGS[INDEX  ];
        WORD_B,FLAG_B = WORDS_AND_FLAGS[INDEX+1];
        RELATION_AB = patter_classify(FLAG_A,FLAG_B);
        if INDEX==0:
            WORD_CHAIN += [WORD_A,RELATION_AB,WORD_B];
            continue;
        WORD_CHAIN += [RELATION_AB,WORD_B];
    #-^-  INDEX=0;
    #-^-  for WORD,FLAG in WORDS_AND_FLAGS:
    #-^-      RELATION_AB = patter_classify
    return WORD_CHAIN;    


# ========= T E S T =========        
if __name__ == '__main__':    
    # HAN_SENTENCE_LIST =['小明硕士毕业于中国科学院计算所',
    #                     '后在日本京都大学深造',
    #                     '匹配到二进制文件',
    #                     '数据文件',
    #                     '气死了快走好绿搬出去人民的力量'];
    # FILE_NAME = 'TEST_TOKEN.txt';
    # for HAN_SENTENCE in HAN_SENTENCE_LIST:
    #     WORDS_AND_FLAGS = cut_and_flag(HAN_SENTENCE);
    #     write_flags_to_file(WORDS_AND_FLAGS,FILE_NAME);
    HAN_SENTENCE = '小明硕士毕业于中国科学院计算所';
    WORDS_AND_FLAGS = cut_and_flag(HAN_SENTENCE);
    print make_word_chain(WORDS_AND_FLAGS);
