# -*- coding: utf-8 -*-
"""BUN',
    'NUMBER',
    'SEMI',
    'CORON',
    'VAL',
    'KAKUTYOUSI',
    'FUNCTION',
    'ERROR',
    'KAKKO',
    'SHUTYOU',
    'KIGO',
    'ZENKAKU',
    'ELSE'
"""
import ply.yacc as yacc
from clang_lex import tokens
x = '1911282.c: In function \'main\':\n1911282.c:12:1: error: expected \';\' before \'}\' token\n}'

def p_all(p):
    '''all : function statement'''

def p_filename(p):
    '''filename : BUN KAKUTYOUSI SEMI
    | NUMBER KAKUTYOUSI SEMI'''
    p[0] = p[1] + p[2]
    print('filename' + p[0] + 'は')


def p_statement(p):
    '''statement : filename NUMBER CORON NUMBER CORON'''
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
    print('statement' + p[6])

def p_function(p):
    '''function : filename kansu CORON'''
    print('function')

def p_bunbun(p):
    '''bunbun : BUN bunbun
    | BUN'''
    print('bunbun')

def p_kansu(p):
    '''kansu : bunbun VAL'''
    print('kansu')

def p_sonota(p):
    '''kansu : bunbun VAL'''
    print('kansu')

def p_error(p):
    print('Syntax error in input!')

def yacc_test():
    path = 'sample/sample1.txt'
    f = open(path,'r')
    data = f.read()
    parser = yacc.yacc()
    result = parser.parse(data)
    print('result: ', result)

if __name__ == '__main__':
    yacc_test()
