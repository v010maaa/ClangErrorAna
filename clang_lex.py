# -*- coding: utf-8 -*-
import ply.lex as lex
import sys
args = sys.argv
# x=input("文字入力\n").rstrip()
tokens = [
    'WORDS',
    'NUMBER',
    'KAIGYO',
    'CORON',
    'ERROR',
    'WARNING',
    'NOTE',
    'POINT',
    'KIGO',
    'VAL',
    'TEN',
    'ELSE'
]
t_NUMBER = '[0-9]+' #数字の１回以上の繰り返し
t_WORDS = '(?!error)(?!warning)(?!note)[a-zA-Z0-9ぁ-んァ-ン一-龥ー]*[a-zA-Zぁ-んァ-ン一-龥ー]+[a-zA-Z0-9ぁ-んァ-ン一-龥ー]*'
#t_SEMI = ';'
t_NOTE = 'note'
t_ignore = ' \t　'
t_CORON = ':'
t_ERROR = 'error'
t_WARNING = 'warning'
t_VAL = '\'[^\']+\''
t_TEN = '.'
t_KIGO = '[\}\{\]\[\(\)\"\,\<\>\?\;\|\}\{\+\=\_\-\*\&\%\$\#\@\!\`\/^]'
#t_ZENKAKU = '[^\x01-\x7E]'

def t_KAIGYO(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


def lex_test():
    path = 'errorsample/sample' + args[1] + '.txt'
    f = open(path,'r')
    data = f.read()
    lexer.input(data)
    print(lexer.token())
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
if __name__ == '__main__':
    lex_test()
