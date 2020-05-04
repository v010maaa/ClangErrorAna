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
    #print('all:' + p[0])
    
def p_allbefore(p):
    '''allbefore : lines
        | lines allbefore'''
    if(len(p)==3):
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]
    #print('all:' + p[0])

def p_lines(p):
    '''
    lines : main
        | lines line
    '''
    if(len(p)==3):
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]

    #print('lines:' + p[0])

def p_main(p):
    '''main : placecouse sentence
        | main KAIGYO'''
    if(p[2]==''):
        p[0] = ''
    else:
        p[0] = p[1] + p[2]
    #print('main:' + p[0])

def p_placecouse(p):
    '''placecouse : place couse
        | place
        | filename'''
    if(len(p)==3):
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]
    #print('placecouse:' + p[0])

def p_place(p):
    'place : filename points'
    p[0] =  p[2]
    #print('place:' + p[0])

def p_points(p):
    'points : point point'
    p[0] = p[1] + '行' + p[2] + '文字目付近'
    #print('points:' + p[0])


def p_point(p):
    'point : NUMBER CORON'
    p[0] = p[1]
    #print('point:' + p[0])

def p_couse(p):
    'couse : note CORON'
    p[0] = p[1]
    #print('couse:' + p[0])

def p_line(p):
    '''line : sentence KAIGYO
        | sentence'''
    p[0] = ''
    #if(len(p)==3):
    #    p[0] = p[1] + p[2]
    #else:
    #    p[0] = p[1]
    #print('line:' + p[0])


def p_sentence(p):
    '''sentence : bun
        | sentence warning
        | sentence sentence'''
    if(len(p)==3):
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]
    #print('sentence:' + p[0])


def p_warning(p):
    'warning : WTYPE'
    p[0] = '警告の種類は' + p[1] + 'です．'
    #print('warning:' + p[0])

def p_bun(p):
    '''bun :
        | jukugo
        | bun jukugo
        | bun TEN
        | jukugo TEN
        | bun CORON
        | jukugo CORON
        '''
    if(len(p)==3 and p[2]!='.' and p[2]!=':'):
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]
    #print('bun:' + p[0])


def p_filename(p):
    '''filename : jukugo TEN jukugo CORON '''
    #if(p[3]=='c'):
    #    p[0] = p[1] + p[2] + p[3] + p[4]
    #    print('filename:' + p[0])
    #else:
    #    p[0] = p[1] + p[2] + p[3] + p[4]
    #    print('nomal word:' + p[0])
    p[0] = ''


def p_jukugo(p):
    '''jukugo : WORDS
        | KIGO
        | NUMBER
        | note
        | jukugo jukugo'''
    if(len(p)==3):
        p[0] =  p[2] + p[1] 
    else:
        p[0] = ''
    #print('jukugo:' + p[0])
def p_jukugo2(p):
    'jukugo : jukugo VAL'
    if(p[1]==''):
        p[0] = ''
    else:
        p[0] = p[2] + p[1]

def p_funct(p):
    'jukugo : FUNCTION'
    p[0] = '関数は定義されていますか？'

def p_match(p):
    '''jukugo : MATCH'''
    p[0] = 'の括弧の対応ができていないらしい.'

def p_expe(p):
    'jukugo : EXPE'
    p[0] = 'が必要ですよ！'

def  p_undec(p):
    'jukugo : UNDECLEAR jukugo VAL'
    p[0] = p[3] + 'という宣言していない変数が使われているよ！'

def p_tarminate(p):
    'jukugo : TERMINATE'
    p[0] = 'の始点と終点はありますか？'

def p_undefi(p):
    'jukugo : UNDEFINE WORDS WORDS VAL'
    p[0] = p[4] + 'はスペルミスか存在していないかのどちらかの可能性が高いです.'

def p_note(p):
    '''note : NOTE
        | ERROR
        | WARNING'''
    if(p[1]=='error'):
        p[0] = 'で書き方を間違えている可能性があるよ！'
    elif(p[1]=='warning'):
        p[0] = 'でに警告が出ているよ！'
    else: 
        p[0] = 'の'
    #print('note:' + p[0])

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
    print('result:\n', result)


if __name__ == '__main__':
    yacc_test()
