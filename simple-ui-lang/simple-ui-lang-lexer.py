import generic_lexer
import sys


RESERVED = 'RESERVED'
ID = 'ID'


# Using array to keep elements in order
TOKEN_EXPRESSIONS = [
    (r'[ \n\t]+', None),
    (r'\\\\[^\n]*', None),
    
    ('(', RESERVED),
    (')', RESERVED),
    ('{', RESERVED),
    ('}', RESERVED),
    ('=', RESERVED),
    (',', RESERVED),
    (r'\'', RESERVED),
    
    (r'[a-zA-Z][a-zA-Z0-9_]*', ID)
]


def lex(characters):
    return generic_lexer.lex(characters, TOKEN_EXPRESSIONS)


def main():
    file = input('File to lex: ')
    text = open(file).read()
    tokens = lex(text, TOKEN_EXPRESSIONS)
    print(tokens)


if __name__ == '__main__':
    main()
