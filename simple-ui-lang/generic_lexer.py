"""
Convert input into tokens.
"""

import re


def lex(characters, token_expressions):
    print('lex()')
    print('lex(), token_expressions=', token_expressions)
    pos = 0
    tokens = []
    size = len(characters)
    while pos < size:
        match = None
        for token_expr in token_expressions:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            raise SyntaxError('Illegal character at pos(' + str(pos) + '): ' + characters[pos])
        else:
            pos = match.end(0)
    return tokens
