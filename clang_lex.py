# -*- coding: utf-8 -*-
import ply.lex as lex
# x=input("文字入力\n").rstrip()
x = '1911282.c: In function \'main\':\n1911282.c:12:1: error: expected \';\' before \'}\' token\n}'
# -*- encoding: utf-8 -*-
tokens = (
    'BUN',
    'NUMBER',
    'LBRACE',
    'RBRACE',
    'SEMI',
    'CORON',
    'VAL',
    'FILENAME'
)

t_FILENAME = '[a-zA-Z0-9]+\.c'
t_NUMBER = '[0-9]+'
t_BUN = '[a-zA-Z0-9]+[a-zA-Z]'
t_LBRACE = '{'
t_RBRACE = '}'
t_SEMI = ';'
t_ignore_COMMENT = '/\*[\s\S]*?\*/|//.*'
t_ignore = ' \t'
t_CORON = ':'
t_VAL = '\'[^\']+\''

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


def lex_test():
    lexer.input(x)
    print(lexer.token())
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
if __name__ == '__main__':
    print(x)
    lex_test()
