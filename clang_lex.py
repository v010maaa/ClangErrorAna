# -*- coding: utf-8 -*-
import ply.lex as lex
# x=input("文字入力\n").rstrip()
x = '1911282.c: In function \'main\':\n1911282.c:12:1: error: expected \';\' before \'}\' token\n}'
reserved = {
'function' : 'FUNCTION',
'error' : 'ERROR',
'.c' : 'KAKUTYOUSI',
'warning' : 'WARNING'
}
tokens = [
    'BUN',
    'NUMBER',
    'SEMI',
    'CORON',
    'VAL',
    'KAKKO',
    'SHUTYOU',
    'KIGO',
    'ZENKAKU',
    'ELSE'
] + list(reserved.values())

t_NUMBER = '[0-9]+'
t_BUN = r'(?!function)[a-zA-Z0-9ぁ-んァ-ン一-龥ー]*[a-zA-Zぁ-んァ-ン一-龥ー]+'
t_SEMI = ';'
t_ignore = ' \t　'
t_CORON = ':'
t_VAL = '\'[^\']+\''
t_KAKKO = '[\}\{\]\[\(\)\"]'
t_KIGO = '[\,\<\>\?\;\|\}\{\+\=\_\-\*\&\%\$\#\@\!\`\/]'
t_SHUTYOU = '\^[~]*'
t_ZENKAKU = '[^\x01-\x7E]'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


def lex_test():
    path = 'sample/sample1.txt'
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
    print(x)
    lex_test()
