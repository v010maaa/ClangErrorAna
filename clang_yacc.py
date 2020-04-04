# -*- coding: utf-8 -*-
import ply.yacc as yacc
from clang_lex import tokens
x = '1911282.c: In function \'main\':\n1911282.c:12:1: error: expected \';\' before \'}\' token\n}'

def p_all(p):
    '''all : function statement'''

def p_filename(p):
    '''filename : FILENAME CORON'''
    print('filename'+ p[1])
    p[0] = p[1] + p[2]


def p_statement(p):
    '''statement : filename NUMBER CORON NUMBER CORON'''
    print('statement')

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

def p_error(p):
    print('Syntax error in input!')

def yacc_test():
    print(x)
    parser = yacc.yacc()
    result = parser.parse(x)
    print('result: ', result)

if __name__ == '__main__':
    yacc_test()
