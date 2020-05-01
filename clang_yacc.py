# -*- coding: utf-8 -*-
"""
    'WORDS',
    'NUMBER',
    'KAIGYO',
    'CORON',
    'ERROR',
    'WARNING',
    'NOTE',
    'POINT',
    'KIGO',
    'KAKKO',
    'SHUTYOU',
    'VAL',
    'ZENKAKU',
    'TEN',
    'ELSE'
"""
import ply.yacc as yacc
from clang_lex import tokens
import sys
args = sys.argv

def p_contents(p):
    'contents : placou sentence'
    p[0] = p[1] + p[2]
    print('contents')

def p_placecouse(p):
    'placou : place couse'
    p[0] = p[1] + p[2]
    print('hellow' + p[0])

def p_place(p):
    'place : filename points'
    p[0] = p[1] + p[2]
    print('hellow' + p[0])

def p_filename(p):
    'filename : WORDS TEN WORDS CORON'
    if(p[3]=='c'):
        p[0] = p[1] + p[2] + p[3] + p[4]
        print('clang file name:' + p[0])
    else:
        p[0] = p[1] + p[2] + p[3] + p[4]
        print('nomal word:' + p[0])

def p_points(p):
    'points : point point'
    p[0] = p[1] + p[2]
    print('points:' + p[0])

def p_point(p):
    'point : NUMBER CORON'
    p[0] = p[1] + p[2]
    print('point line:' + p[0])

def p_couse(p):
    '''couse : WARNING CORON
        | ERROR CORON
        | NOTE CORON'''
    p[0] = p[1] + p[2]
    print('hellow' + p[0])

def p_sentence(p):
    '''sentence : bun
        | jukugo '''
    if(len(p)==3):
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]
    print('sentence')

def p_jukugo(p):
    '''jukugo : WORDS
        | jukugo WORDS'''
    if(len(p)==3):
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]
    print('bunbun')

def p_bun(p):
    '''bun : jukugo VAL
        | bun jukugo'''
    p[0] = p[1] + p[2]
    print('ss')

def p_error(p):
    print(f"Undefined name {p!r}")

def yacc_test():
    path = 'errorsample/sample' + args[1] + '.txt'
    f = open(path,'r')
    data = f.read()
    parser = yacc.yacc()
    result = parser.parse(data)
    print('result: ', result)

if __name__ == '__main__':
    yacc_test()
