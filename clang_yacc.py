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

def p_all(p):
    'all : allbefore'
    if(len(p)==3):
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]
    print('all:' + p[0])
    
def p_allbefore(p):
    '''allbefore : lines
        | lines allbefore'''
    if(len(p)==3):
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]
    print('all:' + p[0])

def p_lines(p):
    '''
    lines : main
        | lines line
    '''
    if(len(p)==3):
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]

    print('lines:' + p[0])

def p_main(p):
    '''main : placecouse sentence
        | main KAIGYO'''
    p[0] = p[1] + p[2]
    print('main:' + p[0])

def p_placecouse(p):
    'placecouse : place couse'
    p[0] = p[1] + p[2]
    print('placecouse:' + p[0])

def p_place(p):
    'place : filename points'
    p[0] = p[1] + p[2]
    print('place:' + p[0])

def p_points(p):
    'points : point point'
    p[0] = p[1] + p[2]
    print('points:' + p[0])


def p_point(p):
    'point : NUMBER CORON'
    p[0] = p[1] + p[2]
    print('point:' + p[0])

def p_couse(p):
    'couse : note CORON'
    p[0] = p[1] + p[2]
    print('couse:' + p[0])

def p_line(p):
    '''line : sentence KAIGYO
        | sentence'''
    if(len(p)==3):
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]
    print('line:' + p[0])


def p_sentence(p):
    '''sentence : bun
        | sentence warning
        | sentence sentence'''
    if(len(p)==2):
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]
    print('sentence:' + p[0])

def p_warning(p):
    'warning : LKAKU bun RKAKU'
    p[0] = p[1] + p[2] + p[3]
    print('warning:' + p[0])

def p_bun(p):
    '''bun :
        | jukugo
        | bun jukugo'''
    if(len(p)==3):
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]
    print('bun:' + p[0])


def p_filename(p):
    '''filename : jukugo TEN jukugo CORON'''
    if(p[3]=='c'):
        p[0] = p[1] + p[2] + p[3] + p[4]
        print('filename:' + p[0])
    else:
        p[0] = p[1] + p[2] + p[3] + p[4]
        print('nomal word:' + p[0])

def p_jukugo(p):
    '''jukugo : WORDS
        | KIGO
        | jukugo KIGO
        | jukugo WORDS
        | jukugo TEN
        | jukugo VAL
        | NUMBER note
        | jukugo NUMBER
        | jukugo note
        | jukugo CORON'''
    if(len(p)==3):
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]
    print('jukugo:' + p[0])

def p_note(p):
    '''note : NOTE
        | ERROR
        | WARNING'''
    p[0] = p[1]
    print('note:' + p[0])

def p_error(p):
    print('VVVVVVVVVVVVVVVVV')
    print(f"Undefined name {p!r}")
    print('人人人人人人人人人人人人')


def yacc_test():
    path = 'errorsample/sample' + args[1] + '.txt'
    f = open(path,'r')
    data = f.read()
    parser = yacc.yacc()
    result = parser.parse(data)
    print('result: ', result)


if __name__ == '__main__':
    yacc_test()
