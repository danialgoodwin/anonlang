"""
Convert input into tokens.
"""

import re

def lex(input, token_expressions):
    pos = 0
    tokens = []
    size = len(input)
    while pos < size:
        match = None
        for token_expr in token_expressions:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(input, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            raise SyntaxError(f'Illegal character: {input[pos]}')
        else:
            pos = match.end(0)
    return tokens
